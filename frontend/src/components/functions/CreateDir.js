import React from 'react'
import axios from 'axios'

const CreateDir = (name) => {
    if (!name) return use("Заполните поле")

    axios.post('http://127.0.0.1:8000/files/create',
        { path: name },
        { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } }
    )
        .then(() => {
            window.location.reload()
        })
        .catch(() => alert("Ошибка подключения"))

}

export default CreateDir
