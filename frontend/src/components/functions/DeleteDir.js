import React from 'react'
import axios from 'axios'

const DeleteDir = (name) => {
    if (!name) return use("Заполните поле")

    axios.post('http://127.0.0.1:8000/files/delete',
        { path: name },
        { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } }
    )
        .then(() => {
            window.location.reload()
        })
        .catch(() => alert("Ошибка подключения"))
}

export default DeleteDir
