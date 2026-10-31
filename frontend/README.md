# Cartelera ReactJS Laboratorios 09 y 10

Cartelera académica de Órbita Cine.

## Ejecución

Desde frontend ejecutar npm ci y npm run dev. Abrir la dirección que muestra Vite.

Para comprobar: npm run build y npm run lint.

## Componentes y props

App carga movies.js y compone Header, Hero, MovieList y Footer. Pasa movie a Hero y movies a MovieList. MovieList recorre con map, pasa movie a MovieCard y usa movie.id como key. Cada componente tiene carpeta y CSS. src/styles/global.css define la base. public/images contiene los ocho afiches SVG locales.

Los datos son ficticios y locales, según el alcance del laboratorio.

## Evidencias

Consultar ../docs/lab09/. Los tres errores solicitados se provocaron y corrigieron. La versión final no los conserva.

## Laboratorio 10 Componentes y eventos

La misma cartelera incorpora Button reutilizable con children y variantes primary, secondary y selected. MovieSearch es una entrada controlada con un retardo de 400 ms; su botón aplica la búsqueda inmediatamente. MovieList filtra por título y muestra un estado vacío si no hay coincidencias.

App conserva favoriteIds y searchQuery. Las tarjetas reciben isFavorite y onToggleFavorite; avisan al padre mediante la función recibida. Las favoritas se guardan en localStorage bajo orbita.favoriteMovieIds y se recuperan al cargar la página en el mismo origen.

Consultar ../docs/lab10/README.md para los doce pasos, las decisiones de estado y las pruebas. Se registraron 19 comprobaciones correctas; al escribir Tokyo rápidamente se observaron cinco eventos de entrada y un único filtrado después del retardo. No se añadieron dependencias.
