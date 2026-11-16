# Laboratorio 11 Comunicación entre componentes en React

**Estudiante:** Pamela Meneses
**Curso:** Desarrollo de Aplicaciones Empresariales
**Proyecto:** Órbita Cine, continuación de la semana 10

## Desarrollo y casos de prueba

| Desarrollo | Código | Resultado y caso de prueba |
|---|---|---|
| Estilos y catálogo adaptable | `styles/global.css`, `components/MovieList/MovieList.css` | La cuadrícula usa 1 columna hasta 360 px, 2 hasta 900 px y 4 por encima. Comprobar cambiando el ancho de la ventana. |
| Adaptador | `data/adaptMovie.js`, `data/movies.js` | Transforma los registros de origen al modelo de React. Al abrir la cartelera se observaron 8 películas con título, imagen, clasificación y horarios. |
| Favoritas y aviso | `App.jsx`, `components/Header/Header.jsx`, `components/MovieCard/MovieCard.jsx` | Se marcó Beyond the Horizon. La cabecera pasó de 0 a 1 y apareció el aviso de Sonner. Tras volver a cargar persistió la favorita. Al quitarla, la cabecera volvió a 0 y apareció el aviso correspondiente. |
| Búsqueda y limpieza | `hooks/useDebounce.js`, `components/Hero/Hero.jsx`, `components/MovieSearch/MovieSearch.jsx` | Al escribir Tokyo, quedó una película, Midnight in Tokyo. Al pulsar Limpiar filtro, se recuperaron las 8 películas. El retardo es de 400 ms y el envío del formulario aplica el filtro inmediatamente. |
| Estrenos | `hooks/usePremieres.js`, `components/Premieres/Premieres.jsx` | Se observó la carga y el carrusel en la ruta normal. En `/?premieres=error` se observó la carga seguida del mensaje de error. Se usan tres películas ficticias del catálogo para simular la respuesta. |

Las rutas de código son relativas a `frontend/src`. Comprobaciones ejecutadas con éxito en el frontend: `npm run lint` y `npm run build`.

## Árbol de componentes y datos

```text
App [texto y consulta de búsqueda, identificadores de favoritas]
├── Header [recibe favoriteCount]
├── Hero [recibe el texto y las funciones de cambio, envío y limpieza]
│   └── MovieSearch [campo controlado por App]
├── MovieList [recibe consulta y favoritas, calcula resultados y columnas]
│   └── MovieCard [recibe la película, isFavorite y la función de cambio]
├── Premieres [estado de petición en usePremieres]
│   ├── PremiereSkeleton [carga]
│   └── PremiereCarousel [recibe estrenos, calcula columnas]
├── Toaster [muestra los avisos de Sonner]
└── Footer
```

El contador se calcula con `favoriteIds.length` en App. Header recibe el número. Las tarjetas solicitan el cambio por medio de MovieList y App vuelve a calcular el total con los identificadores actualizados. Un contador independiente en Header duplicaría ese dato y podría quedar desfasado de las tarjetas.

`useDebounce` controla el temporizador y su cancelación. `useWindowSize` se reutiliza en MovieList y PremiereCarousel para reaccionar al redimensionamiento. `usePremieres` concentra el estado de la petición simulada y cancela el temporizador al desmontar el componente.

## Conclusiones

Elevar el filtro a App permite que el banner y el listado se actualicen con el mismo dato. Compartir el total derivado de favoritas mantiene sincronizadas la cabecera y las tarjetas. La sección de estrenos comunica qué ocurre durante la espera y cuando falla la petición.
