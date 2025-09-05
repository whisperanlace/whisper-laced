import React from "react";

const PromptInput = ({ prompt, setPrompt }) => {
  return (
    <textarea
      value={prompt}
      onChange={(e) => setPrompt(e.target.value)}
      placeholder="Enter your prompt..."
      className="w-full p-3 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-gold resize-none"
      rows={4}
    />
  );
};

export default PromptInput;
