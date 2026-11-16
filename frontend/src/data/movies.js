import adaptMovie from './adaptMovie.js'

export const movies = [
  {
    "movie_id": 1,
    "original_title": "Beyond the Horizon",
    "poster_path": "/images/horizon.svg",
    "overview": "Una astronauta recibe una señal imposible y viaja hacia los límites del universo.",
    "age_rating": "PG-13",
    "vote_average": 8.8,
    "screenings": [
      "15:00",
      "18:00",
      "21:00"
    ]
  },
  {
    "movie_id": 2,
    "original_title": "The Last Light",
    "poster_path": "/images/light.svg",
    "overview": "Dos hermanos cruzan un desierto para encontrar la última ciudad iluminada.",
    "age_rating": "PG-13",
    "vote_average": 8.2,
    "screenings": [
      "14:30",
      "17:30",
      "20:30"
    ]
  },
  {
    "movie_id": 3,
    "original_title": "Midnight in Tokyo",
    "poster_path": "/images/tokyo.svg",
    "overview": "Una fotógrafa descubre una historia oculta entre las luces y calles de Tokio.",
    "age_rating": "PG-13",
    "vote_average": 8.5,
    "screenings": [
      "16:00",
      "19:00",
      "22:00"
    ]
  },
  {
    "movie_id": 4,
    "original_title": "Wild Hearts",
    "poster_path": "/images/hearts.svg",
    "overview": "Una exploradora y su hermano intentan proteger el bosque donde crecieron.",
    "age_rating": "PG",
    "vote_average": 7.9,
    "screenings": [
      "14:00",
      "16:30",
      "19:00"
    ]
  },
  {
    "movie_id": 5,
    "original_title": "Ocean of Secrets",
    "poster_path": "/images/ocean.svg",
    "overview": "Un equipo de buzos encuentra una ciudad sumergida y un misterio que cambia sus vidas.",
    "age_rating": "PG-13",
    "vote_average": 8.1,
    "screenings": [
      "15:30",
      "18:30",
      "21:30"
    ]
  },
  {
    "movie_id": 6,
    "original_title": "The Clockmaker",
    "poster_path": "/images/clock.svg",
    "overview": "Un relojero descubre que su última creación puede detener el tiempo por un minuto.",
    "age_rating": "PG",
    "vote_average": 8.6,
    "screenings": [
      "14:15",
      "17:15",
      "20:15"
    ]
  },
  {
    "movie_id": 7,
    "original_title": "Little Planet",
    "poster_path": "/images/planet.svg",
    "overview": "Una pequeña robot busca un nuevo hogar para las criaturas de su planeta.",
    "age_rating": "G",
    "vote_average": 8.3,
    "screenings": [
      "14:00",
      "16:00",
      "18:00"
    ]
  },
  {
    "movie_id": 8,
    "original_title": "Echoes of Winter",
    "poster_path": "/images/winter.svg",
    "overview": "Una pianista regresa a su pueblo nevado para reconstruir los recuerdos de su familia.",
    "age_rating": "PG-13",
    "vote_average": 8,
    "screenings": [
      "15:45",
      "18:45",
      "21:45"
    ]
  }
].map(adaptMovie)
