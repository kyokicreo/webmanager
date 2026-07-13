import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'


const Login = () => {
    const [value1, setValue1] = useState("")
    const [value2, setValue2] = useState("")
    const [output, setOutput] = useState("")
    const navigate = useNavigate()

    useEffect(() => {
        const token = localStorage.getItem("token")
        if (token) navigate('/tab')
    }, [])

    const LoginFunction = () => {
        const formData = new URLSearchParams();
        formData.append('username', value1);
        formData.append('password', value2);

        axios.post('http://localhost:8000/auth/login', formData, {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        })
            .then(response => {
                localStorage.setItem('token', response.data.access_token);
                navigate('/tab')
            })
            .catch(error => {
                setOutput("Аккаунт не найден")
            });
    }

    return (
        <div>
            <div>
                <input type="text" className="value1" placeholder='Введите имя' onChange={(e) => { setValue1(e.target.value) }} />
                <input type="text" className="value2" placeholder='Введите пароль' onChange={(e) => { setValue2(e.target.value) }} />
                <button onClick={LoginFunction}>Войти</button>
                <p>{output}</p>
                <Link to="/">Не входить</Link>

            </div>
        </div>
    )
}

export default Login
