import { useAppContext } from "../context/AppContext";

export const useHistory = () => {
  const { history, addToHistory } = useAppContext();

  const clearHistory = () => {
    if (window.confirm("Clear all history?")) {
      addToHistory([]); // reset history
    }
  };

  return { history, addToHistory, clearHistory };
};
