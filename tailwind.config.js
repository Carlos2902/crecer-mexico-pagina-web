// tailwind.config.js
module.exports = {
    content: [
      './apps/**/*.{html,js,py}', // Ajusta esto a las rutas de tus plantillas Django
      './templates/**/*.{html,js,py}',
    ],
    theme: {
      extend: {
        colors: {
          'figma-green': '#69C624', // Puedes darle el nombre que quieras
        },
      },
    },
    plugins: [],
  }