import React from "react";
import { useAppContext } from "../../context/AppContext";
import { useModels } from "../../hooks/useModels";

const ModelSelect = () => {
  const { model, setModel } = useAppContext();
  const { models, loading } = useModels();

  if (loading) return <p>Loading models...</p>;

  return (
    <select
      value={model || ""}
      onChange={(e) => setModel(e.target.value)}
      className="border rounded p-1"
    >
      <option value="" disabled>Select Model</option>
      {models.map(m => (
        <option key={m.id} value={m.name}>{m.name}</option>
      ))}
    </select>
  );
};

export default ModelSelect;
