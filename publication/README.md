# Publication APIs

Ce document dresse la liste des tâches à réaliser pour intégrer les APIs de publication sur les différentes plateformes (TikTok, YouTube Shorts, Instagram Reels).

## TikTok Content Posting API

- [ ] Créer une application TikTok et obtenir un **client_key**, **client_secret** et **redirect_uri**.
- [ ] Mettre en place le flux OAuth pour récupérer un **access_token** avec les scopes *video.upload* et *video.publish*.
- [ ] Implémenter l’appel `POST /open-api/v2/video/init/` pour initialiser l’upload (obtenir `upload_url` et `video_id`).
- [ ] Envoyer la vidéo vers `upload_url` via requête HTTP PUT.
- [ ] Finaliser l’upload avec `POST /open-api/v2/video/commit/` pour publier ou sauver en brouillon.
- [ ] Gérer les erreurs et récupérer l’état avec `GET /open-api/v2/video/query/`.
- **Documentation** : [TikTok Content Posting API Overview](https://developers.tiktok.com/doc/content-posting-api-overview/).

## YouTube Shorts (YouTube Data API)

- [ ] Créer un projet Google Cloud et activer l’API YouTube Data.
- [ ] Obtenir les identifiants OAuth2 (**client_id**, **client_secret**) et un **refresh_token**.
- [ ] Utiliser l’endpoint `videos.insert` avec le paramètre `uploadType=resumable` pour uploader la vidéo.
- [ ] Renseigner `snippet.title`, `snippet.description`, `snippet.tags` et `snippet.categoryId` (24 pour Shorts).
- [ ] Définir `status.privacyStatus` (private, unlisted ou public).
- **Documentation** : [YouTube Data API: Uploading Videos](https://developers.google.com/youtube/v3/docs/videos/insert).

## Instagram Reels (Graph API)

- [ ] Avoir une **Page Facebook** et un **compte Instagram Professionnel** relié à cette page.
- [ ] Créer une application Meta et obtenir **app_id**, **app_secret** et un **user access token** longue durée.
- [ ] Utiliser `POST /{ig-user-id}/media` pour téléverser la vidéo en mode ébauche (champ `media_type=REELS`).
- [ ] Appeler `POST /{ig-user-id}/media_publish` avec l’ID de la média pour publier le Reel.
- **Documentation** : [Instagram Graph API: Publishing Reels](https://developers.facebook.com/docs/instagram-api/guides/content-publishing/).
