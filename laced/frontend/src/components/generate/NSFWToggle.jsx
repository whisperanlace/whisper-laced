import React from "react";
import { useAppContext } from "../../context/AppContext";

const NSFWToggle = () => {
  const { nsfw, setNSFW } = useAppContext();
  return (
    <label className="flex items-center space-x-2">
      <input type="checkbox" checked={nsfw} onChange={(e) => setNSFW(e.target.checked)} />
      <span>NSFW</span>
    </label>
  );
};

export default NSFWToggle;
