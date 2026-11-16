import { useEffect, useRef } from 'react'
import Button from '../Button/Button.jsx'
import usePremieres from '../../hooks/usePremieres.js'
import useWindowSize from '../../hooks/useWindowSize.js'
import './Premieres.css'

function PremiereSkeleton() {
  return (
    <div role="status">
      <p>Cargando próximos estrenos…</p>
      <div className="premiere-skeleton" aria-hidden="true" />
    </div>
  )
}

function PremiereCarousel({ movies }) {
  const carousel = useRef(null)
  const { width } = useWindowSize()
  const columns = width <= 540 ? 1 : 2

  useEffect(() => {
    carousel.current.scrollLeft = 0
  }, [columns])

  function move(direction) {
    const list = carousel.current
    const step = list.children[1].offsetLeft - list.children[0].offsetLeft
    list.scrollBy({ left: step * direction })
  }

  return (
    <div role="region" aria-label="Carrusel de estrenos">
      <div className="premiere-controls">
        <Button variant="secondary" onClick={() => move(-1)}>Anterior</Button>
        <Button variant="secondary" onClick={() => move(1)}>Siguiente</Button>
      </div>
      <ul className="premiere-carousel" ref={carousel} style={{ '--premiere-columns': columns }}>
        {movies.map((movie) => (
          <li key={movie.id} className="premiere-card">
            <img src={movie.image} alt="" />
            <div>
              <h3>{movie.title}</h3>
              <p>{movie.synopsis}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default function Premieres({ movies, simulateError }) {
  const result = usePremieres(movies, simulateError)

  return (
    <section className="premieres" aria-labelledby="premieres-title">
      <h2 id="premieres-title">Próximos estrenos</h2>
      {result.status === 'loading' && <PremiereSkeleton />}
      {result.status === 'success' && <PremiereCarousel movies={result.movies} />}
      {result.status === 'error' && (
        <p className="premiere-error" role="alert">No pudimos cargar los estrenos. Recarga la página para intentar de nuevo.</p>
      )}
    </section>
  )
}
