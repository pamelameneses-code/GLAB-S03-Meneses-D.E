# Laboratorio 09 ReactJS

Cartelera académica de Órbita Cine.

## Ejecución

Desde frontend ejecutar npm ci y npm run dev. Abrir la dirección que muestra Vite.

Para comprobar: npm run build y npm run lint.

## Componentes y props

App carga movies.js y compone Header, Hero, MovieList y Footer. Pasa movie a Hero y movies a MovieList. MovieList recorre con map, pasa movie a MovieCard y usa movie.id como key. Cada componente tiene carpeta y CSS. src/styles/global.css define la base. public/images contiene los ocho afiches SVG locales.

Los datos son ficticios y locales, según el alcance del laboratorio.

## Evidencias

Consultar ../docs/lab09/. Los tres errores solicitados se provocaron y corrigieron. La versión final no los conserva.
