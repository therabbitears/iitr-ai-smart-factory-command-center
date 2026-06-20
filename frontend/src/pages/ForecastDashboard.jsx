import React from 'react'
import {
  Typography,
  Grid,
  Card,
  CardContent,
  TextField,
  Button,
  Stack,
  Alert,
  Chip
} from '@mui/material'
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, Legend } from 'recharts'
import { postForecast } from '../api/client'

export default function ForecastDashboard(){
  const [storeId, setStoreId] = React.useState('S1')
  const [itemId, setItemId] = React.useState('I1')
  const [horizon, setHorizon] = React.useState('14')
  const [baseDemand, setBaseDemand] = React.useState('100')
  const [loading, setLoading] = React.useState(false)
  const [error, setError] = React.useState('')
  const [result, setResult] = React.useState(null)
  const [plotData, setPlotData] = React.useState([])

  function buildHistory(base) {
    const n = 14
    return Array.from({ length: n }).map((_, i) => {
      const d = new Date()
      d.setDate(d.getDate() - (n - i))
      return {
        date: d.toISOString(),
        demand: Math.max(1, Math.round(base + Math.sin(i / 2) * 8 + (Math.random() * 6 - 3)))
      }
    })
  }

  async function handleForecast() {
    setLoading(true)
    setError('')
    try {
      const history = buildHistory(Number(baseDemand))
      const data = await postForecast({
        store_id: storeId,
        item_id: itemId,
        history,
        horizon: Number(horizon)
      })
      setResult(data)

      const historical = history.map((h, idx) => ({
        step: `H${idx + 1}`,
        historical: h.demand,
        forecast: null
      }))
      const forecasted = data.forecast.map((v, idx) => ({
        step: `F${idx + 1}`,
        historical: null,
        forecast: Number(v.toFixed(2))
      }))
      setPlotData([...historical, ...forecasted])
    } catch (e) {
      setError(e?.response?.data?.detail || e.message || 'Forecast failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <Typography variant="h5" gutterBottom>Forecast Dashboard</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 2 }}>Live Forecast Input</Typography>
              <Stack spacing={2}>
                <TextField label="Store ID" value={storeId} onChange={(e) => setStoreId(e.target.value)} fullWidth />
                <TextField label="Item ID" value={itemId} onChange={(e) => setItemId(e.target.value)} fullWidth />
                <TextField label="Forecast Horizon" type="number" value={horizon} onChange={(e) => setHorizon(e.target.value)} fullWidth />
                <TextField label="Base Daily Demand" type="number" value={baseDemand} onChange={(e) => setBaseDemand(e.target.value)} fullWidth />
                <Button variant="contained" onClick={handleForecast} disabled={loading}>Generate Forecast</Button>
                {error ? <Alert severity="error">{error}</Alert> : null}
              </Stack>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={8}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 1 }}>Historical + Forecast Curve</Typography>
              {result ? (
                <>
                  <Stack direction="row" spacing={1} sx={{ mb: 1 }}>
                    <Chip label={`Method: ${result.method}`} color="primary" />
                    <Chip label={`Horizon: ${result.horizon} days`} color="secondary" />
                  </Stack>
                  <ResponsiveContainer width="100%" height={300}>
                    <LineChart data={plotData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="step" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Line type="monotone" dataKey="historical" stroke="#2e7d32" strokeWidth={2} dot={false} />
                      <Line type="monotone" dataKey="forecast" stroke="#1565c0" strokeWidth={2} dot={false} />
                    </LineChart>
                  </ResponsiveContainer>
                </>
              ) : (
                <Typography color="text.secondary">Run forecast to visualize demand trajectory.</Typography>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </div>
  )
}
