from __future__ import annotations
import copy, json, hashlib
from pathlib import Path

HOME=Path(__file__).resolve().parents[1]
KNOWLEDGE_PATH=HOME/'references/knowledge.jsonl'
VALID_LEVELS={'direct','context_only','hold','do_not_generalize'}
LEGACY_RUNTIME_HOLD_IDS={
 'mikey-gameshengjing-001-K0001','mikey-practice-003-K0002','mikey-practice-009-K0012',
 'mikey-sijiao-017-K0006','mikey-youtube-live-009-K0013','mikey-youtube-live-009-K0026',
 'mikey-youtube-live-010-K0003',
}


def _read_raw_rows():
    return [json.loads(line) for line in KNOWLEDGE_PATH.read_text(encoding='utf-8-sig').splitlines() if line.strip()]


_AUTHORITY=json.loads((HOME/'references/atom-authority.json').read_text(encoding='utf-8'))

def _compute_authoritative_policy(stored_row):
    row=copy.deepcopy(stored_row)
    authority=_AUTHORITY
    if row.get('id') in authority['parent_expected']:
        row.setdefault('status',{}).update(authority['parent_expected'][row['id']])
    if row.get('id') in authority['atom_payload_sha256']:
        actual=hashlib.sha256(json.dumps(stored_row,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        if actual!=authority['atom_payload_sha256'][row['id']]:
            row['status']={'cross_use_level':'hold','first_person_allowed':False,'action_advice_allowed':False,'runtime_notice':'atom_authoritative_payload_hash_mismatch'}
    stored_status=row.get('status')
    status=copy.deepcopy(stored_status) if isinstance(stored_status,dict) else {}
    row['status']=status
    claimed_runtime_computation=status.get('permission_computation')=='runtime_not_persisted'
    stored_level=status.get('cross_use_level')
    override=row.get('id') in LEGACY_RUNTIME_HOLD_IDS
    effective_level='hold' if override else stored_level
    status_present=isinstance(stored_status,dict)
    level_valid=type(stored_level) is str and stored_level in VALID_LEVELS
    first_present=status_present and 'first_person_allowed' in stored_status
    action_present=status_present and 'action_advice_allowed' in stored_status
    first_valid=first_present and type(stored_status.get('first_person_allowed')) is bool
    action_valid=action_present and type(stored_status.get('action_advice_allowed')) is bool
    schema_valid=status_present and level_valid and first_valid and action_valid
    if claimed_runtime_computation:
        # Never trust the marker itself.  A row that has already passed through
        # this function carries an audit of the original stored schema; require
        # that audit to be complete and internally consistent on every pass.
        # A forged/stale marker, or a runtime-filled false value for a field
        # that was originally absent, therefore remains fail closed.
        prior_presence=status.get('stored_permission_fields_present')
        prior_types=status.get('stored_permission_field_types_valid')
        prior_metadata_valid=(
          status.get('permission_schema_valid') is True and
          isinstance(prior_presence,dict) and
          prior_presence.get('first_person_allowed') is True and
          prior_presence.get('action_advice_allowed') is True and
          isinstance(prior_types,dict) and
          prior_types.get('cross_use_level') is True and
          prior_types.get('first_person_allowed') is True and
          prior_types.get('action_advice_allowed') is True
        )
        schema_valid=schema_valid and prior_metadata_valid
    # Permission fields are one fail-closed schema.  A missing or mistyped
    # action flag therefore also denies personification, and vice versa.
    effective_first=False if override or not schema_valid else stored_status['first_person_allowed']
    effective_action=False if override or not schema_valid else stored_status['action_advice_allowed']
    if stored_level!=effective_level:
        status['cross_use_level_as_stored']=stored_level
    status['cross_use_level']=effective_level
    status['first_person_allowed']=effective_first
    status['action_advice_allowed']=effective_action
    if override:
        status['direct_scope']=None
        status['runtime_notice']='legacy_forward_audit_hold; effective hold override merged before permission evaluation'
    elif not schema_valid:
        status['runtime_notice']='invalid or incomplete stored permission schema; runtime deny by default'
    status['permission_computation']='runtime_not_persisted'
    status['stored_permission_fields_present']={'first_person_allowed':first_present,'action_advice_allowed':action_present}
    status['stored_permission_field_types_valid']={'cross_use_level':level_valid,'first_person_allowed':first_valid,'action_advice_allowed':action_valid}
    status['permission_schema_valid']=schema_valid
    # Historical field name retained for compatibility; true now covers both
    # missing fields and invalid field types.
    status['default_denied_missing_fields']=not schema_valid
    status['effective_hold_override_applied']=override
    status['computed_marker_revalidated']=claimed_runtime_computation
    return row



def _deny_record(knowledge_id,reason,authoritative=None):
    row=copy.deepcopy(authoritative) if authoritative else {'id':knowledge_id}
    row['status']={'cross_use_level':'hold','first_person_allowed':False,'action_advice_allowed':False,'permission_schema_valid':False,'default_denied_missing_fields':True,'runtime_notice':reason,'permission_computation':'runtime_not_persisted'}
    return row

def _bind_caller(caller,index):
    if not isinstance(caller,dict):return _deny_record(None,'invalid_caller_record')
    kid=caller.get('id')
    authoritative=index.get(kid) if type(kid) is str else None
    if authoritative is None:return _deny_record(kid,'unknown_or_noncanonical_id')
    # All payload fields are exact; computed/cached status is ignored, never authority.
    body={k:v for k,v in caller.items() if k!='status'}
    canonical={k:v for k,v in authoritative.items() if k!='status'}
    if not _exact_json_equal(body,canonical):return _deny_record(kid,'caller_payload_differs_from_authority',authoritative)
    return _compute_authoritative_policy(authoritative)

def compute_effective_policy(caller):
    """Public inputs are untrusted; bind exact ID, body and stored status to fresh bytes."""
    index={r['id']:r for r in _read_raw_rows()}
    return _bind_caller(caller,index)

def _legacy_decision_from_effective(row,requested='personification'):
    if requested not in {'personification','action_advice'}:
        return {'knowledge_id':row.get('id'),'requested':requested,'allowed':False,'reason':'unsupported_request_mode_concept_only'}
    status=row['status']
    if status.get('permission_schema_valid') is not True:allowed=False;reason='invalid_or_incomplete_permission_schema'
    elif status.get('cross_use_level')!='direct':allowed=False;reason='effective_level_not_direct'
    elif status.get('first_person_allowed') is not True:allowed=False;reason='first_person_not_explicitly_allowed'
    elif requested=='action_advice' and status.get('action_advice_allowed') is not True:allowed=False;reason='action_advice_not_explicitly_allowed'
    else:allowed=True;reason='explicit_effective_permission'
    return {'knowledge_id':row.get('id'),'requested':requested,'allowed':allowed,'reason':reason,'effective_status':status}

_METHODS=json.loads((HOME/'references/method-authority.json').read_text(encoding='utf-8'))
def _exact_json_equal(left,right):
    try:
        return json.dumps(left,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)==json.dumps(right,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)
    except (TypeError,ValueError):return False
def _decision_from_effective(row,requested='personification',payload=None):
    decision=_legacy_decision_from_effective(row,requested)
    kid=row.get('id')
    if requested=='action_advice' and kid not in _METHODS:
        decision.update(allowed=False,reason='finite_action_pilot_requires_registered_payload')
        return decision
    if kid not in _METHODS:return decision
    if not decision['allowed']:return decision
    canonical=row['action_payload']
    actual=hashlib.sha256(json.dumps(canonical,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    if actual!=_METHODS[kid]['action_payload_sha256'] or (payload is not None and not _exact_json_equal(payload,canonical)):
        decision.update(allowed=False,reason='requested_payload_differs_from_reviewed_finite_payload')
        return decision
    decision.update(reason='exact_reviewed_finite_payload',payload_scope='finite_method_payload_only',
      approved_payload=copy.deepcopy(canonical),payload_sha256=actual,
      editorial_conditions=copy.deepcopy(row['editorial_conditions']),
      editorial_observation_is_not_source_explicit_rule=True,
      raw_transcript_authorized=False,parent_payload_inherited=False,
      quote_allowed=False,personal_history_allowed=False)
    return decision

def permission_decision(caller,requested='personification',payload=None):
    return _decision_from_effective(compute_effective_policy(caller),requested,payload)

def permission_decisions(callers,requested='personification'):
    """Batch public interface: one fresh authoritative index, no trusted caller rows."""
    index={r['id']:r for r in _read_raw_rows()}
    return [_decision_from_effective(_bind_caller(caller,index),requested) for caller in callers]

class KnowledgeStore:
    """Each read starts with fresh authoritative bytes; trusted traversal stays private."""
    def rows(self):return [_compute_authoritative_policy(r) for r in _read_raw_rows()]
    def raw_rows(self):return _read_raw_rows()
    def exact(self,knowledge_id):
        if type(knowledge_id) is not str:return None
        row=next((r for r in _read_raw_rows() if r.get('id')==knowledge_id),None)
        return _compute_authoritative_policy(row) if row else None
    def raw_original(self,knowledge_id):
        row=next((r for r in _read_raw_rows() if r.get('id')==knowledge_id),None)
        if not row:return None
        effective=_compute_authoritative_policy(row)
        return {'raw_record':copy.deepcopy((row.get('raw_notes') or {}).get('original_entry')),'authoritative_record':effective,'permission':_decision_from_effective(effective),'raw_fields_are_not_authority':True}
    def reread_cached(self,cached_row):
        kid=(cached_row or {}).get('id')
        row=next((r for r in _read_raw_rows() if r.get('id')==kid),None)
        if not row:return {'cache_input_id':kid,'found':False,'permission':{'allowed':False,'reason':'unknown_or_noncanonical_id'},'cache_security_fields_ignored':True}
        effective=_compute_authoritative_policy(row)
        return {'cache_input_id':kid,'found':True,'record':effective,'permission':_decision_from_effective(effective),'cache_security_fields_ignored':True,'authoritative_bytes_reread':True}

STORE=KnowledgeStore()
