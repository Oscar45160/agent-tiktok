import os, tempfile, pathlib
from moviepy.editor import AudioFileClip, TextClip, CompositeVideoClip, ColorClip

def assemble_video(audio_path:str, script_text:str, lang:str="fr")->str:
    audio = AudioFileClip(audio_path)
    w, h = 1080, 1920  # format vertical
    bg = ColorClip(size=(w,h), color=(0,0,0), duration=audio.duration)
    caption = TextClip(script_text[:120]+"...", fontsize=60, font="Arial", method="caption", size=(w-120,None))
    caption = caption.set_position(("center","center")).set_duration(min(8, audio.duration))
    video = CompositeVideoClip([bg, caption]).set_audio(audio)
    out = tempfile.mktemp(suffix=".mp4")
    video.write_videofile(out, fps=30, codec="libx264", audio_codec="aac", verbose=False, logger=None)
    return out
