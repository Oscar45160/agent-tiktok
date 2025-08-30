import os, json, time, pathlib, logging
from dotenv import load_dotenv
from . import script_gen, scheduler
from ..tts.tts_engine import synthesize_tts
from ..montage.video_assembler import assemble_video
from ..publication.uploader import prepare_outputs

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL","INFO"))

def run_once(theme:str, lang:str="fr"):
    # 1) Générer script
    script_text = script_gen.generate_script(theme=theme, lang=lang)
    # 2) TTS
    audio_path = synthesize_tts(text=script_text, lang=lang)
    # 3) Montage
    video_path = assemble_video(audio_path=audio_path, script_text=script_text, lang=lang)
    # 4) Préparer upload (métadonnées + artefacts)
    meta = {"title": theme[:95], "description": theme, "tags": ["tiktok","shorts","ia"]}
    out = prepare_outputs(video_path=video_path, metadata=meta)
    logger.info("Pipeline terminé: %s", out)
    return out
