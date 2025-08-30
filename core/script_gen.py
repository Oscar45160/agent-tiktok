import os, pathlib
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_PATH = pathlib.Path(__file__).resolve().parents[1] / "prompts" / "script_generator.txt"

def _read_template():
    return PROMPT_PATH.read_text(encoding="utf-8")

def generate_script(theme:str, lang:str="fr")->str:
    tmpl = _read_template()
    prompt = tmpl.format(theme=theme, lang=lang)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7,
        max_tokens=400
    )
    return resp.choices[0].message.content.strip()
