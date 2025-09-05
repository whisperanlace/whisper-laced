import React from "react";
import ModelPreviewCard from "./ModelPreviewCard";

const ModelList = ({ models, onSelect }) => {
  if (!models || !models.length) return <p>No models available</p>;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      {models.map(model => (
        <ModelPreviewCard key={model.id} model={model} onSelect={onSelect} />
      ))}
    </div>
  );
};

export default ModelList;
