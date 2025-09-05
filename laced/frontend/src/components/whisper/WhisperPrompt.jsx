import React from "react";
import { useWhisperContext } from "../../context/WhisperContext";

const WhisperPrompt = () => {
  const { prompt, updatePrompt } = useWhisperContext();

  return (
    <input
      type="text"
      value={prompt}
      onChange={(e) => updatePrompt(e.target.value)}
      placeholder="Whisper prompt..."
      className="border rounded p-2 w-full focus:ring-2 focus:ring-gold"
    />
  );
};

export default WhisperPrompt;
