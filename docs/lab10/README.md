# Laboratorio 10 Componentes y eventos

Estudiante: Pamela Meneses. Curso: Desarrollo de Aplicaciones Empresariales. Fecha: 30 de octubre de 2026.

Continuación directa del laboratorio 9 según el paso 1 de la guía GLAB-S10-MMONTGOMERY-2026-02.docx.

## 1. Partir del laboratorio 9

Se continuó el frontend existente de GLAB-S03-Meneses, con su cartelera de ocho películas, datos, estilos y componentes. No se creó otro proyecto.

Resultado: Inicio con ocho tarjetas y servidor Vite en el puerto 5173.

Caso de prueba: Abrir la página y contar ocho películas.

## 2. Ampliar los estilos base

Se añadieron estilos para entradas de búsqueda, tipografía de controles, texto auxiliar y foco visible. Los estilos de Button y MovieSearch se mantienen en sus carpetas.

Resultado: Controles legibles e integrados en el diseño existente.

Caso de prueba: Revisar formulario en escritorio y móvil; no hay desbordamiento a 390 px.

Código: frontend/src/styles/global.css

## 3. Crear Button reutilizable

Button recibe contenido mediante children y aspecto mediante variant. Las variantes primary, secondary y selected comparten una única implementación. El buscador utiliza primary; cada tarjeta utiliza secondary o selected según su estado. La llamada a la acción anterior del banner se sustituyó por el botón del formulario.

Resultado: El mismo componente sirve en el banner y en ocho tarjetas cambiando props.

Caso de prueba: Buscar una película y marcar una favorita: ambos controles utilizan Button.

Código: frontend/src/components/Button/Button.jsx

## 4. Añadir el estado de favoritas a App

App mantiene favoriteIds mediante useState. toggleFavorite usa la actualización funcional para agregar o quitar un identificador sin mutar el arreglo anterior. Se guardan identificadores, no copias completas de las películas.

Resultado: Una sola fuente del estado de favoritas, compartida por todas las tarjetas.

Caso de prueba: Marcar dos películas: el contador muestra dos favoritas.

Código: frontend/src/App.jsx

## 5. Comunicar MovieCard con App

App pasa toggleFavorite como onToggleFavorite a MovieList y luego a MovieCard. La tarjeta llama onToggleFavorite(movie.id) al pulsar el botón; App actualiza el estado y devuelve isFavorite. El hijo no modifica el estado del padre.

Resultado: El botón alterna entre Agregar a favoritas y En favoritas, con aria-pressed y variante visual.

Caso de prueba: Marcar y desmarcar la primera película: cambia el texto, el estilo y el contador sin recargar.

Código: frontend/src/components/MovieCard/MovieCard.jsx

## 6. Crear MovieSearch controlado

searchText vive en MovieSearch con useState. El valor del input viene de ese estado y onChange actualiza cada pulsación. El formulario evita la recarga con preventDefault.

Resultado: La entrada siempre refleja el estado de React.

Caso de prueba: Escribir Tokyo: la entrada refleja las cinco letras inmediatamente.

Código: frontend/src/components/MovieSearch/MovieSearch.jsx

## 7. Añadir el retardo de búsqueda

Un efecto programa onSearch tras 400 ms y cancela el temporizador anterior en cada cambio. La referencia timeoutRef guarda el temporizador sin provocar renders. La consola diferencia [search:input] de [search:filter]. Al enviar el formulario se cancela el retardo pendiente y se aplica la búsqueda inmediatamente.

Resultado: Prueba real con Tokyo: cinco eventos de entrada y un filtrado después de la pausa.

Caso de prueba: Escribir Tokyo rápido y observar la consola: T, To, Tok, Toky, Tokyo y un único [search:filter] Tokyo.

## 8. Filtrar MovieList y mostrar estado vacío

MovieList recibe searchQuery y filtra por título sin distinguir mayúsculas. filteredMovies se calcula a partir de props, no se duplica en estado. Sin coincidencias se muestran cero películas y un mensaje explicativo.

Resultado: Tokyo devuelve Midnight in Tokyo; una consulta inexistente muestra el estado vacío.

Caso de prueba: Buscar zz-no-matching-movie: aparece No encontramos películas y no hay tarjetas. Borrar el texto restaura ocho.

Código: frontend/src/components/MovieList/MovieList.jsx

## 9. Integrar el buscador en Hero

Hero recibe onSearch desde App y lo entrega a MovieSearch. El botón Buscar películas envía el formulario, aplica el texto y navega a #movies. App conserva la consulta aplicada para compartirla entre el banner y la lista.

Resultado: La búsqueda funciona desde el banner y su llamada a la acción.

Caso de prueba: Buscar oCeAn y pulsar el botón: aparece Ocean of Secrets y la dirección termina en #movies.

