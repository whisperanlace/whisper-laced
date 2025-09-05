import apiClient from "./apiClient";

export const getLoRAs = async () => {
  try {
    const response = await apiClient.get("/lora");
    return response.loras || [];
  } catch (error) {
    console.error("LoRA fetch error:", error);
    throw error;
  }
};

export const applyLoRA = async (loraId) => {
  try {
    const response = await apiClient.post("/lora/apply", { loraId });
    return response;
  } catch (error) {
    console.error("Apply LoRA error:", error);
    throw error;
  }
};
