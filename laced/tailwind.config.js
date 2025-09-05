/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        ivory: "#FFF8F0",
        "wine-red": "#8B0000",
        gold: "#FFD700",
      },
      fontFamily: {
        playfair: ["'Playfair Display'", "serif"],
        raleway: ["'Raleway'", "sans-serif"],
      },
    },
  },
  plugins: [],
}
