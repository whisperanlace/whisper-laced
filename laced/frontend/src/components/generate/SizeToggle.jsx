import React from "react";
import { useAppContext } from "../../context/AppContext";

const SizeToggle = () => {
  const { size, setSize } = useAppContext();
  const options = ["512x768", "768x512", "768x768", "720x1080", "1080x720"];

  return (
    <div className="flex space-x-2">
      {options.map(opt => (
        <button
          key={opt}
          className={`px-2 py-1 rounded border ${size === opt ? "bg-gold text-wine-red" : "bg-ivory text-gray-700"}`}
          onClick={() => setSize(opt)}
        >
          {opt}
        </button>
      ))}
    </div>
  );
};

export default SizeToggle;
