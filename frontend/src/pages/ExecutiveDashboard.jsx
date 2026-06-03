import React from 'react'
import { Card, CardContent, Typography, Grid } from '@mui/material'
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts'

const sample = Array.from({length:30}).map((_,i)=>({date:`Day ${i+1}`, value: Math.round(100 + Math.sin(i/5)*20 + Math.random()*10)}))

export default function ExecutiveDashboard(){
  return (
    <div>
      <Typography variant="h5" gutterBottom>Executive Dashboard</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6">Summary KPI</Typography>
              <ResponsiveContainer width="100%" height={200}>
                <LineChart data={sample}><XAxis dataKey="date"/><YAxis/><Tooltip/><Line type="monotone" dataKey="value" stroke="#1976d2"/></LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6">Forecast Overview</Typography>
              <Typography>Placeholder for summary cards and metric tiles.</Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </div>
  )
}
