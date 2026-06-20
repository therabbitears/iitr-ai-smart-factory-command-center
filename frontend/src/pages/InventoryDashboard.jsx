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
  LinearProgress,
  Chip
} from '@mui/material'
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts'
import { postInventoryRisk } from '../api/client'

export default function InventoryDashboard(){
  const [sku, setSku] = React.useState('SKU-1001')
  const [warehouse, setWarehouse] = React.useState('W-A')
  const [currentStock, setCurrentStock] = React.useState('340')
  const [reorderPoint, setReorderPoint] = React.useState('120')
  const [forecastCsv, setForecastCsv] = React.useState('100,110,95,120,105,115,130')
  const [loading, setLoading] = React.useState(false)
  const [error, setError] = React.useState('')
  const [result, setResult] = React.useState(null)

  function parseForecast(input) {
    return input
      .split(',')
      .map((x) => Number(x.trim()))
      .filter((x) => Number.isFinite(x) && x >= 0)
  }

  async function handleRisk() {
    setLoading(true)
    setError('')
    try {
      const forecast_next_horizon = parseForecast(forecastCsv)
      if (forecast_next_horizon.length === 0) {
        throw new Error('Please provide valid forecast values')
      }

      const data = await postInventoryRisk({
        sku,
        warehouse,
        current_stock: Number(currentStock),
        forecast_next_horizon,
        reorder_point: Number(reorderPoint)
      })
      setResult(data)
    } catch (e) {
      setError(e?.response?.data?.detail || e.message || 'Inventory risk prediction failed')
    } finally {
      setLoading(false)
    }
  }

  const bars = result
    ? [
        { key: 'Risk', value: Number((result.risk_score || 0).toFixed(3)) },
        { key: 'Recommended Order', value: Number((result.recommended_order || 0).toFixed(1)) }
      ]
    : []

  return (
    <div>
      <Typography variant="h5" gutterBottom>Inventory Dashboard</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} md={5}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 2 }}>Live Inventory Risk Input</Typography>
              <Stack spacing={2}>
                <TextField label="SKU" value={sku} onChange={(e) => setSku(e.target.value)} fullWidth />
                <TextField label="Warehouse" value={warehouse} onChange={(e) => setWarehouse(e.target.value)} fullWidth />
                <TextField label="Current Stock" type="number" value={currentStock} onChange={(e) => setCurrentStock(e.target.value)} fullWidth />
                <TextField label="Reorder Point" type="number" value={reorderPoint} onChange={(e) => setReorderPoint(e.target.value)} fullWidth />
                <TextField label="Forecast List (comma separated)" value={forecastCsv} onChange={(e) => setForecastCsv(e.target.value)} fullWidth multiline minRows={2} />
                <Button variant="contained" onClick={handleRisk} disabled={loading}>Compute Inventory Risk</Button>
                {loading ? <LinearProgress /> : null}
                {error ? <Alert severity="error">{error}</Alert> : null}
              </Stack>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={7}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 1 }}>Risk and Recommendation</Typography>
              {result ? (
                <Stack spacing={2}>
                  <Stack direction="row" spacing={1}>
                    <Chip label={`Risk ${(result.risk_score * 100).toFixed(1)}%`} color={result.risk_score > 0.6 ? 'error' : 'success'} />
                    <Chip label={`Order ${Number(result.recommended_order).toFixed(1)}`} color="primary" />
                  </Stack>
                  <Typography>{result.note}</Typography>
                  <ResponsiveContainer width="100%" height={260}>
                    <BarChart data={bars}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="key" />
                      <YAxis />
                      <Tooltip />
                      <Bar dataKey="value" fill="#1565c0" />
                    </BarChart>
                  </ResponsiveContainer>
                </Stack>
              ) : (
                <Typography color="text.secondary">Run risk computation to demo reorder recommendations.</Typography>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </div>
  )
}
