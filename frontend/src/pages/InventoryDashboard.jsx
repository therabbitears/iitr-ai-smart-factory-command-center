import React from 'react'
import { Typography, Grid, Card, CardContent } from '@mui/material'

export default function InventoryDashboard(){
  return (
    <div>
      <Typography variant="h5" gutterBottom>Inventory Dashboard</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12}><Card><CardContent>Stock Levels, Risk Scores, Reorder Recommendations</CardContent></Card></Grid>
      </Grid>
    </div>
  )
}
