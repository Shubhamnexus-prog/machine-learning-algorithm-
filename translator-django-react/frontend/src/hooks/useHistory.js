import { useCallback, useEffect, useState } from "react";

const HISTORY_KEY = "lingua_translation_history";
const MAX_HISTORY = 20;

export function useHistory() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    try {
      const saved = JSON.parse(localStorage.getItem(HISTORY_KEY)) || [];
      setHistory(saved);
    } catch {
      setHistory([]);
    }
  }, []);

  const addEntry = useCallback((entry) => {
    setHistory((prev) => {
      const next = [
        { ...entry, time: new Date().toLocaleString("en-IN", { hour: "2-digit", minute: "2-digit", day: "2-digit", month: "short" }) },
        ...prev,
      ].slice(0, MAX_HISTORY);
      localStorage.setItem(HISTORY_KEY, JSON.stringify(next));
      return next;
    });
  }, []);

  const clearHistory = useCallback(() => {
    localStorage.removeItem(HISTORY_KEY);
    setHistory([]);
  }, []);

  return { history, addEntry, clearHistory };
}
