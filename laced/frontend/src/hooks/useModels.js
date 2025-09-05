import { useState, useEffect } from "react";
import { getModels } from "../api/models";

export const useModels = () => {
  const [models, setModels] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchModels = async () => {
    setLoading(true);
    try {
      const data = await getModels();
      setModels(data);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchModels();
  }, []);

  return { models, loading, error, fetchModels };
};
