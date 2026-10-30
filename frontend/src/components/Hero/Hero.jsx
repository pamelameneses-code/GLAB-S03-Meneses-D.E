import './Hero.css'
export default function Hero({ movie }) {
  return (
    <section className="hero" id="home" aria-labelledby="featured-title">
      <img className="hero-image" src={movie.image} alt={movie.title} />
      <div className="hero-content">
        <p className="eyebrow">LA PELÍCULA DESTACADA</p>
        <p className="hero-meta">{movie.classification} <span>★ {movie.rating.toFixed(1)} / 10</span></p>
        <h1 id="featured-title">{movie.title}</h1>
        <p className="hero-synopsis">{movie.synopsis}</p>
        <a className="primary-link" href="#movies">Explorar cartelera <span aria-hidden="true">↗</span></a>
      </div>
      <p className="hero-caption">EN ÓRBITA, CADA HISTORIA ES UN VIAJE.</p>
    </section>
  )
}
