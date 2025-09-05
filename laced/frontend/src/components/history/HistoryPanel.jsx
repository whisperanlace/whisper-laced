import React from "react";
import { useHistory } from "../../hooks/useHistory";
import HistoryThumbnail from "./HistoryThumbnail";

const HistoryPanel = () => {
  const { history, clearHistory } = useHistory();

  if (!history.length) return <p className="text-gray-500">No history yet.</p>;

  return (
    <div className="p-2 space-y-2">
      <div className="flex justify-between items-center">
        <h2 className="text-sm font-playfair text-wine-red">History</h2>
        <button
          onClick={clearHistory}
          className="text-xs text-gold hover:underline"
        >
          Clear All
        </button>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2">
        {history.map((item, idx) => (
          <HistoryThumbnail key={idx} item={item} />
        ))}
      </div>
    </div>
  );
};

export default HistoryPanel;
