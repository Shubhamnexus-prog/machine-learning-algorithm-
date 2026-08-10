export default function ThemeToggle({ isLight, onToggle }) {
  return (
    <button className="theme-toggle" onClick={onToggle} title="Toggle theme" aria-label="Toggle light/dark theme">
      <span className="theme-toggle-track">
        <span className={`theme-toggle-thumb ${isLight ? "is-light" : ""}`}>{isLight ? "☀" : "☾"}</span>
      </span>
    </button>
  );
}
