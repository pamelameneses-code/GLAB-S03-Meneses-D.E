import { useEffect, useState } from 'react'

export default function usePremieres(movies, simulateError) {
  const [result, setResult] = useState({ status: 'loading', movies: [] })

  useEffect(() => {
    const timer = setTimeout(() => {
      setResult(simulateError
        ? { status: 'error', movies: [] }
        : { status: 'success', movies })
    }, 900)
    return () => clearTimeout(timer)
  }, [movies, simulateError])

  return result
}
