import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Main from './pages/Main'
import Tab from './pages/Tab'
import Login from './pages/Login'
import Register from './pages/Register'

const App = () => {
  return (
    <Routes>
      <Route path='/' element={<Main />} />
      <Route path='/tab' element={<Tab />} />
      <Route path='/login' element={<Login />} />
      <Route path='/register' element={<Register />} />
    </Routes>
  )
}

export default App
