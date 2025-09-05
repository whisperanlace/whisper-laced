import React from "react";
import { useAppContext } from "../context/AppContext";

const Settings = () => {
  const { nsfw, setNSFW, feet, setFeet, mirror, setMirror } = useAppContext();

  return (
    <div className="p-4 space-y-4">
      <h2 className="text-xl font-playfair text-wine-red">Settings</h2>
      <label className="flex items-center space-x-2">
        <input type="checkbox" checked={nsfw} onChange={(e) => setNSFW(e.target.checked)} />
        <span>Enable NSFW</span>
      </label>
      <label className="flex items-center space-x-2">
        <input type="checkbox" checked={feet} onChange={(e) => setFeet(e.target.checked)} />
        <span>Enable Feet Content</span>
      </label>
      <label className="flex items-center space-x-2">
        <input type="checkbox" checked={mirror} onChange={(e) => setMirror(e.target.checked)} />
        <span>Enable Mirror Accuracy</span>
      </label>
    </div>
  );
};

export default Settings;
