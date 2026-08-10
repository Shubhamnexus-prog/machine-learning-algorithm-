# Lingua — React + Django Translator

A multilingual translator with a custom "atlas & ink" UI: React (Vite) frontend
talking to a Django REST Framework backend.

```
translator-django-react/
├── backend/     Django REST API (translate, detect, speak, upload)
└── frontend/    React (Vite) single-page app
```

## Requirements
- Python 3.12
- Node.js 18+ (for the frontend)

## 1. Backend setup (Django)

```bash
cd backend
python -m venv venv

# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs at **http://127.0.0.1:8000**. Endpoints live under `/api/`:
- `GET  /api/languages/` — list of supported languages
- `POST /api/detect/` — detect the language of a text
- `POST /api/translate/` — translate text
- `POST /api/speak/` — generate TTS audio (gTTS)
- `POST /api/upload/` — read text from an uploaded .txt/.md/.csv file

## 2. Frontend setup (React)

Open a **second terminal**:

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at **http://localhost:5173** and proxies `/api` and `/media`
calls to the Django server automatically (configured in `vite.config.js`).

Open **http://localhost:5173** in your browser — keep both terminals running.

## Features
- 57 languages (Google Translate via `deep-translator`)
- Auto language detection (`langdetect`) with a detected-language badge
- Voice input — browser Speech-to-Text (best in Chrome/Edge)
- Voice output — gTTS, with a slow-audio toggle
- File upload translate (.txt, .md, .csv)
- Translation history, saved in the browser, click to reload any entry
- Dark / light theme toggle
- Copy, swap, clear

## Notes
- Translation and TTS require an internet connection (they call Google Translate under the hood).
- For production, build the frontend with `npm run build` and serve the
  `frontend/dist` folder from Django or a static host, and set `DEBUG = False`
  plus a real `SECRET_KEY` and `ALLOWED_HOSTS` in `backend/translator_project/settings.py`.
