import React from "react";
import { downloadImage } from "../../utils/download";

const HistoryDownloadButton = ({ url }) => {
  return (
    <button
      onClick={() => downloadImage(url)}
      className="mt-1 px-2 py-1 bg-gold text-wine-red rounded text-xs w-full hover:shadow-md transition"
    >
      Download
    </button>
  );
};

export default HistoryDownloadButton;
