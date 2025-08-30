# Agent TikTok Automatisé (Starter)

Pipeline minimal pour générer un script, TTS, assembler une vidéo courte et préparer l'upload
(TikTok/YouTube/Instagram), conçu pour être piloté par un **agent ChatGPT** ou lancé en CLI.

## Démarrage rapide

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # renseigne tes clés
python core/run_pipeline.py --theme "astuce cybersécurité du jour" --lang fr
```

## Structure

- `core/agent.py` : orchestration pas-à-pas
- `core/run_pipeline.py` : point d'entrée CLI (idéal pour l'agent)
- `prompts/script_generator.txt` : prompt modèle pour écrire le script
- `tts/tts_engine.py` : TTS (ElevenLabs ou fallback simple via gTTS)
- `montage/video_assembler.py` : assemble la voix + sous-titres + B-roll
- `publication/` : sorties et placeholders pour upload APIs
- `config/themes_historique.json` : anti-doublon

## Notes publication

- **TikTok** : utiliser la Content Posting API (Direct Post ou Upload + Draft).
- **YouTube Shorts** : utiliser `videos.insert` (quota 1600/vidéo).
- **Instagram Reels** : via Instagram Graph API (upload + publish).

Tu peux déclencher le pipeline 3×/jour (cron) ou via des **Tasks** de ChatGPT Agent.
