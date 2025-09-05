import React from "react";
import { useWhisper } from "../../hooks/useWhisper";

const WhisperPanel = () => {
  const { prompt, updatePrompt, sendPrompt, output, loading } = useWhisper();

  const handleSend = async () => {
    try {
      await sendPrompt();
    } catch (err) {
      console.error("Whisper send error", err);
    }
  };

  return (
    <div className="bg-ivory rounded p-4 w-96 max-w-full shadow-lg flex flex-col space-y-2">
      <h2 className="text-wine-red font-playfair text-lg">Whisper</h2>
      <textarea
        value={prompt}
        onChange={(e) => updatePrompt(e.target.value)}
        placeholder="Enter your Whisper prompt..."
        className="w-full p-2 border rounded resize-none focus:ring-2 focus:ring-gold"
        rows={3}
      />
      <button
        onClick={handleSend}
        disabled={loading}
        className="bg-gold text-wine-red px-3 py-1 rounded hover:shadow-md transition"
      >
        {loading ? "Processing..." : "Send"}
      </button>
      {output && <div className="mt-2 p-2 border rounded bg-gray-100 text-sm">{output}</div>}
    </div>
  );
};

export default WhisperPanel;
