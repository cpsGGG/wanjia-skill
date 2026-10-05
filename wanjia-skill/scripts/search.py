"""Weighted lexical retrieval with shared effective-permission evaluation."""
import argparse,json,math,re,sys
from pathlib import Path
from resource_utils import internal_path, read_resource_json
from runtime_policy import STORE, permission_decision, permission_decisions
HOME=Path(__file__).resolve().parents[1]
WEIGHTS={'title':7,'claim':4,'reason':3,'method_or_meaning':4,'conditions':3,'limits':1,'evidence':0.5}
FILLERS=('如何','怎么','怎样','为什么','帮我','请问','能不能','无论','还是','一个','什么','提升','提高')

def tokens(query):
 query=query.lower()
 for word in FILLERS:query=query.replace(word,' ')
 result=set(re.findall(r'[a-z0-9][a-z0-9_-]*',query))
 for span in re.findall(r'[\u3400-\u9fff]+',query):
  if len(span)==1:continue
  result.update(span[i:i+2] for i in range(len(span)-1))
  if len(span)<=6:result.add(span)
 return result

def finite_action_available(decision):
 return (decision.get('allowed') is True and decision.get('requested')=='action_advice'
  and decision.get('payload_scope')=='finite_method_payload_only'
  and isinstance(decision.get('approved_payload'),dict)
  and isinstance(decision['approved_payload'].get('steps'),list)
  and bool(decision['approved_payload']['steps'])
  and isinstance(decision['approved_payload'].get('next_observation'),dict))

def search(query,limit=5,source_id=None,persona_only=False,action_only=False):
 rows=[r for r in STORE.rows() if (r.get('status') or {}).get('runtime_search_allowed') is not False]
 if source_id:rows=[r for r in rows if r['source_id']==source_id]
 terms=tokens(query)
 if not terms:return []
 texts=[{field:json.dumps(r.get(field),ensure_ascii=False).lower() for field in WEIGHTS} for r in rows]
 frequencies={term:sum(any(term in text for text in fields.values()) for fields in texts) for term in terms}
 results=[]
 for row,fields in zip(rows,texts):
  matched=[term for term in sorted(terms) if any(term in text for text in fields.values())]
  if not matched or (len(terms)>=4 and len(matched)<2):continue
  score=sum((1+math.log((1+len(rows))/(1+frequencies[t])))*sum(w for f,w in WEIGHTS.items() if t in fields[f]) for t in matched)*len(matched)/len(terms)
  results.append({'score':round(score,4),'matched_terms':matched,'entry':row,'permission_decision':None})
 for result,decision in zip(results,permission_decisions([r['entry'] for r in results],'action_advice' if action_only else 'personification')):result['permission_decision']=decision
 if action_only:results=[r for r in results if finite_action_available(r['permission_decision'])]
 elif persona_only:results=[r for r in results if r['permission_decision']['allowed'] is True]
 return sorted(results,key=lambda r:(-r['score'],r['entry']['id']))[:max(0,limit)]

def compact_result(result):
 row=result['entry']; entry={k:row[k] for k in ('id','source_id','title')}; truncated=[]
 for k in ('conditions_attribution','limits_attribution','mikey_explicit_conditions','editorial_use_limits'):
  if k in row:entry[k]=row[k]
 for key in ('claim','reason','method_or_meaning','conditions','limits'):
  value=row.get(key)
  if value is None:continue
  if isinstance(value,str):entry[key]=value[:220]+'…' if len(value)>220 else value; truncated += [key] if len(value)>220 else []
  elif isinstance(value,list):entry[key]=value[:3]; truncated += [key] if len(value)>3 else []
  else:entry[key]=value
 evidence=row.get('evidence',[]);entry['evidence_locations']=[{k:e.get(k) for k in ('sid','start','end','url')} for e in evidence[:2]];entry['evidence_count']=len(evidence)
 entry['status']=row.get('status',{});entry['truncated_fields']=truncated
 if evidence:entry['read_context_args']=['--source-id',row['source_id'],'--sid',evidence[0]['sid'],'--before','3','--after','3']
 if row.get('status',{}).get('payload_kind') in {'isolated_concept_atom','isolated_action_method'}:
  entry['payload_scope']=row['payload_scope'];entry['parent_knowledge_id']=row.get('parent_knowledge_id');entry['parent_knowledge_ids']=row.get('parent_knowledge_ids');entry['read_context_args'] += ['--knowledge-id',row['id']]
 return {'score':result.get('score'),'matched_terms':result.get('matched_terms',[]),'entry':entry,'permission_decision':result['permission_decision']}


def search_posts(query,limit=5,source_id=None):
 terms=tokens(query);sources=json.loads((HOME/'references/source-index.json').read_text(encoding='utf-8-sig'))['sources'];results=[]
 for source in sources:
  if source.get('source_kind')!='youtube_community_post' or (source_id and source['source_id']!=source_id):continue
  doc=read_resource_json(HOME,source['fulltext']);body=(doc.get('body') or '').lower();matched=[t for t in sorted(terms) if t in body]
  if not matched or (len(terms)>=4 and len(matched)<2):continue
  score=round((len(matched)/len(terms))*sum(body.count(t) for t in matched),4)
  results.append({'score':score,'matched_terms':matched,'result_kind':'community_post_body','source_id':source['source_id'],'title':source['title'],'date':source['date'],'url':source.get('url'),'body_preview':(doc.get('body') or '')[:360],'body_sid':doc['segments'][0]['sid'],'body_kind':doc.get('body_kind'),'body_verbatim_allowed':doc['segments'][0].get('verbatim_allowed',False),'body_source_scope':doc['segments'][0].get('source_scope'),'evidence_weight':source.get('evidence_weight',0),'effective_source_level':source.get('effective_source_level'),'source_level_does_not_authorize_knowledge':True,'image_refs':doc.get('image_refs',[]),'permission_decision':{'allowed':False,'reason':'community_post_candidate_evidence_only_runtime_answer_disabled'}})
 return sorted(results,key=lambda x:(-x['score'],x['source_id']))[:max(0,limit)]

