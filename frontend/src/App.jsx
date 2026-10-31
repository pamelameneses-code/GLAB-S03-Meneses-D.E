import { useEffect, useState } from 'react'
import Header from './components/Header/Header.jsx'
import Footer from './components/Footer/Footer.jsx'
import Hero from './components/Hero/Hero.jsx'
import MovieList from './components/MovieList/MovieList.jsx'
import { movies } from './data/movies.js'

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
  const [searchQuery, setSearchQuery] = useState('')

  useEffect(() => {
    try {
      localStorage.setItem(FAVORITES_KEY, JSON.stringify(favoriteIds))
    } catch {
      console.warn('Favorite movies could not be saved in this browser.')
    }
  }, [favoriteIds])

  function toggleFavorite(movieId) {
    setFavoriteIds((currentIds) => currentIds.includes(movieId)
      ? currentIds.filter((id) => id !== movieId)
      : [...currentIds, movieId])
  }

  return (
    <>
      <Header />
      <main>
        <Hero movie={movies[0]} onSearch={setSearchQuery} />
        <MovieList
          movies={movies}
          searchQuery={searchQuery}
          favoriteIds={favoriteIds}
          onToggleFavorite={toggleFavorite}
        />
      </main>
      <Footer />
    </>
  )
}
