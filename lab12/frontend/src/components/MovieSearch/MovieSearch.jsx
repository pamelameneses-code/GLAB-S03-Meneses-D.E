import Button from '../Button/Button.jsx'
import './MovieSearch.css'

export default function MovieSearch({ searchText, onChange, onSubmit }) {
  function handleSubmit(event) {
    event.preventDefault()
    onSubmit()
    window.location.hash = 'movies'
  }

  return (
    <form className="movie-search" role="search" onSubmit={handleSubmit}>
      <label htmlFor="movie-search">Encuentra tu próxima película</label>
      <div className="search-controls">
        <input
          id="movie-search"
          type="search"
          placeholder="Buscar por título…"
          value={searchText}
          onChange={(event) => onChange(event.target.value)}
          aria-describedby="search-hint"
        />
        <Button type="submit" variant="primary">Buscar películas <span aria-hidden="true">↗</span></Button>
      </div>
      <p className="form-hint" id="search-hint">La cartelera se actualiza al terminar de escribir.</p>
    </form>
  )
}
