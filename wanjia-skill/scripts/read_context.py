"""Read source/SID evidence; an evidence locator never creates persona permission."""
import argparse,hashlib,json,sys
from pathlib import Path
from resource_utils import internal_path, read_resource_json
from runtime_policy import STORE, permission_decision, permission_decisions
HOME=Path(__file__).resolve().parents[1]

def evidence_policy_context(source, returned_sids):
 """Expose source identity and effective knowledge policy without granting by SID."""
 matching=[]
 rows=STORE.rows()
 decisions={r['id']:d for r,d in zip(rows,permission_decisions(rows))}
 actions={r['id']:d for r,d in zip(rows,permission_decisions(rows,'action_advice'))}
 for row in rows:
  if row.get('source_id')!=source['source_id']:continue
  cited=sorted({e.get('sid') for e in row.get('evidence',[]) if e.get('sid') in returned_sids})
  if not cited:continue
  status=row['status']
  matching.append({'knowledge_id':row['id'],'matched_sids':cited,'claim':row.get('claim'),
   'conditions':row.get('conditions'),'limits':row.get('limits'),'effective_status':status,
   'conditions_attribution':row.get('conditions_attribution'),'limits_attribution':row.get('limits_attribution'),
   'mikey_explicit_conditions':row.get('mikey_explicit_conditions'),'editorial_use_limits':row.get('editorial_use_limits'),
   'speaker':status.get('speaker'),'speaker_claim_scope':status.get('speaker_claim_scope'),
   'content_origin':status.get('content_origin'),'personification_permission':decisions[row['id']],
   'action_advice_permission':actions[row['id']]})
 return {'source_identity':{k:source.get(k) for k in (
  'source_id','source_kind','formal_weight','dedup_decision','canonical_source_ids','zero_weight_reason',
  'permissions','first_person_allowed','action_advice_allowed','runtime_answer_allowed',
  'effective_source_level','evidence_weight','coverage','novelty_status','runtime_notice',
  'candidate_transcript_remediation','project_source_path','body_kind','body_verbatim_allowed',
  'untrimmed_transcript','untrimmed_transcript_sha256','excluded_segments_ledger',
  'excluded_segments_ledger_sha256','untrimmed_timing_status')},
  'matched_knowledge':matching,
  'rules':{'evidence_locator_grants_permission':False,'source_permission_overrides_knowledge':False,
   'no_matching_knowledge_means_authorized':False,'context_only_can_form_standalone_conclusion':False,
   'hold_or_do_not_generalize_can_support_persona_or_action_advice':False,
   'reuse_or_reuse_pending_adds_independent_weight':False},
  'notice':'Raw transcript/post words are evidence, not an authorization or verified speaker assignment. Consult each matched effective knowledge record; uncatalogued words remain unapproved. Zero-weight/reuse sources never add independent corroboration.'}
def timestamp_url(url,start):
 if not url:return None
 return url+('&' if '?' in url else '?')+'t='+str(int(start))

