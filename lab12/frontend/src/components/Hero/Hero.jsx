import MovieSearch from '../MovieSearch/MovieSearch.jsx'
import Button from '../Button/Button.jsx'
import './Hero.css'
export default function Hero({ movie, searchText, onSearchChange, onSearchSubmit, showClear }) {
  return (
    <section className="hero" id="home" aria-labelledby="featured-title">
      <img className="hero-image" src={movie.image} alt={movie.title} />
      <div className="hero-content">
        <p className="eyebrow">LA PELÍCULA DESTACADA</p>
        <p className="hero-meta">{movie.classification} <span>★ {movie.rating.toFixed(1)} / 10</span></p>
        <h1 id="featured-title">{movie.title}</h1>
        <p className="hero-synopsis">{movie.synopsis}</p>
        <MovieSearch searchText={searchText} onChange={onSearchChange} onSubmit={onSearchSubmit} />
        {showClear && <Button variant='secondary' onClick={() => onSearchChange('')}>Limpiar filtro</Button>}
      </div>
      <p className="hero-caption">EN ÓRBITA, CADA HISTORIA ES UN VIAJE.</p>
    </section>
  )
}
