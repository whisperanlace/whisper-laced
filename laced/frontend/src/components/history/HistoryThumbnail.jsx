import React from "react";
import HistoryDownloadButton from "./HistoryDownloadButton";

const HistoryThumbnail = ({ item }) => {
  return (
    <div className="border rounded p-1">
      <img src={item.result.url} alt={item.prompt} className="w-full h-24 object-cover rounded" />
      <p className="text-xs mt-1 truncate">{item.prompt}</p>
      <HistoryDownloadButton url={item.result.url} />
    </div>
  );
};

export default HistoryThumbnail;
