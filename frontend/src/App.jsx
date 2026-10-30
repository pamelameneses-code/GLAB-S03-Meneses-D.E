import Header from './components/Header/Header.jsx'
import Footer from './components/Footer/Footer.jsx'
import Hero from './components/Hero/Hero.jsx'
import MovieList from './components/MovieList/MovieList.jsx'
import { movies } from './data/movies.js'

export default function App() {
  return (
    <>
      <Header />
      <main>
        <Hero movie={movies[0]} />
        <MovieList movies={movies} />
      </main>
      <Footer />
    </>
  )
}
