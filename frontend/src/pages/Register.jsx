import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

const Register = () => {
    const [value1, setValue1] = useState("")
    const [value2, setValue2] = useState("")
    const [output, setOutput] = useState("")

    const RegisterFunction = () => {
        if(!value1 || !value2) {
            setOutput("Заполни поля")
            return
        }
        axios
            .post("http://127.0.0.1:8000/auth/register", {
                username: value1,
                password: value2,
            })
        .then(() => {
            setOutput("Регистрация успешна")
        })
        .catch(() => {
            setOutput("Имя занято")
        })
        
    }
    return (
        <div>
            <input type="text" className="value1" placeholder='Введите имя' onChange={(e) => { setValue1(e.target.value) }} />
            <input type="text" className="value2" placeholder='Введите пароль' onChange={(e) => { setValue2(e.target.value) }} />
            <button onClick={RegisterFunction}>Register</button>
            <p>{output}</p>
            <Link to="/">Не регистрироваться</Link>
        </div>
    )
}

export default Register
