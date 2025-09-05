import React from "react";
import { useAppContext } from "../../context/AppContext";
import { downloadImage } from "../../utils/download";

const OutputGrid = () => {
  const { history } = useAppContext();

  if (!history.length) return <p>No generated images yet.</p>;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mt-4">
      {history.map((item, idx) => (
        <div key={idx} className="border rounded p-2">
          <img src={item.result.url} alt={item.prompt} className="w-full h-auto rounded" />
          <p className="text-xs mt-1">{item.prompt}</p>
          <button
            onClick={() => downloadImage(item.result.url)}
            className="mt-1 px-2 py-1 bg-gold text-wine-red rounded text-xs"
          >
            Download
          </button>
        </div>
      ))}
    </div>
  );
};

export default OutputGrid;
