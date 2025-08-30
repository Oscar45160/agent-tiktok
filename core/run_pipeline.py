import argparse
from .agent import run_once


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--theme", required=True)
    p.add_argument("--lang", default="fr")
    p.add_argument("--dummy", action="store_true", help="Mode test sans API (texte et audio factices)")
    args = p.parse_args()

    if args.dummy:
        # Mode dummy: bypass API et TTS
        script_text = f"[DUMMY MODE] Vidéo test sur le thème: {args.theme}"
        from ..tts.tts_engine import synthesize_tts
        from ..montage.video_assembler import assemble_video
        from ..publication.uploader import prepare_outputs
        audio_path = synthesize_tts(text=script_text, lang=args.lang)
        video_path = assemble_video(audio_path=audio_path, script_text=script_text, lang=args.lang)
        meta = {
            "title": f"dummy-{args.theme[:50]}",
            "description": "Dummy video",
            "tags": ["dummy"]
        }
        out = prepare_outputs(video_path=video_path, metadata=meta)
        print(out)
    else:
        out = run_once(theme=args.theme, lang=args.lang)
        print(out)


if __name__ == "__main__":
    main()
