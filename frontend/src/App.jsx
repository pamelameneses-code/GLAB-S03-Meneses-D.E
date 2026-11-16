import { useEffect, useState } from 'react'
import { Toaster, toast } from 'sonner'
import Header from './components/Header/Header.jsx'
import Footer from './components/Footer/Footer.jsx'
import Hero from './components/Hero/Hero.jsx'
import MovieList from './components/MovieList/MovieList.jsx'
import Premieres from './components/Premieres/Premieres.jsx'
import useDebounce from './hooks/useDebounce.js'
import { movies } from './data/movies.js'

const premiereMovies = movies.slice(-3)
const simulatePremiereError = new URLSearchParams(window.location.search).get('premieres') === 'error'
const FAVORITES_KEY = 'orbita.favoriteMovieIds'

function loadFavoriteIds() {
  try {
    const savedIds = JSON.parse(localStorage.getItem(FAVORITES_KEY) ?? '[]')
    return Array.isArray(savedIds)
      ? [...new Set(savedIds.filter((id) => movies.some((movie) => movie.id === id)))]
      : []
  } catch {
    return []
  }
}

export default function App() {
  const [favoriteIds, setFavoriteIds] = useState(loadFavoriteIds)
  const [searchText, setSearchText] = useState('')
  const [submittedText, setSubmittedText] = useState(null)
  const debouncedText = useDebounce(searchText, 400)
  const searchQuery = searchText === '' ? '' : submittedText ?? debouncedText

  function changeSearch(text) {
    setSubmittedText(null)
    setSearchText(text)
  }

  useEffect(() => {
    try {
      localStorage.setItem(FAVORITES_KEY, JSON.stringify(favoriteIds))
    } catch {
      console.warn('Favorite movies could not be saved in this browser.')
    }
  }, [favoriteIds])

  function toggleFavorite(movieId) {
    const movie = movies.find((item) => item.id === movieId)
    const action = favoriteIds.includes(movieId) ? 'Quitaste de favoritas' : 'Agregaste a favoritas'
    toast(action + ': ' + movie.title)
    setFavoriteIds((currentIds) => currentIds.includes(movieId)
      ? currentIds.filter((id) => id !== movieId)
      : [...currentIds, movieId])
  }

  return (
    <>
      <Header favoriteCount={favoriteIds.length} />
      <main>
        <Hero movie={movies[0]} searchText={searchText} onSearchChange={changeSearch} onSearchSubmit={() => setSubmittedText(searchText)} showClear={Boolean(searchText || searchQuery)} />
        <MovieList
          movies={movies}
          searchQuery={searchQuery}
          favoriteIds={favoriteIds}
          onToggleFavorite={toggleFavorite}
        />
        <Premieres movies={premiereMovies} simulateError={simulatePremiereError} />
      </main>
      <Toaster theme="dark" duration={3000} />
      <Footer />
    </>
  )
}
