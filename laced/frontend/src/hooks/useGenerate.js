import { useState } from "react";
import { generateImage } from "../api/generate";
import { useAppContext } from "../context/AppContext";

export const useGenerate = () => {
  const { model, size, style, nsfw, feet, mirror, addToHistory } = useAppContext();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const generate = async (prompt) => {
    setLoading(true);
    setError(null);

    try {
      const options = { model, size, style, nsfw, feet, mirror };
      const result = await generateImage(prompt, options);
      addToHistory({ prompt, result, date: new Date() });
      setLoading(false);
      return result;
    } catch (err) {
      setError(err);
      setLoading(false);
      throw err;
    }
  };

  return { generate, loading, error };
};
