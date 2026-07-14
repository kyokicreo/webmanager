import axios from 'axios'

import React from 'react'

const TelegramLink = () => {
    axios.post('http://127.0.0.1:8000/telegram/link-code', {}, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    })
        .then((res) => {
            window.open(res.data.link, '_blank')
        })
        .catch(() => alert('Ошибка получения ссылки'))
}

export default TelegramLink
