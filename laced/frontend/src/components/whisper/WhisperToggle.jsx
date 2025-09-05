import React from "react";
import { useWhisperContext } from "../../context/WhisperContext";

const WhisperToggle = () => {
  const { isOpen, openPanel, closePanel } = useWhisperContext();

  return (
    <button
      onClick={isOpen ? closePanel : openPanel}
      className="bg-gold text-wine-red px-3 py-1 rounded hover:shadow-md transition"
    >
      {isOpen ? "Close Whisper" : "Open Whisper"}
    </button>
  );
};

export default WhisperToggle;
