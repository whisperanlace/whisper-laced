import React, { createContext, useState, useContext } from "react";

// Create App context
const AppContext = createContext();

export const AppContextProvider = ({ children }) => {
  // Global app state
  const [model, setModel] = useState(null);
  const [size, setSize] = useState("512x768");
  const [style, setStyle] = useState("default");
  const [nsfw, setNSFW] = useState(false);
  const [feet, setFeet] = useState(false);
  const [mirror, setMirror] = useState(false);
  const [history, setHistory] = useState([]);

  const addToHistory = (item) => {
    setHistory(prev => [item, ...prev]);
  };

  return (
    <AppContext.Provider value={{
      model,
      setModel,
      size,
      setSize,
      style,
      setStyle,
      nsfw,
      setNSFW,
      feet,
      setFeet,
      mirror,
      setMirror,
      history,
      addToHistory
    }}>
      {children}
    </AppContext.Provider>
  );
};

// Hook for easy access
export const useAppContext = () => useContext(AppContext);
