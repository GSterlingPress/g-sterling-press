import json, pathlib, subprocess, sys, shutil, hashlib
root=pathlib.Path(__file__).resolve().parents[1]
out=root/"factory/out"; out.mkdir(parents=True,exist_ok=True)
m=json.loads((root/"factory/batch-25.json").read_text())
target=(sys.argv[1] if len(sys.argv)>1 else "ALL").lower()
selected=[t for t in m["themes"] if target=="all" or t["slug"]==target]
built=[]; blocked=[]
for t in selected:
    d=root/"factory/themes"/t["slug"]
    home=d/"home_1440x3120.png"; lock=d/"lock_1440x3120.png"
    if not home.exists() or not lock.exists():
        blocked.append((t["slug"],"missing unique home/lock masters")); continue
    if hashlib.sha256(home.read_bytes()).digest()==hashlib.sha256(lock.read_bytes()).digest():
        blocked.append((t["slug"],"home and lock masters are identical")); continue
    # Production factory intentionally fails closed until each candidate has its own art.
    # The OBSIDIAN Android host remains the validated build master; Samsung Themes Studio
    # packaging is a separate approved-designer step and must not be misrepresented here.
    built.append(t["slug"])
(out/"batch-report.txt").write_text("BUILT CANDIDATES\n"+"\n".join(built)+"\n\nBLOCKED\n"+"\n".join(f"{a}: {b}" for a,b in blocked)+"\n")
print("ready:",built); print("blocked:",blocked)
