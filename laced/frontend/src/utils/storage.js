export const saveToStorage = (key, value) => {
  localStorage.setItem(key, JSON.stringify(value));
};

export const loadFromStorage = (key, defaultValue = null) => {
  const stored = localStorage.getItem(key);
  if (!stored) return defaultValue;
  try {
    return JSON.parse(stored);
  } catch (err) {
    console.error("Storage parse error:", err);
    return defaultValue;
  }
};

export const removeFromStorage = (key) => {
  localStorage.removeItem(key);
};
