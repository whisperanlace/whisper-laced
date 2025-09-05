import React from "react";
import { useAppContext } from "../../context/AppContext";

const StyleToggle = () => {
  const { style, setStyle } = useAppContext();
  const styles = ["default", "photorealistic", "cinematic", "anime"];

  return (
    <div className="flex space-x-2">
      {styles.map(s => (
        <button
          key={s}
          className={`px-2 py-1 rounded border ${style === s ? "bg-gold text-wine-red" : "bg-ivory text-gray-700"}`}
          onClick={() => setStyle(s)}
        >
          {s}
        </button>
      ))}
    </div>
  );
};

export default StyleToggle;
