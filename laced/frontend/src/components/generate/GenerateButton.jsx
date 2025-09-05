import React from "react";

const GenerateButton = ({ onClick, loading }) => {
  return (
    <button
      onClick={onClick}
      disabled={loading}
      className="bg-gold text-wine-red px-4 py-2 rounded hover:shadow-lg transition disabled:opacity-50"
    >
      {loading ? "Generating..." : "Generate"}
    </button>
  );
};

export default GenerateButton;
