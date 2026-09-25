const BASE = "/api";

async function handle(res) {
  const data = await res.json();
  return data;
}

export async function fetchLanguages() {
  const res = await fetch(`${BASE}/languages/`);
  return handle(res);
}

export async function translateText(text, source, target) {
  const res = await fetch(`${BASE}/translate/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text, source, target }),
  });
  return handle(res);
}

export async function detectLanguage(text) {
  const res = await fetch(`${BASE}/detect/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  return handle(res);
}

export async function speakText(text, lang, slow) {
  const res = await fetch(`${BASE}/speak/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text, lang, slow }),
  });
  return handle(res);
}

export async function uploadFile(file) {
  const formData = new FormData();
  formData.append("file", file);
  const res = await fetch(`${BASE}/upload/`, {
    method: "POST",
    body: formData,
  });
  return handle(res);
}
