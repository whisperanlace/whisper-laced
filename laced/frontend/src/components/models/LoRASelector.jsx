import React, { useState, useEffect } from "react";
import { getLoRAs, applyLoRA } from "../../api/lora";

const LoRASelector = ({ onApply }) => {
  const [loras, setLoras] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchLoRAs = async () => {
      setLoading(true);
      try {
        const data = await getLoRAs();
        setLoras(data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchLoRAs();
  }, []);

  const handleApply = async (id) => {
    try {
      await applyLoRA(id);
      if (onApply) onApply(id);
    } catch (err) {
      console.error("Failed to apply LoRA", err);
    }
  };

  if (loading) return <p>Loading LoRAs...</p>;
  if (!loras.length) return <p>No LoRAs available</p>;

  return (
    <div className="grid grid-cols-2 gap-2">
      {loras.map(lora => (
        <button
          key={lora.id}
          className="border rounded p-2 hover:bg-gold hover:text-wine-red transition"
          onClick={() => handleApply(lora.id)}
        >
          {lora.name}
        </button>
      ))}
    </div>
  );
};

export default LoRASelector;
