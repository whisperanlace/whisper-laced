import React from "react";

const Tooltip = ({ text, children }) => {
  return (
    <div className="relative group">
      {children}
      <div className="absolute bottom-full mb-1 left-1/2 transform -translate-x-1/2 bg-gray-700 text-white text-xs px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition">
        {text}
      </div>
    </div>
  );
};

export default Tooltip;