Código: frontend/src/components/Hero/Hero.jsx

## 10. Persistir y recuperar favoritas

App inicializa favoriteIds leyendo localStorage mediante un inicializador de useState. Un efecto guarda cada cambio en orbita.favoriteMovieIds. Se valida el formato, se descartan ids inexistentes y se evitan duplicados. Ante un dato inválido se utiliza una lista vacía.

Resultado: Las favoritas permanecen tras recargar el mismo navegador y origen.

Caso de prueba: Guardar las películas 1 y 8, recargar y comprobar ambos botones seleccionados. Quitar la 1 y comprobar que queda el id 8.

## 11. Documentar la ubicación de cada dato

Se documentó por qué favoriteIds y searchQuery viven en App, por qué searchText y timeoutRef viven en MovieSearch, y por qué los datos derivados no requieren useState. Se incluyó la captura real del estado vacío.

Resultado: Decisiones de estado documentadas y evidencias organizadas.

Caso de prueba: Revisar la tabla de estado y evidence/empty-state.png.

## 12. Preparar repositorio y entrega

La continuación se guarda en el mismo repositorio. Los componentes y sus observaciones se documentan en docs/lab10. Se incluyen código, pruebas, capturas y dependencias ya declaradas en package.json; no se añadieron librerías.

Resultado: Código y evidencias listos para revisión.

Caso de prueba: Ejecutar npm run build y npm run lint. El equipo debe completar aportes reales y presentar el informe en el campus dentro del plazo.

## Ubicación y razón de cada dato

| Dato | Componente y mecanismo | Razón | Persistencia |
|---|---|---|---|
| favoriteIds | App / useState | Lo comparten todas las tarjetas y el contador; App coordina sus cambios. | Sí, localStorage |
| searchQuery | App / useState | Consulta aplicada después del retardo o del envío; conecta el buscador del banner con MovieList. | No |
| searchText | MovieSearch / useState | Texto inmediato de la entrada controlada, distinto de la consulta aplicada durante el retardo. | No |
| timeoutRef | MovieSearch / useRef | Identificador del temporizador para cancelarlo; no afecta por sí mismo a la interfaz. | No |
| filteredMovies | MovieList / dato derivado | Se calcula desde movies y searchQuery; guardarlo en estado duplicaría información. | No |
| isFavorite | MovieList / prop derivada | Se calcula con favoriteIds.includes(movie.id) y se entrega a la tarjeta. | No |
| movies | src/data/movies.js / constante | Cartelera del laboratorio 9; no cambia durante esta práctica. | Archivo del proyecto |

## Comprobaciones y capturas

Se superaron 19 comprobaciones funcionales en navegador aislado, sin cambiar las favoritas personales del navegador del estudiante. Los resultados detallados se encuentran en checks.json.

- evidence/desktop.png: cartelera inicial con buscador y botones.
- evidence/favorites.png: dos favoritas recuperadas tras recargar.
- evidence/search-result.png: búsqueda Tokyo con una coincidencia.
- evidence/empty-state.png: búsqueda sin coincidencias.
- evidence/mobile.png: vista a 390 px.
- evidence/editor.png: estructura real en VS Code.
- debounce-console.txt: registro real de cinco entradas frente a un filtrado.

Para repetir el retardo manualmente, abrir F12 > Consola y escribir Tokyo rápidamente. Se verán cinco mensajes [search:input] y uno [search:filter] tras 400 ms sin pulsaciones. El envío del formulario produce [search:submit] y aplica inmediatamente. Al iniciar la página también existe un filtrado inicial; no se cuenta como pulsación.

Para persistencia, agregar favoritas y recargar en el mismo origen. localhost:5173 y 127.0.0.1:5173 tienen almacenamientos distintos.

## Observaciones

Button es reutilizable porque el mismo JSX recibe texto e iconos por children y estilos por variant. MovieCard no tiene un estado propio de favoritas: comunica el evento hacia App mediante una función recibida. Los cambios de búsqueda y favoritas actualizan la interfaz con React sin recargar.

## Conclusiones

1. Button permite reutilizar controles con contenido y variantes por props.
2. useState mantiene las favoritas y la entrada de búsqueda sincronizadas con la interfaz.
3. Las funciones pasadas por props permiten que las tarjetas comuniquen sus eventos a App.
4. El retardo de 400 ms reduce los filtrados durante la escritura; el estado vacío informa cuando no existen coincidencias.
5. localStorage conserva las favoritas entre recargas del mismo navegador y origen.

## Integrantes y presentación

Completar la distribución real de aportes entre integrantes antes de entregar; no se han supuesto nombres ni responsabilidades. Repositorio del equipo: https://github.com/pamelameneses-code/GLAB-S03-Meneses-D.E. La presentación final en el campus virtual y la revisión del plazo corresponden al equipo.
