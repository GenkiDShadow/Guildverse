# GuildVerse — V1

Application Android de guilde virtuelle créée avec Python + Kivy.

## Ce que contient cette V1
- Accueil de la guilde
- Chat général local (simulation)
- Liste des membres
- Rangs et XP
- Activités / défis
- Profil

## Lancer sur PC

```bash
pip install -r requirements.txt
python main.py
```

## Important
Le chat de cette V1 est volontairement local : les messages ne sont pas encore envoyés sur Internet.
La prochaine étape sera d'ajouter un serveur Python (FastAPI + WebSocket) pour permettre à plusieurs téléphones de discuter réellement.

## Android
Quand la version PC fonctionne, on pourra générer un APK avec Buildozer depuis Linux/WSL.
