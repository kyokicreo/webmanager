import React, { useEffect, useState } from 'react'
import axios from 'axios'


const Lists = () => {
    const [list, setList] = useState([])

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/files/list', {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        })
            .then((res) => {
                setList(res.data.data)
            })
    }, [])
    return (
        <div>
            <h2>Директории в папке</h2>
            <table>
                <tr>
                    <td>Название директории</td>
                </tr>
                {list.map((item, index) => (
                    <tr key={index}>
                        <td>{item}</td>
                    </tr>
                ))}
            </table>
        </div>
    )
}

export default Lists
