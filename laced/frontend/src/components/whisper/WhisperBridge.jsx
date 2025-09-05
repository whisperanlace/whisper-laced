import React from "react";
import WhisperPanel from "./WhisperPanel";
import { useWhisperContext } from "../../context/WhisperContext";

const WhisperBridge = () => {
  const { isOpen } = useWhisperContext();

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <WhisperPanel />
    </div>
  );
};

export default WhisperBridge;
