import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { CssBaseline, Box } from '@mui/material'
import Header from './components/Header'
import Sidebar from './components/Sidebar'
import ExecutiveDashboard from './pages/ExecutiveDashboard'
import MaintenanceDashboard from './pages/MaintenanceDashboard'
import QualityDashboard from './pages/QualityDashboard'
import ForecastDashboard from './pages/ForecastDashboard'
import InventoryDashboard from './pages/InventoryDashboard'
import { AuthProvider } from './auth/AuthProvider'

export default function App(){
  return (
    <AuthProvider>
      <CssBaseline />
      <Header />
      <Box sx={{display:'flex'}}>
        <Sidebar />
        <Box component="main" sx={{flexGrow:1, p:2}} className="app-content">
          <Routes>
            <Route path="/" element={<Navigate to="/executive" replace />} />
            <Route path="/executive" element={<ExecutiveDashboard/>} />
            <Route path="/maintenance" element={<MaintenanceDashboard/>} />
            <Route path="/quality" element={<QualityDashboard/>} />
            <Route path="/forecast" element={<ForecastDashboard/>} />
            <Route path="/inventory" element={<InventoryDashboard/>} />
          </Routes>
        </Box>
      </Box>
    </AuthProvider>
  )
}
