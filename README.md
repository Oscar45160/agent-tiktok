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
- - 'config/themes_historique.json' : anti-doublon



## Mode Dummy

Ce projet inclut un mode de test qui ne consomme aucune clé API.
Utilisez l’option `--dummy` pour générer une vidéo factice avec un texte de test et un son silencieux.

Exemple : `python -m core.run_pipeline --theme "test rapide" --dummy`

Ce mode vous permet de vérifier l’assemblage vidéo sans configuration préalable.

## Notes publication

- **TikTok** : utiliser la Content Posting API (Direct Post ou Upload + Draft).
- **YouTube Shorts** : utiliser `videos.insert` (quota 1600/vidéo).
- **Instagram Reels** : via Instagram Graph API (upload + publish).

Tu peux déclencher le pipeline 3×/jour (cron) ou via des **Tasks** de ChatGPT Agent.

  
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
 `config/themes_historique.json` : anti-doublon

18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43

- 
## Mode Dummy

Ce projet inclut un mode de test qui ne consomme aucune clé API.
Utilisez l’option `--dummy` pour générer une vidéo factice avec un texte de test et un son silencieux.

Exemple : `python -m core.run_pipeline --theme "test rapide" --dummy`

Ce mode vous permet de vérifier l’assemblage vidéo sans configuration préalable.

## Notes publication

- **TikTok** : utiliser la Content Posting API (Direct Post ou Upload + Draft).
- **YouTube Shorts** : utiliser `videos.insert` (quota 1600/vidéo).
- **Instagram Reels** : via Instagram Graph API (upload + publish).

Tu peux déclencher le pipeline 3×/jour (cron) ou via des **Tasks** de ChatGPT Agent.
