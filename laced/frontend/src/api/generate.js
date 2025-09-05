import apiClient from "./apiClient";

export const generateImage = async (prompt, options) => {
  // options: { model, size, style, nsfw, feet, mirror }
  try {
    const response = await apiClient.post("/generate", {
      prompt,
      ...options,
    });
    return response;
  } catch (error) {
    console.error("Generate error:", error);
    throw error;
  }
};
