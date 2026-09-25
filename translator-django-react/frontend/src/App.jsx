import { useEffect, useMemo, useRef, useState } from "react";
import { detectLanguage, fetchLanguages, speakText, translateText, uploadFile } from "./api.js";
import { SPEECH_LANG_MAP } from "./constants.js";
import HistoryPanel from "./components/HistoryPanel.jsx";
import ThemeToggle from "./components/ThemeToggle.jsx";
import { useHistory } from "./hooks/useHistory.js";
import { useSpeechRecognition } from "./hooks/useSpeechRecognition.js";
import "./App.css";

const THEME_KEY = "lingua_theme";

export default function App() {
  const [languages, setLanguages] = useState({});
  const [ttsSupported, setTtsSupported] = useState([]);
  const [sourceLang, setSourceLang] = useState("auto");
  const [targetLang, setTargetLang] = useState("hi");
  const [sourceText, setSourceText] = useState("");
  const [targetText, setTargetText] = useState("");
  const [detected, setDetected] = useState(null);
  const [slow, setSlow] = useState(false);
  const [status, setStatus] = useState("");
  const [isTranslating, setIsTranslating] = useState(false);
  const [isLight, setIsLight] = useState(false);

  const { history, addEntry, clearHistory } = useHistory();
  const debounceRef = useRef(null);
  const detectDebounceRef = useRef(null);
  const audioRef = useRef(null);
  const fileInputRef = useRef(null);

  // ---------- Load languages from Django API ----------
  useEffect(() => {
    fetchLanguages().then((data) => {
      setLanguages(data.languages || {});
      setTtsSupported(data.tts_supported || []);
    });
  }, []);

  // ---------- Theme ----------
  useEffect(() => {
    const saved = localStorage.getItem(THEME_KEY);
    const prefersLight = window.matchMedia?.("(prefers-color-scheme: light)").matches;
    const light = saved ? saved === "light" : Boolean(prefersLight && false);
    setIsLight(light);
    document.body.classList.toggle("light-mode", light);
  }, []);

  function toggleTheme() {
    setIsLight((prev) => {
      const next = !prev;
      document.body.classList.toggle("light-mode", next);
      localStorage.setItem(THEME_KEY, next ? "light" : "dark");
      return next;
    });
  }

  // ---------- Translate (debounced on typing) ----------
  async function runTranslate(text = sourceText) {
    if (!text.trim()) {
      setStatus("Type something to translate.");
      return;
    }
    setIsTranslating(true);
    setStatus("Translating…");
    const data = await translateText(text.trim(), sourceLang, targetLang);
    setIsTranslating(false);
    if (data.success) {
      setTargetText(data.translated_text);
      setStatus("");
      addEntry({ source: text.trim(), target: data.translated_text, srcLang: sourceLang, tgtLang: targetLang });
    } else {
      setStatus(data.error || "Something went wrong.");
    }
  }

  function handleSourceChange(e) {
    const value = e.target.value;
    setSourceText(value);

    clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(() => {
      if (value.trim()) runTranslate(value);
    }, 700);

    clearTimeout(detectDebounceRef.current);
    if (sourceLang === "auto" && value.trim().length > 2) {
      detectDebounceRef.current = setTimeout(async () => {
        const data = await detectLanguage(value.trim());
        if (data.success) setDetected(data.name);
        else setDetected(null);
      }, 500);
    } else {
      setDetected(null);
    }
  }

  function handleSwap() {
    if (sourceLang === "auto") {
      setStatus("Can't swap while source is Auto Detect.");
      return;
    }
    setSourceLang(targetLang);
    setTargetLang(sourceLang);
    setSourceText(targetText);
    setTargetText(sourceText);
  }

  function handleClear() {
    setSourceText("");
    setTargetText("");
    setStatus("");
    setDetected(null);
  }

  async function handleCopy() {
    if (!targetText) return;
    await navigator.clipboard.writeText(targetText);
    setStatus("Copied.");
    setTimeout(() => setStatus(""), 1400);
  }

  async function handleSpeak(text, lang) {
    if (!text.trim()) return;
    setStatus("Preparing audio…");
    const data = await speakText(text, lang === "auto" ? "en" : lang, slow);
    if (data.success) {
      audioRef.current.src = data.audio_url;
      audioRef.current.play();
      setStatus("");
    } else {
      setStatus(data.error || "Audio failed.");
    }
  }

  async function handleFileUpload(e) {
    const file = e.target.files[0];
    if (!file) return;
    setStatus("Reading file…");
    const data = await uploadFile(file);
    if (data.success) {
      setSourceText(data.text);
      runTranslate(data.text);
    } else {
      setStatus(data.error || "Could not read file.");
    }
    e.target.value = "";
  }

  function handleHistorySelect(item) {
    setSourceLang(item.srcLang);
    setTargetLang(item.tgtLang);
    setSourceText(item.source);
    setTargetText(item.target);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  // ---------- Voice input ----------
  const { supported: micSupported, isRecording, start, stop } = useSpeechRecognition({
    onResult: (transcript) => {
      const merged = sourceText ? `${sourceText} ${transcript}` : transcript;
      setSourceText(merged);
      runTranslate(merged);
    },
    onError: (err) => setStatus(`Voice input error: ${err}`),
  });

  function handleMicClick() {
    if (!micSupported) {
      setStatus("Voice input isn't supported in this browser.");
      return;
    }
    if (isRecording) {
      stop();
      return;
    }
    const code = sourceLang === "auto" ? "en" : sourceLang;
    start(SPEECH_LANG_MAP[code] || "en-US");
    setStatus("Listening…");
  }

  const languageEntries = useMemo(() => Object.entries(languages), [languages]);
  const targetEntries = useMemo(() => languageEntries.filter(([code]) => code !== "auto"), [languageEntries]);

  return (
    <div className="app-shell">
      <header className="masthead">
        <div className="masthead-mark">
          <span className="mark-glyph">文A</span>
        </div>
        <div className="masthead-titles">
          <span className="eyebrow">Vol. I — Multilingual Edition</span>
          <h1>Lingua</h1>
        </div>
        <ThemeToggle isLight={isLight} onToggle={toggleTheme} />
      </header>

      <main className="translator-frame">
        <div className="lang-bar">
          <div className="lang-field">
            <label>From</label>
            <select value={sourceLang} onChange={(e) => { setSourceLang(e.target.value); setDetected(null); }}>
              {languageEntries.map(([code, name]) => (
                <option key={code} value={code}>
                  {name}
                </option>
              ))}
            </select>
            {detected && <span className="detected-tag">Detected: {detected}</span>}
          </div>

          <button className="swap-btn" onClick={handleSwap} title="Swap languages" aria-label="Swap languages">
            ⇄
          </button>

          <div className="lang-field">
            <label>To</label>
            <select value={targetLang} onChange={(e) => setTargetLang(e.target.value)}>
              {targetEntries.map(([code, name]) => (
                <option key={code} value={code}>
                  {name}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className="pages">
          <div className="page">
            <textarea
              value={sourceText}
              onChange={handleSourceChange}
              placeholder="Write, paste, or speak text here…"
              maxLength={4000}
            />
            <div className="page-footer">
              <span className="char-count">{sourceText.length} / 4000</span>
              <div className="page-actions">
                <button className="icon-btn" title="Upload a text file" onClick={() => fileInputRef.current?.click()}>
                  ⤴
                </button>
                <input ref={fileInputRef} type="file" hidden accept=".txt,.md,.csv" onChange={handleFileUpload} />
                <button
                  className={`icon-btn ${isRecording ? "is-recording" : ""}`}
                  title="Voice input"
                  onClick={handleMicClick}
                >
                  ●
                </button>
                <button className="icon-btn" title="Listen" onClick={() => handleSpeak(sourceText, sourceLang)}>
                  ♪
                </button>
                <button className="icon-btn" title="Clear" onClick={handleClear}>
                  ✕
                </button>
              </div>
            </div>
          </div>

          <div className="spine" aria-hidden="true">
            <span className="spine-line" />
          </div>

          <div className="page page-output">
            <textarea value={targetText} readOnly placeholder="Your translation appears here…" />
            <div className="page-footer">
              <span className="status-text">{status}</span>
              <div className="page-actions">
                <button className="icon-btn" title="Listen" onClick={() => handleSpeak(targetText, targetLang)}>
                  ♪
                </button>
                <button className="icon-btn" title="Copy" onClick={handleCopy}>
                  ⧉
                </button>
              </div>
            </div>
          </div>
        </div>

        <div className="controls-row">
          <label className="slow-toggle">
            <input type="checkbox" checked={slow} onChange={(e) => setSlow(e.target.checked)} />
            Slow audio
          </label>
          <button className="translate-btn" disabled={isTranslating} onClick={() => runTranslate()}>
            {isTranslating ? "Translating…" : "Translate"}
          </button>
        </div>
      </main>

      <div className="translator-frame">
        <HistoryPanel history={history} onSelect={handleHistorySelect} onClear={clearHistory} />
      </div>

      <footer className="app-footer">
        <span>React · Django REST · Google Translate · gTTS</span>
      </footer>

      <audio ref={audioRef} hidden />
    </div>
  );
}
