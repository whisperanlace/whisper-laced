import React from "react";
import { useAppContext } from "../../context/AppContext";

const FeetToggle = () => {
  const { feet, setFeet } = useAppContext();
  return (
    <label className="flex items-center space-x-2">
      <input type="checkbox" checked={feet} onChange={(e) => setFeet(e.target.checked)} />
      <span>Feet</span>
    </label>
  );
};

export default FeetToggle;