def attach_audio_correction_context(source,result):
 """Show existing review candidates beside preserved ASR; never grant permission."""
 value=source.get('audio_correction_overlay')
 if not value:return result
 path=internal_path(HOME,value);overlay=read_resource_json(HOME,value)
 if overlay.get('source_id')!=source['source_id']:raise ValueError('Audio correction/source mismatch')
 if not isinstance(overlay.get('corrections'),list):raise ValueError('Invalid audio correction records')
 overlay_sha=hashlib.sha256(path.read_bytes()).hexdigest()
 navigation_value='references/audio-correction-evidence/navigation.json';navigation=None;navigation_sha=None
 if (HOME/navigation_value).is_file():
  navigation_path=internal_path(HOME,navigation_value)
  navigation_sha=hashlib.sha256(navigation_path.read_bytes()).hexdigest()
  navigation=read_resource_json(HOME,navigation_value)
  if navigation.get('source_id')!=source['source_id'] or navigation.get('overlay_sha256')!=overlay_sha:raise ValueError('Audio correction navigation/source binding mismatch')
 returned={s['sid']:s for s in result['segments']};records=[]
 for record in overlay['corrections']:
  sid=record.get('segment_id')
  if sid not in returned:continue
  item={'review_record':record,'automatic_text_matches_returned_asr':record.get('automatic_text')==returned[sid]['text'],
   'transcript_text_replaced':False,'independent_local_listening_claimed':False,
   'permission_granted':False,'verbatim_certified':False}
  if navigation:item['internal_evidence']=navigation.get('segments',{}).get(sid)
  returned[sid].update(text_status='automatic_asr_with_separate_audio_review_not_a_definite_reading',
   correction_review_required=True,text_must_not_be_used_as_definite_reading=True,
   correction_candidate=record.get('web_audio_candidate'),correction_candidate_status=record.get('status'),
   independent_local_audio_review=record.get('independent_local_audio_review'),audio_correction=item)
  records.append(item)
 result['audio_correction_context']={'overlay_path':value,'overlay_sha256':overlay_sha,
  'scope':overlay.get('scope'),'policy':overlay.get('policy'),'records':records,
  'evidence_navigation_path':navigation_value if navigation else None,'evidence_navigation_sha256':navigation_sha,
  'transcript_text_replaced':False,'timing_recalibrated':False,'permission_granted':False,
  'editorial_notice':'text保留自动稿原字。review_record另列既有网页音频候选、真实status、独立听校状态与未决问题；supported_web_audio仅为已提供网页结果支持，不能称本地独立听校、认证原话或已验证事实。涉及否定方向、人物身份或效果时同时读取完整限制；unresolved候选不能据此定案。没有本窗记录也不等于该段已核实。'}
 return result

def read_context(source_id,sid,before=3,after=3,untrimmed=False,knowledge_id=None):
 if before<0 or after<0:raise ValueError('before/after must be nonnegative segment counts')
 sources=json.loads((HOME/'references/source-index.json').read_text(encoding='utf-8'))['sources'];source=next((s for s in sources if s['source_id']==source_id),None)
 if source is None:raise ValueError('Unknown source_id: '+source_id)
 content_key='untrimmed_transcript' if untrimmed else ('fulltext' if source.get('source_kind')=='youtube_community_post' else 'transcript')
 if content_key not in source:raise ValueError('No preserved untrimmed transcript registered for '+source_id)
 transcript=read_resource_json(HOME,source[content_key]);segments=transcript['segments'];ids=[s.get('segment_id',s.get('sid',s.get('id'))) for s in segments]
 if sid not in ids:raise ValueError('Unknown SID for this source: '+sid)
 index=ids.index(sid);result=[]
 for i in range(max(0,index-before),min(len(segments),index+after+1)):
  s=segments[i];result.append({'sid':ids[i],'start':s.get('start'),'end':s.get('end'),'text':s['text'],'is_target':i==index,'url':source.get('url') if source.get('source_kind')=='youtube_community_post' else timestamp_url(source.get('url'),s['start']), 'segment_kind':s.get('kind','automatic_transcript_segment'),'verbatim_allowed':s.get('verbatim_allowed',False),'source_scope':s.get('source_scope'),'speaker':s.get('speaker'),'speaker_assignment_status':s.get('speaker_assignment_status','not_proven_by_raw_segment')})
 return attach_audio_correction_context(source,bind_atom_context({'source_id':source_id,'source_kind':source.get('source_kind','youtube_local_video'),'title':source['title'],'source_url':source.get('url'),'target_sid':sid,'window_units':'consecutive source segments, not seconds','segments':result,'body_kind':transcript.get('body_kind'),'untrimmed_archive_read':untrimmed,'time_alignment_status':'unreliable_not_verified' if untrimmed else source.get('untrimmed_timing_status','as_stored_not_sentence_by_sentence_verified'),'image_refs':transcript.get('image_refs',[]) if source.get('source_kind')=='youtube_community_post' else [],'permission_decision':{'allowed':False,'reason':'source_id_plus_sid_is_evidence_locator_not_knowledge_permission'},'evidence_policy_context':evidence_policy_context(source,{s['sid'] for s in result}),'status':({'text':'archived_public_post_body','listening':'not_applicable','visual':'reference_metadata_only_no_image_packaged'} if source.get('source_kind')=='youtube_community_post' else {'text':source['text_status'],'listening':source['listening_status'],'visual':source['visual_status']})},knowledge_id))
