import json, pathlib, shutil
root=pathlib.Path(__file__).resolve().parents[1]
m=json.loads((root/"factory/batch-25.json").read_text())
out=root/"factory/submission-packs"; out.mkdir(parents=True,exist_ok=True)
req=["home_1440x3040.png","lock_1440x3040.png","messages_1440x3040.png","dialer_1440x3040.png","contacts_1440x3040.png","settings_1440x3040.png","metadata.json"]
for t in m["themes"]:
 d=root/"factory/themes"/t["slug"]; dest=out/t["slug"]; dest.mkdir(exist_ok=True)
 missing=[x for x in req if not (d/x).exists()]
 status={"collection":t["collection"],"name":t["name"],"ready_for_themes_studio":not missing,"missing":missing}
 (dest/"submission-status.json").write_text(json.dumps(status,indent=2)+"\n")
 if not missing:
  for x in req: shutil.copy2(d/x,dest/x)
print("Prepared handoff status for",len(m["themes"]),"themes")
