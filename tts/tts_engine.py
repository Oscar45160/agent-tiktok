import os, tempfile, pathlib
from dotenv import load_dotenv
load_dotenv()

# Placeholder: remplace par ElevenLabs ou Coqui
def synthesize_tts(text:str, lang:str="fr")->str:
    # Pour un starter simple, on crée un faux audio silencieux via ffmpeg
    # (à remplacer par un vrai TTS)
    from moviepy.editor import AudioClip
    import numpy as np
    def make_sound(t):
        return 0.0
    duration = max(6, min(60, len(text)/18))
    ac = AudioClip(make_sound, duration=duration, fps=44100)
    out = tempfile.mktemp(suffix=".wav")
    ac.write_audiofile(out, fps=44100, nbytes=2, codec="pcm_s16le", verbose=False, logger=None)
    return out
