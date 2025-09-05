import React from "react";

const Card = ({ children, className = "" }) => {
  return (
    <div className={`border rounded p-4 bg-ivory shadow-sm ${className}`}>
      {children}
    </div>
  );
};

export default Card;
