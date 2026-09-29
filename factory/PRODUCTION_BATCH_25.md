# OBSIDIAN Production Factory — Batch 25

OBSIDIAN #002 is the validated Android/Gradle production master.

This branch adds the first 25-theme production queue. It deliberately **fails closed** rather than cloning OBSIDIAN art into fake products. Each candidate must receive unique Home and Lock masters plus its complete-theme asset set before it is marked buildable.

## Samsung distribution boundary
Galaxy Themes sold as themes must be produced with Samsung Galaxy Themes Studio by an approved Themes designer and distributed through Galaxy Store. The ordinary Gradle APK host is retained for engineering/phone testing; it is not labeled as a Galaxy Themes Studio store package.

## Batch
Collections 003–027 are declared in `factory/batch-25.json`.

Run **Theme Factory Batch 25** manually. The workflow validates all 25 and reports which candidates have the required unique masters.
