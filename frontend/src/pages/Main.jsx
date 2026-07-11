import React, { useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'

const Main = () => {
  const navigate = useNavigate()

  useEffect(() => {
    const token = localStorage.getItem("token")
    if (token) return navigate('/tab')
  }, [])
  return (
    <div>
      <Link to="/login"><button>LOGIN</button></Link>
      <Link to="register"><button>REGISTER</button></Link>
    </div>
  )
}

export default Main
