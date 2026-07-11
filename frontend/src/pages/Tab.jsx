import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import './Tab.css'
import { Link } from 'react-router-dom'
import History from '../components/History'
import Lists from '../components/Lists'

const Tab = () => {
  const navigate = useNavigate()
  return (
    <div className='box'>
      <Link to='/' onClick={() => localStorage.removeItem('token')}>Выйти с аккаунта</Link>
      <Lists />
      <History />
    </div>
  )
}

export default Tab
