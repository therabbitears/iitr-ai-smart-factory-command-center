import React from 'react'
import { Typography, Grid, Card, CardContent } from '@mui/material'

export default function QualityDashboard(){
  return (
    <div>
      <Typography variant="h5" gutterBottom>Quality Dashboard</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12}><Card><CardContent>Quality Metrics & Defect Trends</CardContent></Card></Grid>
      </Grid>
    </div>
  )
}
