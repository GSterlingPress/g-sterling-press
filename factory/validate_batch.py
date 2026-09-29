import json, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
m=json.loads((root/"factory/batch-25.json").read_text())
assert len(m["themes"])==25, "batch must contain exactly 25 themes"
slugs=[t["slug"] for t in m["themes"]]
assert len(slugs)==len(set(slugs)), "duplicate theme slugs"
print("Batch manifest valid:", len(slugs), "unique themes")
