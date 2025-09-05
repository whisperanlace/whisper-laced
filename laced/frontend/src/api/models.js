import apiClient from "./apiClient";

export const getModels = async () => {
  try {
    const response = await apiClient.get("/models");
    return response.models || [];
  } catch (error) {
    console.error("Models fetch error:", error);
    throw error;
  }
};
