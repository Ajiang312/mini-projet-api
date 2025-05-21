
# 🚀 Mini-Projet API – FastAPI + GCP + IA

Ce projet consiste à développer une API Python en *FastAPI, contenant des endpoints simples, connectée à **Google Cloud Storage* pour lire/écrire un fichier de données, et utilisant *Vertex AI* pour générer des blagues automatiquement.
HEAD
- Lecture et écriture de données sur **Google Cloud Storage**
- Génération de blagues aléatoires via **Vertex AI (Gemini)**
- API exposée publiquement via des endpoints simples
=======
Le tout est containerisé avec Docker et déployé via *Cloud Run* sur *Google Cloud Platform*.

---

## 🌐 Endpoints de l’API

| Méthode | Endpoint   | Description |
|---------|------------|-------------|
| GET     | ⁠ /hello ⁠   | Message de bienvenue |
| GET     | ⁠ /status ⁠  | Date/heure serveur |
| GET     | ⁠ /data ⁠    | Retourne le fichier JSON stocké sur GCS |
| POST    | ⁠ /data ⁠    | Ajoute une ligne à ce fichier JSON |
| GET     | ⁠ /joke ⁠    | Renvoie une blague générée par Vertex AI |

---

## 📦 Stack technique

•⁠  ⁠*FastAPI*
•⁠  ⁠*Docker*
•⁠  ⁠*Google Cloud Run*
•⁠  ⁠*Google Cloud Storage*
•⁠  ⁠*Vertex AI (⁠ text-bison ⁠)*

---

## 🧑‍🤝‍🧑 Rôles des membres

| Membre     | Rôle |
|------------|------|
| *Antoine* | Structure du projet, Dockerfile, ⁠ .env ⁠, GitHub, nettoyage |
| *Roman*   | Développement de l’API FastAPI, intégration GCS, déploiement GCP |
| *Baptiste*| Génération IA avec Vertex AI, création ⁠ joke_utils.py ⁠, test ⁠ /joke ⁠ |

---

## ▶️ Exécution locale

### 1. Installer les dépendances
```bash
pip install -r requirements.txt

