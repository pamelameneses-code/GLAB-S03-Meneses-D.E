import { useEffect, useState } from 'react'
import { createExam, deleteExam, listExams } from '../../api/exams.js'
import './Exams.css'

function ExamForm() {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [errors, setErrors] = useState({})
  const [saving, setSaving] = useState(false)

  async function submit(event) {
    event.preventDefault()
    setSaving(true)
    setErrors({})
    try {
      await createExam({ title, description })
      window.location.hash = 'exams'
    } catch (error) {
      setErrors(error.response?.status === 400
        ? error.response.data
        : { detail: 'No se pudo guardar el examen. Comprueba que Django esté en ejecución e inténtalo de nuevo.' })
    } finally {
      setSaving(false)
    }
  }

  return (
    <>
      <h1>Nuevo examen</h1>
      <form onSubmit={submit} noValidate>
        <label htmlFor="exam-title">Título (obligatorio)</label>
        <input id="exam-title" value={title} onChange={(event) => setTitle(event.target.value)}
          required maxLength={200} aria-invalid={Boolean(errors.title)} aria-describedby="exam-title-error" />
        <div id="exam-title-error" role="alert">{errors.title?.join(' ')}</div>
        <label htmlFor="exam-description">Descripción</label>
        <textarea id="exam-description" value={description} onChange={(event) => setDescription(event.target.value)} />
        {errors.description && <p role="alert">{errors.description.join(' ')}</p>}
        {errors.detail && <p role="alert">{errors.detail}</p>}
        <div className="exam-actions">
          <button disabled={saving}>{saving ? 'Guardando…' : 'Guardar examen'}</button>
          <a href="#exams">Volver al listado</a>
        </div>
      </form>
    </>
  )
}

function ExamList() {
  const [result, setResult] = useState({ status: 'loading' })
  const [request, setRequest] = useState(0)
  const [deletingId, setDeletingId] = useState(null)
  const [deleteError, setDeleteError] = useState('')

  function refresh() {
    setResult({ status: 'loading' })
    setRequest((current) => current + 1)
  }

  useEffect(() => {
    const controller = new AbortController()

    async function load() {
      try {
        const exams = await listExams(controller.signal)
        if (!controller.signal.aborted) setResult({ status: 'success', exams })
      } catch {
        if (!controller.signal.aborted) setResult({ status: 'error' })
      }
    }

    void load()
    return () => controller.abort()
  }, [request])

  async function remove(exam) {
    if (!window.confirm('¿Eliminar el examen «' + exam.title + '»?')) return
    setDeleteError('')
    setDeletingId(exam.id)
    try {
      await deleteExam(exam.id)
      refresh()
    } catch (error) {
      if (error.response?.status === 404) {
        refresh()
      } else {
        setDeleteError('No se pudo eliminar el examen. Comprueba la conexión con Django e inténtalo de nuevo.')
      }
    } finally {
      setDeletingId(null)
    }
  }

  return (
    <>
      <div className="exam-actions">
        <h1>Exámenes</h1>
        <a href="#exams/new">Nuevo examen</a>
      </div>
      {result.status === 'loading' && (
        <div role="status">
          <p>Cargando exámenes…</p>
          <div className="exam-skeleton" aria-hidden="true" />
        </div>
      )}
      {result.status === 'error' && (
        <div className="exam-alert" role="alert">
          <p>No se pudo conectar con la API de exámenes. Comprueba que Django esté en ejecución y que autorice el origen de esta página.</p>
          <button onClick={refresh}>Reintentar</button>
        </div>
      )}
      {deleteError && <p className="exam-alert" role="alert">{deleteError}</p>}
      {result.status === 'success' && (
        result.exams.length ? (
          <div className="exam-table">
            <table>
              <caption>Exámenes registrados</caption>
              <thead><tr><th scope="col">Título</th><th scope="col">Descripción</th><th scope="col">Acciones</th></tr></thead>
              <tbody>
                {result.exams.map((exam) => (
                  <tr key={exam.id}>
                    <th scope="row">{exam.title}</th>
                    <td>{exam.description || 'Sin descripción'}</td>
                    <td><button disabled={deletingId !== null} onClick={() => remove(exam)}
                      aria-label={'Eliminar ' + exam.title}>{deletingId === exam.id ? 'Eliminando…' : 'Eliminar'}</button></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : <p role="status">Aún no hay exámenes. Crea uno para empezar.</p>
      )}
    </>
  )
}

export default function Exams({ showForm }) {
  return <section className="exams">{showForm ? <ExamForm /> : <ExamList />}</section>
}
