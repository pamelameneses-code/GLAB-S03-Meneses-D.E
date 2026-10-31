import MovieCard from '../MovieCard/MovieCard.jsx'
import './MovieList.css'
export default function MovieList({ movies, searchQuery, favoriteIds, onToggleFavorite }) {
  const normalizedQuery = searchQuery.trim().toLowerCase()
  const filteredMovies = movies.filter((movie) => movie.title.toLowerCase().includes(normalizedQuery))

  return (
    <section className="movie-list" id="movies" aria-labelledby="movies-title">
      <div className="section-heading">
        <div><p className="eyebrow">ELIGE TU PRÓXIMA HISTORIA</p><h2 id="movies-title">En cartelera</h2></div>
        <div className="list-summary" role="status" aria-live="polite">
          <p>{filteredMovies.length} {filteredMovies.length === 1 ? 'película en pantalla' : 'películas en pantalla'}</p>
          <p>{favoriteIds.length} {favoriteIds.length === 1 ? 'favorita guardada' : 'favoritas guardadas'}</p>
        </div>
      </div>
      {filteredMovies.length > 0 ? (
        <div className="movie-grid">
          {filteredMovies.map((movie) => (
            <MovieCard
              key={movie.id}
              movie={movie}
              isFavorite={favoriteIds.includes(movie.id)}
              onToggleFavorite={onToggleFavorite}
            />
          ))}
        </div>
      ) : (
        <div className="empty-state" role="status">
          <span aria-hidden="true">⌕</span>
          <h3>No encontramos películas</h3>
          <p>No hay títulos que coincidan con «{searchQuery}».</p>
          <p>Prueba con otro título o borra el texto del buscador.</p>
        </div>
      )}
    </section>
  )
}