def bind_atom_context(result,knowledge_id):
 row=STORE.exact(knowledge_id) if knowledge_id else None
 if knowledge_id and row is None: raise ValueError('Unknown exact knowledge_id')
 if row and row['source_id']!=result['source_id']: raise ValueError('Knowledge/source mismatch')
 atom=row and row.get('status',{}).get('payload_kind')=='isolated_concept_atom'
 approved=set(row['payload_scope']['approved_evidence_sids']) if atom else set()
 if atom and result['target_sid'] not in approved: raise ValueError('Target SID outside selected atom evidence')
 for segment in result['segments']:
  segment['usage']={'kind':'research_original_context_only','personification_allowed':False,'action_advice_allowed':False,'raw_words_verbatim_certified':False,'selected_atom_evidence_reference':bool(atom and segment['sid'] in approved),'reference_owner_knowledge_id':knowledge_id if atom and segment['sid'] in approved else None}
 result['selected_knowledge_id']=knowledge_id
 result['approved_concept_payload']=None
 if atom:
  result['approved_concept_payload']={'knowledge_id':row['id'],'claim':row['claim'],'reason':row['reason'],'reason_attribution':row.get('reason_attribution'),'editorial_use_limits':row.get('editorial_use_limits'),'example_modality':row.get('example_modality'),'permission':permission_decision(row),'action_advice_permission':permission_decision(row,'action_advice'),'text_scope':['claim','reason'],'approved_evidence_sids':row['payload_scope']['approved_evidence_sids'],'parent_payload_inherited':False}
  result['approved_atom_evidence_references']=[e for e in row['evidence'] if e['sid'] in {s['sid'] for s in result['segments']}]
 for match in result['evidence_policy_context']['matched_knowledge']:
  match['row_permission_applies_to_raw_transcript']=False
  match['raw_transcript_personification_allowed']=False
  match['raw_transcript_action_advice_allowed']=False
 result['context_has_no_persona_payload_inheritance']=True
 return bind_method_context(result,row)

def bind_method_context(result,row):
 method=row and row.get('status',{}).get('payload_kind')=='isolated_action_method'
 result['approved_action_payload']=None
 if method:
  approved=set(row['payload_scope']['approved_evidence_sids'])
  if result['target_sid'] not in approved:raise ValueError('Target SID outside selected method evidence')
  for segment in result['segments']:
   segment['usage']['selected_method_evidence_reference']=segment['sid'] in approved
   segment['usage']['reference_owner_knowledge_id']=row['id'] if segment['sid'] in approved else None
  result['approved_action_payload']=permission_decision(row,'action_advice')
  result['approved_method_evidence_references']=[e for e in row['evidence'] if e['sid'] in {s['sid'] for s in result['segments']}]
 for match in result['evidence_policy_context']['matched_knowledge']:
  for key in ('personification_permission','action_advice_permission'):
   match[key].pop('approved_payload',None)
   match[key]['payload_requires_exact_knowledge_binding']=True
 return result

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-id',required=True);p.add_argument('--sid',required=True);p.add_argument('--before',type=int,default=3);p.add_argument('--after',type=int,default=3);p.add_argument('--untrimmed',action='store_true');p.add_argument('--knowledge-id');a=p.parse_args()
 try:r=read_context(a.source_id,a.sid,a.before,a.after,a.untrimmed,a.knowledge_id);code=0
 except (ValueError,OSError) as e:r={'error':str(e),'permission_decision':{'allowed':False,'reason':'invalid_evidence_locator'}};code=2
 if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
 print(json.dumps(r,ensure_ascii=False,indent=2));return code
if __name__=='__main__':raise SystemExit(main())
