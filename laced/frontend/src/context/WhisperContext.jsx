import React, { createContext, useState, useContext } from "react";

// Whisper panel context
const WhisperContext = createContext();

export const WhisperContextProvider = ({ children }) => {
  const [isOpen, setIsOpen] = useState(false);  // Show/hide panel
  const [prompt, setPrompt] = useState("");     // Current whisper prompt
  const [output, setOutput] = useState("");     // Response from Whisper

  const openPanel = () => setIsOpen(true);
  const closePanel = () => setIsOpen(false);
  const updatePrompt = (text) => setPrompt(text);
  const setWhisperOutput = (text) => setOutput(text);

  return (
    <WhisperContext.Provider value={{
      isOpen,
      openPanel,
      closePanel,
      prompt,
      updatePrompt,
      output,
      setWhisperOutput
    }}>
      {children}
    </WhisperContext.Provider>
  );
};

// Hook for easy access
export const useWhisperContext = () => useContext(WhisperContext);
