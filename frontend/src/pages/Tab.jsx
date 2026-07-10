import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

const Tab = () => {
  const token = localStorage.getItem('token')
  if(!token) return navigate('/')
  const navigate = useNavigate()
  const [ histories, setHistories ] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/history/', {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    }, [])
      .then(res => {
        setHistories(res.data)
      })
      .catch(() => alert("Покиньте сайт"))

  })
  return (
    <div>
      {/* <table>
        <tr>
          <td>Название</td>
          <td>Оригинальное название</td>
          <td>Год</td>
        </tr>
        <tr>
          <td>Человек-паук: Возвращение домой</td>
          <td>Spider-Man: Homecoming</td>
          <td>2017</td>
        </tr>
        <tr>
          <td>Человек-паук: Вдали от дома</td>
          <td>Spider-Man: Far From Home</td>
          <td>2019</td>
        </tr>
        <tr>
          <td>Человек-паук: Нет пути домой</td>
          <td>Spider-Man: No Way Home</td>
          <td>2021</td>
        </tr>
      </table> */}
      <table>
        {histories.map((item) => (
          <tr>
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

export default Tab
