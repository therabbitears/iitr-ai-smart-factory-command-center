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
import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { postQuality } from '../api/client'

export default function QualityDashboard(){
  const [batchId, setBatchId] = React.useState('batch-2026-01')
  const [width, setWidth] = React.useState('10.2')
  const [height, setHeight] = React.useState('5.1')
  const [hardness, setHardness] = React.useState('7.3')
  const [loading, setLoading] = React.useState(false)
  const [error, setError] = React.useState('')
  const [result, setResult] = React.useState(null)

  const pie = React.useMemo(() => {
    if (!result) return []
    return [
      { name: 'Pass', value: Math.round((result.pass_rate || 0) * 100) },
      { name: 'Fail', value: Math.round((1 - (result.pass_rate || 0)) * 100) }
    ]
  }, [result])

  async function handlePredict() {
    setLoading(true)
    setError('')
    try {
      const data = await postQuality({
        batch_id: batchId,
        metrics: {
          width: Number(width),
          height: Number(height),
          hardness: Number(hardness)
        }
      })
      setResult(data)
    } catch (e) {
      setError(e?.response?.data?.detail || e.message || 'Quality prediction failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <Typography variant="h5" gutterBottom>Quality Dashboard</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} md={5}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 2 }}>Live Batch Quality Check</Typography>
              <Stack spacing={2}>
                <TextField label="Batch ID" value={batchId} onChange={(e) => setBatchId(e.target.value)} fullWidth />
                <TextField label="Width" type="number" value={width} onChange={(e) => setWidth(e.target.value)} fullWidth />
                <TextField label="Height" type="number" value={height} onChange={(e) => setHeight(e.target.value)} fullWidth />
                <TextField label="Hardness" type="number" value={hardness} onChange={(e) => setHardness(e.target.value)} fullWidth />
                <Button variant="contained" onClick={handlePredict} disabled={loading}>Run Quality Prediction</Button>
                {error ? <Alert severity="error">{error}</Alert> : null}
              </Stack>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={7}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 1 }}>Pass/Fail Distribution</Typography>
              {result ? (
                <>
                  <Stack direction="row" spacing={1} sx={{ mb: 1 }}>
                    <Chip label={`Pass Rate ${(result.pass_rate * 100).toFixed(1)}%`} color="success" />
                    <Chip label={`Defects ${result.defects_expected}`} color="warning" />
                  </Stack>
                  <ResponsiveContainer width="100%" height={280}>
                    <PieChart>
                      <Pie data={pie} dataKey="value" nameKey="name" outerRadius={95}>
                        <Cell fill="#2e7d32" />
                        <Cell fill="#d32f2f" />
                      </Pie>
                      <Tooltip />
                      <Legend />
                    </PieChart>
                  </ResponsiveContainer>
                </>
              ) : (
                <Typography color="text.secondary">Enter measurements and run a live batch check.</Typography>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </div>
  )
}
