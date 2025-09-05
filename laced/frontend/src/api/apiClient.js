import axios from "axios";

const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:5000/api";

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

apiClient.interceptors.response.use(
  response => response.data,
  error => {
    console.error("API Error:", error.response || error.message);
    return Promise.reject(error.response?.data || error.message);
  }
);

export default apiClient;
