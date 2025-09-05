import React from "react";

const ModelPreviewCard = ({ model, onSelect }) => {
  return (
    <div className="border rounded p-2 hover:shadow-lg transition cursor-pointer" onClick={() => onSelect(model)}>
      <img src={model.previewUrl} alt={model.name} className="w-full h-32 object-cover rounded" />
      <h3 className="text-sm font-playfair mt-2 text-wine-red">{model.name}</h3>
      <p className="text-xs text-gray-600">{model.description}</p>
    </div>
  );
};

export default ModelPreviewCard;
