from pathlib import Path
import hashlib, csv, sys

ROOT = Path(__file__).resolve().parents[1]
ledger = ROOT / "07_provenance" / "EXPECTED_CANONICAL_HASH_LEDGER.csv"

search_roots = [
    ROOT/"04_data/source_recovered",
    ROOT/"04_data/full90",
    ROOT/"04_data/null_orientation",
    ROOT/"04_data/cadence",
]

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

fail=False
with open(ledger,newline="",encoding="utf-8") as f:
    for row in csv.DictReader(f):
        fn=row["expected_filename"]
        exp=row["expected_sha256"]
        found=[]
        for d in search_roots:
            p=d/fn
            if p.exists(): found.append(p)
        if not found:
            print(f"MISSING  {fn}  expected={exp}")
            continue
        for p in found:
            got=sha256(p)
            ok=(got==exp)
            print(("PASS   " if ok else "FAIL   ")+f"{p.relative_to(ROOT)}  {got}")
            fail |= not ok
sys.exit(1 if fail else 0)
