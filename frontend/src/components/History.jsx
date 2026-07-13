import '../pages/Tab.css'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useState, useEffect } from 'react'



import React from 'react'

const History = () => {
    const navigate = useNavigate()
    const [histories, setHistories] = useState([])

    useEffect(() => {
        const token = localStorage.getItem('token')
        if (!token) return navigate('/')
        axios.get('http://localhost:8000/history/view', {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        },)
            .then(res => {
                setHistories(res.data)
            })
            .catch(() => { localStorage.removeItem('token'); navigate('/') })

    }, [])
    return (
        <div>
            <h2>История действий</h2>
            <table>
                <tr className='uppername'>
                    <td>Время создания UTC+5</td>
                    <td>Имя пользователя</td>
                    <td>Действие</td>
                    <td>Наименование директории</td>
                    <td>Статус</td>
                    <td>Ответ программы</td>
                </tr>
                {histories.map((item, index) => (
                    <tr key={index}>
                        <td>{item.timestamp}</td>
                        <td>{item.username}</td>
                        <td>{item.command}</td>
                        <td>{item.path}</td>
                        <td>{String(item.success)}</td>
                        <td>{item.message}</td>
                    </tr>
                ))}
            </table>
        </div>
    )
}

export default History
