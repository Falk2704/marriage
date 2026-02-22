/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html"],
  theme: {
    extend: {
      colors: {
        primary: "#4F6F5B",
        bg: "#F4F1E8",
        "bg-alt": "#E9E4D6",
        accent: "#6F8F78",
        body: "#2F3A33",
      },
      fontFamily: {
        serif: ['"PT Serif"', "Georgia", "serif"],
        script: ['"Petit Formal Script"', "cursive"],
      },
      maxWidth: {
        content: "52rem",
      },
    },
  },
  plugins: [],
};
