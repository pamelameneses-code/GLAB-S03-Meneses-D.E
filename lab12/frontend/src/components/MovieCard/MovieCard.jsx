import Button from '../Button/Button.jsx'
import './MovieCard.css'
export default function MovieCard({ movie, isFavorite, onToggleFavorite }) {
  return (
    <article className="movie-card">
      <div className="poster-wrap">
        <img src={movie.image} alt={movie.title} loading="lazy" />
        <span className="movie-rating" aria-label={'Valoración: ' + movie.rating + ' de 10'}>★ {movie.rating.toFixed(1)}</span>
      </div>
      <div className="movie-title-row"><h3>{movie.title}</h3><span className="classification">{movie.classification}</span></div>
      <p className="movie-synopsis">{movie.synopsis}</p>
      <p className="showtimes-label">HORARIOS DE HOY</p>
      <ul className="showtimes" aria-label={'Horarios de ' + movie.title}>
        {movie.showtimes.map((showtime) => <li key={showtime}><time>{showtime}</time></li>)}
      </ul>
      <Button
        className="favorite-button"
        variant={isFavorite ? 'selected' : 'secondary'}
        aria-pressed={isFavorite}
        aria-label={(isFavorite ? 'Quitar de favoritas: ' : 'Agregar a favoritas: ') + movie.title}
        onClick={() => onToggleFavorite(movie.id)}
      >
        <span aria-hidden="true">{isFavorite ? '♥' : '♡'}</span>
        {isFavorite ? 'En favoritas' : 'Agregar a favoritas'}
      </Button>
    </article>
  )
}
