import { useEffect, useRef, useState } from 'react'
import Button from '../Button/Button.jsx'
import './MovieSearch.css'

export default function MovieSearch({ onSearch }) {
  const [searchText, setSearchText] = useState('')
  const timeoutRef = useRef(null)

  useEffect(() => {
    timeoutRef.current = setTimeout(() => {
      console.info('[search:filter]', searchText.trim())
      onSearch(searchText.trim())
    }, 400)

    return () => clearTimeout(timeoutRef.current)
  }, [searchText, onSearch])

  function handleChange(event) {
    const nextText = event.target.value
    console.info('[search:input]', nextText)
    setSearchText(nextText)
  }

  function handleSubmit(event) {
    event.preventDefault()
    clearTimeout(timeoutRef.current)
    console.info('[search:submit]', searchText.trim())
    onSearch(searchText.trim())
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
          onChange={handleChange}
          aria-describedby="search-hint"
        />
        <Button type="submit" variant="primary">Buscar películas <span aria-hidden="true">↗</span></Button>
      </div>
      <p className="form-hint" id="search-hint">La cartelera se actualiza al terminar de escribir.</p>
    </form>
  )
}
