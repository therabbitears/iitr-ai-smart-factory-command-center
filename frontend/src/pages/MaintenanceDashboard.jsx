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
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts'
import { postMaintenance } from '../api/client'

export default function MaintenanceDashboard(){
  const [deviceId, setDeviceId] = React.useState('machine-01')
  const [vibration, setVibration] = React.useState('0.45')
  const [temp, setTemp] = React.useState('72')
  const [pressure, setPressure] = React.useState('1.2')
  const [loading, setLoading] = React.useState(false)
  const [error, setError] = React.useState('')
  const [result, setResult] = React.useState(null)
  const [history, setHistory] = React.useState([])

  async function handlePredict() {
    setLoading(true)
    setError('')
    try {
      const payload = {
        device_id: deviceId,
        sensors: [
          {
            sensor_id: 'sensor-pack-1',
            timestamp: new Date().toISOString(),
            readings: {
              vibration: Number(vibration),
              temp: Number(temp),
              pressure: Number(pressure)
            }
          }
        ]
      }

      const data = await postMaintenance(payload)
      setResult(data)
      setHistory((prev) => [...prev.slice(-14), {
        t: new Date().toLocaleTimeString(),
        risk: Number((data.failure_risk || 0).toFixed(3))
      }])
    } catch (e) {
      setError(e?.response?.data?.detail || e.message || 'Prediction failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <Typography variant="h5" gutterBottom>Maintenance Dashboard</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} md={5}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 2 }}>Live Maintenance Prediction</Typography>
              <Stack spacing={2}>
                <TextField label="Device ID" value={deviceId} onChange={(e) => setDeviceId(e.target.value)} fullWidth />
                <TextField label="Vibration" type="number" value={vibration} onChange={(e) => setVibration(e.target.value)} fullWidth />
                <TextField label="Temperature" type="number" value={temp} onChange={(e) => setTemp(e.target.value)} fullWidth />
                <TextField label="Pressure" type="number" value={pressure} onChange={(e) => setPressure(e.target.value)} fullWidth />
                <Button variant="contained" onClick={handlePredict} disabled={loading}>Predict Risk</Button>
                {loading && <LinearProgress />}
                {error ? <Alert severity="error">{error}</Alert> : null}
              </Stack>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={7}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 1 }}>Prediction Output</Typography>
              {result ? (
                <Stack spacing={2}>
                  <Typography><strong>Device:</strong> {result.device_id}</Typography>
                  <Typography><strong>Failure Risk:</strong> {(result.failure_risk * 100).toFixed(1)}%</Typography>
                  <LinearProgress variant="determinate" value={Math.min(100, Math.max(0, (result.failure_risk || 0) * 100))} />
                  <Stack direction="row" spacing={1}>
                    <Chip label={result.failure_risk > 0.7 ? 'High Risk' : 'Normal'} color={result.failure_risk > 0.7 ? 'error' : 'success'} />
                    {result.eta_hours ? <Chip label={`ETA ${result.eta_hours}h`} color="warning" /> : null}
                  </Stack>
                </Stack>
              ) : (
                <Typography color="text.secondary">Enter values and click Predict Risk to run a live demo.</Typography>
              )}
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 1 }}>Recent Risk Trend</Typography>
              <ResponsiveContainer width="100%" height={260}>
                <LineChart data={history}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="t" />
                  <YAxis domain={[0, 1]} />
                  <Tooltip />
                  <Line type="monotone" dataKey="risk" stroke="#d32f2f" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </div>
  )
}
