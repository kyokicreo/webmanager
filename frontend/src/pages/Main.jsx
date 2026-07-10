import React from 'react'
import { Link } from 'react-router-dom'

const Main = () => {
  return (
    <div>
      <Link to="/login"><button>LOGIN</button></Link>
      <Link to="register"><button>REGISTER</button></Link>
    </div>
  )
}

export default Main