def relation_results(kind,value):
 rows=STORE.rows(); sources=json.loads((HOME/'references/source-index.json').read_text(encoding='utf-8-sig'))['sources']; source_ids=set()
 if kind=='video_id': source_ids={s['source_id'] for s in sources if s.get('video_id')==value or s.get('url')==value}
 elif kind=='title': source_ids={s['source_id'] for s in sources if s.get('title')==value}
 if kind in {'video_id','title'}: selected=[r for r in rows if r['source_id'] in source_ids]
 elif kind=='theme_id': selected=[r for r in rows if value in ((r.get('related') or {}).get('theme_ids') or [])]
 elif kind=='proposition_id': selected=[r for r in rows if value in ((r.get('related') or {}).get('proposition_ids') or [])]
 elif kind=='related_id':
  anchor=STORE.exact(value)
  if anchor and anchor.get('status',{}).get('payload_kind') in {'isolated_concept_atom','isolated_action_method'}: selected=[]
  else: selected=[r for r in rows if r.get('parent_knowledge_id')==value]
 else: selected=[]
 return [{'score':None,'matched_terms':[kind],'entry':r,'permission_decision':d} for r,d in zip(selected,permission_decisions(selected))]

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('query',nargs='?');p.add_argument('--limit',type=int,default=5);p.add_argument('--source-id');p.add_argument('--id',dest='knowledge_id');p.add_argument('--raw-id');p.add_argument('--cache-id');p.add_argument('--theme-id');p.add_argument('--proposition-id');p.add_argument('--video-id');p.add_argument('--title');p.add_argument('--related-id');p.add_argument('--persona-only',action='store_true');p.add_argument('--action-only',action='store_true');p.add_argument('--full',action='store_true');p.add_argument('--include-posts',action='store_true');p.add_argument('--posts-only',action='store_true');a=p.parse_args()
 if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
 modes=[('id',a.knowledge_id),('raw_id',a.raw_id),('cache_id',a.cache_id),('theme_id',a.theme_id),('proposition_id',a.proposition_id),('video_id',a.video_id),('title',a.title),('related_id',a.related_id)]
 chosen=[x for x in modes if x[1] is not None]
 if len(chosen)>1 or (chosen and a.query):p.error('choose exactly one query or selector')
 if a.action_only and (a.persona_only or a.raw_id or a.cache_id or a.include_posts or a.posts_only):p.error('--action-only requires a knowledge query or selector, separately from persona/raw/cache/posts')
 if a.knowledge_id:
  row=STORE.exact(a.knowledge_id);results=[] if row is None else [{'score':None,'matched_terms':['exact_id'],'entry':row,'permission_decision':permission_decision(row)}];out={'mode':'full_record_by_id','knowledge_id':a.knowledge_id,'results':results}
 elif a.raw_id:out={'mode':'raw_history_with_effective_policy','knowledge_id':a.raw_id,'result':STORE.raw_original(a.raw_id)}
 elif a.cache_id:
  # Deliberately forge an unsafe stale cache; the store must ignore it and reread bytes.
  cached={'id':a.cache_id,'status':{'cross_use_level':'direct','first_person_allowed':True,'action_advice_allowed':True}}
  out={'mode':'stale_cache_reread','result':STORE.reread_cached(cached)}
 elif a.theme_id or a.proposition_id or a.video_id or a.title or a.related_id:
  kind,value=next(x for x in modes if x[1] is not None);results=relation_results(kind,value);out={'mode':'relation_lookup','relation_kind':kind,'relation_value':value,'results':results}
 else:
  if not a.query:p.error('query or selector required')
  knowledge=[] if a.posts_only else search(a.query,a.limit,a.source_id,persona_only=a.persona_only,action_only=a.action_only);posts=search_posts(a.query,a.limit,a.source_id) if (a.include_posts or a.posts_only) else [];out={'query':a.query,'mode':'community_posts_only' if a.posts_only else ('knowledge_and_community_posts' if a.include_posts else ('full' if a.full else 'compact_discovery_preview')),'results':posts if a.posts_only else ((knowledge if a.full else [compact_result(x) for x in knowledge])+posts)}
 if a.action_only and chosen and 'results' in out:
  for result,decision in zip(out['results'],permission_decisions([r['entry'] for r in out['results']],'action_advice')):result['permission_decision']=decision
  out['results']=[r for r in out['results'] if finite_action_available(r['permission_decision'])][:max(0,a.limit)]
 if a.knowledge_id and not a.full:
  out['mode']='compact_record_by_id'
  out['results']=[compact_result(r) for r in out['results']]
  for result in out['results']:
   locator=result['entry'].get('read_context_args')
   if locator is not None and '--knowledge-id' not in locator:locator += ['--knowledge-id',result['entry']['id']]
 if a.persona_only and 'results' in out: out['results']=[r for r in out['results'] if r.get('permission_decision',{}).get('allowed') is True]
 print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
