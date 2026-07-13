import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

const NotFound = () => {
  const navigate = useNavigate()
  useEffect(() => {
    const token = localStorage.getItem("token")
    if (token) return navigate('/tab')
    else return navigate('/')
  }, [])
  return (
    <div>

    </div>
  )
}

export default NotFound
