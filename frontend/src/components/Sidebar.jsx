import React from 'react'
import { Drawer, List, ListItem, ListItemIcon, ListItemText, Toolbar } from '@mui/material'
import DashboardIcon from '@mui/icons-material/Dashboard'
import BuildIcon from '@mui/icons-material/Build'
import BugReportIcon from '@mui/icons-material/BugReport'
import TimelineIcon from '@mui/icons-material/Timeline'
import InventoryIcon from '@mui/icons-material/Inventory'
import { useNavigate } from 'react-router-dom'

const drawerWidth = 240

export default function Sidebar(){
  const navigate = useNavigate()
  const items = [
    {text:'Executive', icon:<DashboardIcon/>, to:'/executive'},
    {text:'Maintenance', icon:<BuildIcon/>, to:'/maintenance'},
    {text:'Quality', icon:<BugReportIcon/>, to:'/quality'},
    {text:'Forecast', icon:<TimelineIcon/>, to:'/forecast'},
    {text:'Inventory', icon:<InventoryIcon/>, to:'/inventory'}
  ]

  return (
    <Drawer variant="permanent" sx={{width:drawerWidth,['& .MuiDrawer-paper']:{width:drawerWidth,boxSizing:'border-box'}}}>
      <Toolbar />
      <List>
        {items.map(i=> (
          <ListItem button key={i.text} onClick={()=>navigate(i.to)}>
            <ListItemIcon>{i.icon}</ListItemIcon>
            <ListItemText primary={i.text} />
          </ListItem>
        ))}
      </List>
    </Drawer>
  )
}
