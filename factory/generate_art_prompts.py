import json, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
m=json.loads((root/"factory/batch-25.json").read_text())
out=root/"factory/art-prompts"; out.mkdir(parents=True,exist_ok=True)
for t in m["themes"]:
 d=out/t["slug"]; d.mkdir(exist_ok=True)
 motif=t["art_direction"]["motif"]
 common=f"G STERLING premium Galaxy theme {t['name']}. {motif}. Palette: {t['base']} with {t['accent']} accents. Original custom artwork only. No logos or baked-in text. Cinematic premium finish. Strong legibility zones for phone UI. Visually unique from every other collection."
 (d/"home.txt").write_text(common+" HOME: vertical 1440x3040, calm negative space for clock and icons, sophisticated depth.")
 (d/"lock.txt").write_text(common+" LOCK: vertical 1440x3040, related but compositionally distinct, focal structure away from clock and notifications.")
 (d/"ui-system.txt").write_text(common+" Coherent Messages, Dialer, Contacts, Settings, keyboard, quick panel, notifications, clock widget, plus eight semantically distinct app icons.")
print("Wrote",len(m["themes"]),"theme prompt packs")
