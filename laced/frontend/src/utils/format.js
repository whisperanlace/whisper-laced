export const formatDate = (date) => {
  const d = new Date(date);
  return `${d.getMonth()+1}/${d.getDate()}/${d.getFullYear()} ${d.getHours()}:${d.getMinutes().toString().padStart(2, '0')}`;
};

export const truncateText = (text, length = 50) => {
  return text.length > length ? text.substring(0, length) + "..." : text;
};
