/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'dark-bg': '#121212',
        'tattoo-accent': '#D4AF37',
      }
    },
  },
  plugins: [],
}
