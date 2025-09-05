import { useState } from "react";
import { sendWhisperPrompt } from "../api/whisper";
import { useWhisperContext } from "../context/WhisperContext";

export const useWhisper = () => {
  const { prompt, updatePrompt, setWhisperOutput } = useWhisperContext();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendPrompt = async () => {
    if (!prompt) return;
    setLoading(true);
    setError(null);

    try {
      const output = await sendWhisperPrompt(prompt);
      setWhisperOutput(output);
      setLoading(false);
      return output;
    } catch (err) {
      setError(err);
      setLoading(false);
      throw err;
    }
  };

  return { prompt, updatePrompt, sendPrompt, loading, error };
};
