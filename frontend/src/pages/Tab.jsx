import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { Link } from 'react-router-dom'
import History from '../components/History'
import Lists from '../components/Lists'
import Admin from './Admin'
import Create from '../components/Create'
import Delete from '../components/Delete'
import TelegramLink from '../components/functions/TelegramLink'

const Tab = () => {
  const navigate = useNavigate()
  const [role, setRole] = useState('user')
  const [currentUserId, setCurrentUserId] = useState(null)

  useEffect(() => {
    axios.get('http://localhost:8000/auth/me', {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    })
      .then(res => {
        setRole(res.data.role)
        setCurrentUserId(res.data.id)
      })
      .catch(() => {})
  }, [])

  return (
    <div className='box'>
      <Link to='/' onClick={() => localStorage.removeItem('token')}>Выйти с аккаунта</Link>
      <Lists />
      <History />
      {(role === 'admin' || role === 'superadmin') && (
        <Admin role={role} currentUserId={currentUserId} />
      )}
      <Create />
      <Delete />
      <button className="tgbut" onClick={TelegramLink}>Войти с телеграм</button>
    </div>
  )
}

export default Tab