import React from "react";
import { useAppContext } from "../../context/AppContext";
import { useWhisperContext } from "../../context/WhisperContext";

const Topbar = () => {
  const { model } = useAppContext();
  const { isOpen, openPanel } = useWhisperContext();

  return (
    <header className="h-16 bg-ivory flex items-center justify-between px-4 shadow-sm">
      <div className="flex items-center space-x-4">
        <h1 className="text-xl font-playfair text-wine-red">Laced AI</h1>
        {model && <span className="text-sm text-gray-700">Model: {model}</span>}
      </div>
      <button
        className="bg-gold text-wine-red px-3 py-1 rounded hover:shadow-md transition"
        onClick={openPanel}
      >
        {isOpen ? "Whisper Open" : "Open Whisper"}
      </button>
    </header>
  );
};

export default Topbar;
