import apiClient from "./apiClient";

export const sendWhisperPrompt = async (prompt) => {
  try {
    const response = await apiClient.post("/whisper", { prompt });
    return response.output || "";
  } catch (error) {
    console.error("Whisper error:", error);
    throw error;
  }
};
