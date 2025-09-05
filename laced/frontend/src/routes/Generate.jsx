import React, { useState } from "react";
import PromptInput from "../components/generate/PromptInput";
import GenerateButton from "../components/generate/GenerateButton";
import SizeToggle from "../components/generate/SizeToggle";
import ModelSelect from "../components/generate/ModelSelect";
import StyleToggle from "../components/generate/StyleToggle";
import NSFWToggle from "../components/generate/NSFWToggle";
import FeetToggle from "../components/generate/FeetToggle";
import MirrorToggle from "../components/generate/MirrorToggle";
import OutputGrid from "../components/generate/OutputGrid";
import { useGenerate } from "../hooks/useGenerate";

const Generate = () => {
  const [prompt, setPrompt] = useState("");
  const { generate, loading } = useGenerate();

  const handleGenerate = () => {
    generate(prompt);
  };

  return (
    <div className="p-4 space-y-4">
      <PromptInput prompt={prompt} setPrompt={setPrompt} />
      <div className="flex flex-wrap gap-2">
        <SizeToggle />
        <ModelSelect />
        <StyleToggle />
        <NSFWToggle />
        <FeetToggle />
        <MirrorToggle />
      </div>
      <GenerateButton onClick={handleGenerate} loading={loading} />
      <OutputGrid />
    </div>
  );
};

export default Generate;
