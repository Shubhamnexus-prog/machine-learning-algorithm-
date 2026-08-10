import os
import uuid

from deep_translator import GoogleTranslator
from django.conf import settings
from gtts import gTTS
from langdetect import DetectorFactory, LangDetectException, detect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .languages import DETECT_CODE_MAP, LANGUAGES, TTS_CODE_FIX, TTS_SUPPORTED

DetectorFactory.seed = 0  # consistent detection results

AUDIO_DIR = os.path.join(settings.MEDIA_ROOT, "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)


@api_view(["GET"])
def languages_view(request):
    """Return the full list of supported languages and which ones have TTS."""
    return Response(
        {
            "languages": LANGUAGES,
            "tts_supported": sorted(TTS_SUPPORTED),
        }
    )


@api_view(["POST"])
def detect_view(request):
    text = (request.data.get("text") or "").strip()

    if not text:
        return Response({"success": False, "error": "Text khaali hai."}, status=400)

    try:
        code = detect(text)
        code = DETECT_CODE_MAP.get(code, code)
        name = LANGUAGES.get(code, code.upper())
        return Response({"success": True, "code": code, "name": name})
    except LangDetectException:
        return Response({"success": False, "error": "Language detect nahi ho payi."}, status=400)


@api_view(["POST"])
def translate_view(request):
    text = (request.data.get("text") or "").strip()
    source = request.data.get("source", "auto")
    target = request.data.get("target", "en")

    if not text:
        return Response({"success": False, "error": "Kripya kuch text likhein."}, status=400)

    if target not in LANGUAGES or target == "auto":
        return Response({"success": False, "error": "Sahi target language chunein."}, status=400)

    try:
        translator = GoogleTranslator(source=source, target=target)
        result = translator.translate(text)
        return Response({"success": True, "translated_text": result})
    except Exception as e:
        return Response({"success": False, "error": f"Translation fail hua: {str(e)}"}, status=500)


@api_view(["POST"])
def speak_view(request):
    text = (request.data.get("text") or "").strip()
    lang = request.data.get("lang", "en")
    slow = bool(request.data.get("slow", False))

    if not text:
        return Response({"success": False, "error": "Text khaali hai."}, status=400)

    if lang not in TTS_SUPPORTED:
        return Response(
            {"success": False, "error": "Is language ke liye audio available nahi hai."}, status=400
        )

    try:
        filename = f"{uuid.uuid4().hex}.mp3"
        filepath = os.path.join(AUDIO_DIR, filename)
        tts = gTTS(text=text, lang=TTS_CODE_FIX.get(lang, lang), slow=slow)
        tts.save(filepath)
        return Response({"success": True, "audio_url": f"{settings.MEDIA_URL}audio/{filename}"})
    except Exception as e:
        return Response({"success": False, "error": f"Audio banane mein error: {str(e)}"}, status=500)


@api_view(["POST"])
def upload_view(request):
    file = request.FILES.get("file")
    if not file:
        return Response({"success": False, "error": "Koi file nahi mili."}, status=400)

    allowed_ext = (".txt", ".md", ".csv")
    if not file.name.lower().endswith(allowed_ext):
        return Response(
            {"success": False, "error": "Sirf .txt, .md ya .csv file allowed hai."}, status=400
        )

    try:
        raw = file.read()
        text = raw.decode("utf-8", errors="ignore")
        text = text[:4000]
        return Response({"success": True, "text": text})
    except Exception as e:
        return Response({"success": False, "error": f"File read karne mein error: {str(e)}"}, status=500)
