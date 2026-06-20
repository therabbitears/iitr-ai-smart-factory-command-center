import axios from 'axios'

const baseURL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL,
  timeout: 10000
})

export async function postMaintenance(payload) {
  const { data } = await api.post('/api/predict-maintenance', payload)
  return data
}

export async function postQuality(payload) {
  const { data } = await api.post('/api/predict-quality', payload)
  return data
}

export async function postForecast(payload) {
  const { data } = await api.post('/api/forecast-demand', payload)
  return data
}

export async function postInventoryRisk(payload) {
  const { data } = await api.post('/api/inventory-risk', payload)
  return data
}

export default api
