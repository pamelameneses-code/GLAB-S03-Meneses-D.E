# Laboratorio 09 ReactJS

Estudiante: Pamela Meneses. Fecha: 30 de octubre de 2026.

Curso: Desarrollo de Aplicaciones Empresariales.

## 1. Crear el proyecto con Vite

Se verificó Node.js v24.16.0 y npm 11.13.0. Se creó frontend con la plantilla React, se instalaron dependencias y se inició el servidor.

Resultado: Vite inicia en http://127.0.0.1:5173/.

Caso de prueba: Abrir el servidor: la interfaz debe responder.

Código o comandos:

node -v
npm create vite@latest frontend -- --template react --no-interactive
cd frontend
npm install
npm run dev

## 2. Limpiar la plantilla

Se reemplazó la demostración por index.html, src/main.jsx y src/App.jsx. Se retiraron los logos, el contador y los estilos de ejemplo.

Resultado: React monta App dentro de root y el documento utiliza el idioma español.

Caso de prueba: Recargar: no aparecen elementos de demostración.

Código o comandos:

src/main.jsx

## 3. Organizar componentes datos y estilos

src/components tiene una carpeta por componente con JSX y CSS. src/data contiene movies.js y src/styles contiene global.css. Cada componente importa su CSS. La guía adjunta no detalla otra arquitectura CSS.

Resultado: Se separan datos, presentación y composición.

Caso de prueba: Revisar la captura de la estructura en VS Code.

## 4. Escribir los datos de la cartelera

movies.js exporta ocho películas ficticias con id, title, image, synopsis, classification, rating y showtimes. Los afiches son ilustraciones SVG locales creadas para esta práctica.

Resultado: Ocho registros completos y tres horarios por película.

Caso de prueba: Se observan ocho tarjetas y 24 horarios. Todas las imágenes cargan.

Código o comandos:

src/data/movies.js

## 5. Crear Header

Header contiene el nombre del cine y navegación a Inicio, Cartelera y Contacto. Los enlaces apuntan a los identificadores de las secciones.

Resultado: Aparece ÓRBITA CINE con navegación.

Caso de prueba: Pulsar Cartelera: la dirección termina en #movies.

Código o comandos:

src/components/Header/Header.jsx

## 6. Crear Footer

Footer contiene contacto e información. La dirección es de demostración y el correo utiliza el dominio reservado .example.

Resultado: Se muestran correo, dirección y horario de atención.

Caso de prueba: Pulsar Contacto: la dirección termina en #contact y se llega al pie.

Código o comandos:

src/components/Footer/Footer.jsx

## 7. Crear Hero con props

App pasa movies[0] mediante la prop movie. Hero muestra el afiche, título, sinopsis, clasificación y valoración. El componente no importa los datos.

Resultado: Beyond the Horizon aparece como película destacada.

Caso de prueba: Comparar el banner con el primer objeto de movies.js.

Código o comandos:

src/components/Hero/Hero.jsx

## 8. Crear MovieCard con props

MovieCard recibe movie y muestra su imagen, título, valoración y horarios. También presenta sinopsis y clasificación. Los horarios se recorren con map y usan cada horario como key, único dentro de la película.

Resultado: Una misma tarjeta presenta cualquier película recibida.

Caso de prueba: Cada tarjeta tiene datos propios y tres horarios.

Código o comandos:

src/components/MovieCard/MovieCard.jsx

## 9. Crear MovieList con map y key

MovieList recibe movies desde App, recorre el arreglo con map y pasa cada objeto a MovieCard. La clave estable de cada tarjeta es movie.id.

Resultado: Se dibujan ocho tarjetas sin repetir manualmente el componente.

Caso de prueba: Se contaron 8 elementos article.movie-card y ninguna advertencia de key.

Código o comandos:

src/components/MovieList/MovieList.jsx

## 10. Componer la interfaz en App

App importa los datos y reúne Header, Hero, MovieList y Footer. Pasa la primera película a Hero y el arreglo completo a MovieList. Un fragmento agrupa los nodos raíz.

Resultado: Interfaz completa verificada en escritorio y móvil.

Caso de prueba: 8 tarjetas, 24 horarios, 9 imágenes cargadas, enlaces correctos, sin desbordamiento a 390 px y consola limpia.

Código o comandos:

src/App.jsx

## 11. Provocar y corregir los tres errores JSX

Se sustituyó temporalmente App.jsx por cada ejemplo defectuoso. Se capturaron mensajes reales y se restauró el archivo original. class y key generan advertencias; dos nodos raíz adyacentes impiden compilar.

Resultado: Los tres diagnósticos quedaron registrados en jsx-errors.json.

Caso de prueba: Se repitió la comprobación final: la consola quedó limpia.

## 12. Preparar repositorio y entregable

El frontend continúa el repositorio acumulativo. package.json y package-lock.json declaran dependencias; .gitignore excluye node_modules y dist. El entregable incluye capturas, código, explicación, casos de prueba y recorte en componentes.

Resultado: Archivos organizados en frontend/ y docs/lab09/.

Caso de prueba: Ejecutar npm ci, npm run build y npm run lint. Revisar integrantes y aportes reales antes de presentar en el campus.

## Evidencias

- evidence/desktop.png: interfaz completa.
- evidence/mobile.png: vista móvil.
- evidence/editor.png: estructura en VS Code.
- evidence/components.png: interfaz dividida en componentes.
- checks.json: comprobaciones del navegador.
- jsx-errors.json: mensajes reales de los errores.
- Informe-Lab09.pdf: informe con explicación, capturas y código.

## Conclusiones

Los componentes permiten reutilizar la tarjeta. Las props mantienen los datos en el padre y permiten a los hijos dibujar la información recibida. map construye la cartelera y key identifica cada película. Vite permite ejecutar y compilar la aplicación.

## Integrantes y aportes

Estudiante: Pamela Meneses. Completar la distribución real de aportes con los integrantes del equipo antes de entregar; no se han supuesto nombres ni responsabilidades.

## Entrega

Repositorio: https://github.com/pamelameneses-code/GLAB-S03-Meneses-D.E

La presentación final en el campus virtual y la comprobación del plazo corresponden al equipo.
