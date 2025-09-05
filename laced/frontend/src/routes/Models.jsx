import React, { useState } from "react";
import ModelList from "../components/models/ModelList";
import LoRASelector from "../components/models/LoRASelector";
import { useModels } from "../hooks/useModels";

const Models = () => {
  const { models } = useModels();
  const [selectedModel, setSelectedModel] = useState(null);

  return (
    <div className="p-4 space-y-4">
      <h2 className="text-xl font-playfair text-wine-red">Models</h2>
      <LoRASelector onApply={() => console.log("LoRA applied")} />
      <ModelList models={models} onSelect={setSelectedModel} />
      {selectedModel && <p className="text-gray-700">Selected model: {selectedModel.name}</p>}
    </div>
  );
};

export default Models;
