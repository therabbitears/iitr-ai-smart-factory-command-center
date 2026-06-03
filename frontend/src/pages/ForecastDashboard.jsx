import React from 'react'
import { Typography, Grid, Card, CardContent } from '@mui/material'

export default function ForecastDashboard(){
  return (
    <div>
      <Typography variant="h5" gutterBottom>Forecast Dashboard</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12}><Card><CardContent>Demand Forecasts and Model Performance</CardContent></Card></Grid>
      </Grid>
    </div>
  )
}
