export default function HistoryPanel({ history, onSelect, onClear }) {
  return (
    <section className="history-panel">
      <div className="history-panel-head">
        <h2>
          <span className="eyebrow">Archive</span>
          Recent translations
        </h2>
        {history.length > 0 && (
          <button className="text-btn" onClick={onClear}>
            Clear all
          </button>
        )}
      </div>

      {history.length === 0 ? (
        <p className="history-empty">Nothing translated yet — your entries will be catalogued here.</p>
      ) : (
        <ul className="history-list">
          {history.map((item, i) => (
            <li key={i} className="history-item" onClick={() => onSelect(item)}>
              <span className="history-meta">
                {item.srcLang.toUpperCase()} → {item.tgtLang.toUpperCase()} · {item.time}
              </span>
              <span className="history-source">{item.source}</span>
              <span className="history-target">{item.target}</span>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
