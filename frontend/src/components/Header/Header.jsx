import './Header.css'
export default function Header() {
  return (
    <header className="site-header">
      <a className="brand" href="#home"><span aria-hidden="true">◉</span> ÓRBITA <small>CINE</small></a>
      <nav aria-label="Navegación principal">
        <a href="#home">Inicio</a><a href="#movies">Cartelera</a><a href="#contact">Contacto</a>
      </nav>
    </header>
  )
}
