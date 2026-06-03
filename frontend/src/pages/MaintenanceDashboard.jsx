import React from 'react'
import { Typography, Grid, Card, CardContent } from '@mui/material'

export default function MaintenanceDashboard(){
  return (
    <div>
      <Typography variant="h5" gutterBottom>Maintenance Dashboard</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} md={6}><Card><CardContent>Active Alarms / Devices</CardContent></Card></Grid>
        <Grid item xs={12} md={6}><Card><CardContent>Risk Heatmap / Upcoming Workorders</CardContent></Card></Grid>
      </Grid>
    </div>
  )
}
