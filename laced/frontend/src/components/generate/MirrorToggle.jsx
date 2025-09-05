import React from "react";
import { useAppContext } from "../../context/AppContext";

const MirrorToggle = () => {
  const { mirror, setMirror } = useAppContext();
  return (
    <label className="flex items-center space-x-2">
      <input type="checkbox" checked={mirror} onChange={(e) => setMirror(e.target.checked)} />
      <span>Mirror</span>
    </label>
  );
};

export default MirrorToggle;
