import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/',
  timeout: 8000,
})

export async function listExams(signal) {
  const exams = []
  let page = 'exams/'

  while (page) {
    const { data } = await api.get(page, { signal })
    exams.push(...data.results)
    page = data.next ? 'exams/' + new URL(data.next).search : null
  }

  return exams
}

export async function createExam(exam) {
  const { data } = await api.post('exams/', exam)
  return data
}

export async function deleteExam(id) {
  await api.delete('exams/' + id + '/')
}
