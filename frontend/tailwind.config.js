/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {},
    fontFamily: {
      sans: ['ui-sans-serif', '-apple-system', 'system-ui', 'Roboto', 'sans-serif'],
    },
  },
  plugins: [],
}