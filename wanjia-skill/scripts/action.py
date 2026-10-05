"""Return only an exact reviewed finite next-step payload."""
import argparse,json,sys
from pathlib import Path
from runtime_policy import STORE,permission_decision
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--id',required=True);p.add_argument('--payload-file');a=p.parse_args()
row=STORE.exact(a.id);payload=json.loads(Path(a.payload_file).read_text(encoding='utf-8')) if a.payload_file else None
decision=permission_decision(row,'action_advice',payload)
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
print(json.dumps(decision,ensure_ascii=False,indent=2))
