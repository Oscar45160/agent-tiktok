import os, pathlib, json

def prepare_outputs(video_path:str, metadata:dict):
    out_dir = pathlib.Path(os.getenv("OUTPUT_DIR","out")).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / (metadata.get("title","video") + ".mp4")
    # copie sans renommage robuste (simplifié)
    import shutil
    shutil.copyfile(video_path, target)
    (out_dir / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"video": str(target), "metadata": str(out_dir / "metadata.json")}
