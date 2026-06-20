import React from 'react'
import { Card, CardContent, Typography, Grid, Chip, Stack } from '@mui/material'
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  CartesianGrid,
  Legend
} from 'recharts'

const trend = Array.from({ length: 14 }).map((_, i) => ({
  day: `D${i + 1}`,
  oee: Math.round(72 + Math.sin(i / 2) * 6 + Math.random() * 3),
  output: Math.round(180 + Math.sin(i / 3) * 20 + Math.random() * 10)
}))

const riskBars = [
  { module: 'Maintenance', score: 0.34 },
  { module: 'Quality', score: 0.22 },
  { module: 'Forecast', score: 0.18 },
  { module: 'Inventory', score: 0.41 }
]

const mix = [
  { name: 'Healthy', value: 72 },
  { name: 'Warning', value: 20 },
  { name: 'Critical', value: 8 }
]

const COLORS = ['#2e7d32', '#ed6c02', '#d32f2f']

function KpiCard({ title, value, delta, color = 'primary' }) {
  return (
    <Card>
      <CardContent>
        <Typography variant="body2" color="text.secondary">{title}</Typography>
        <Typography variant="h4" sx={{ mt: 1 }}>{value}</Typography>
        <Chip size="small" color={color} label={delta} sx={{ mt: 1 }} />
      </CardContent>
    </Card>
  )
}

export default function ExecutiveDashboard(){
  return (
    <div>
      <Stack direction="row" justifyContent="space-between" alignItems="center" sx={{ mb: 2 }}>
        <Typography variant="h5">Executive Dashboard</Typography>
        <Chip color="success" label="Live Demo Mode" />
      </Stack>

      <Grid container spacing={2}>
        <Grid item xs={12} sm={6} md={3}><KpiCard title="Plant OEE" value="78.4%" delta="+2.1% WoW" color="success" /></Grid>
        <Grid item xs={12} sm={6} md={3}><KpiCard title="Prediction Volume" value="12,480" delta="+8.4% today" /></Grid>
        <Grid item xs={12} sm={6} md={3}><KpiCard title="Avg API Latency" value="132ms" delta="-14ms" color="success" /></Grid>
        <Grid item xs={12} sm={6} md={3}><KpiCard title="Error Rate" value="0.8%" delta="Within SLO" color="success" /></Grid>

        <Grid item xs={12} md={8}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 1 }}>Summary KPI Trends</Typography>
              <ResponsiveContainer width="100%" height={280}>
                <LineChart data={trend}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="day"/>
                  <YAxis/>
                  <Tooltip/>
                  <Legend />
                  <Line type="monotone" dataKey="oee" stroke="#1565c0" strokeWidth={2} name="OEE %" />
                  <Line type="monotone" dataKey="output" stroke="#2e7d32" strokeWidth={2} name="Output" />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 1 }}>Fleet Health Mix</Typography>
              <ResponsiveContainer width="100%" height={280}>
                <PieChart>
                  <Pie data={mix} dataKey="value" nameKey="name" outerRadius={90}>
                    {mix.map((entry, idx) => <Cell key={entry.name} fill={COLORS[idx % COLORS.length]} />)}
                  </Pie>
                  <Tooltip />
                  <Legend />
                </PieChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" sx={{ mb: 1 }}>Module Risk Snapshot</Typography>
              <ResponsiveContainer width="100%" height={260}>
                <BarChart data={riskBars}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="module"/>
                  <YAxis domain={[0, 1]} />
                  <Tooltip />
                  <Bar dataKey="score" fill="#6a1b9a" />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </div>
  )
}
