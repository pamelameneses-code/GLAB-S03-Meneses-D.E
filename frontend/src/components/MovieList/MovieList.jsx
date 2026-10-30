import MovieCard from '../MovieCard/MovieCard.jsx'
import './MovieList.css'
export default function MovieList({ movies }) {
  return (
    <section className="movie-list" id="movies" aria-labelledby="movies-title">
      <div className="section-heading">
        <div><p className="eyebrow">ELIGE TU PRÓXIMA HISTORIA</p><h2 id="movies-title">En cartelera</h2></div>
        <p>{movies.length} películas en pantalla</p>
      </div>
      <div className="movie-grid">
        {movies.map((movie) => <MovieCard key={movie.id} movie={movie} />)}
      </div>
    </section>
  )
}
