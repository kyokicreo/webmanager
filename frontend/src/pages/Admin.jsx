import React, { useEffect, useState } from 'react'
import axios from 'axios'

const Admin = ({ role, currentUserId }) => {
    const [users, setUsers] = useState([])
    const [newPassword, setNewPassword] = useState({})

    const loadUsers = () => {
        axios.get('http://localhost:8000/admin/users', {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        })
            .then(res => setUsers(res.data))
            .catch(() => { })
    }

    useEffect(() => {
        loadUsers()
    }, [])

    const handleDelete = (userId) => {
        if (!confirm('Точно удалить этого пользователя?')) return

        axios.delete(`http://localhost:8000/admin/users/${userId}`, {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        })
            .then(() => loadUsers())
            .catch(err => alert(err.response?.data?.detail || 'Ошибка удаления'))
    }

    const handleResetPassword = (userId) => {
        const password = newPassword[userId]
        if (!password) {
            alert('Введите новый пароль')
            return
        }

        axios.post(`http://localhost:8000/admin/users/${userId}/reset-password?new_password=${password}`, null, {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        })
            .then(() => {
                alert('Пароль изменён')
                setNewPassword({ ...newPassword, [userId]: '' })
            })
            .catch(err => alert(err.response?.data?.detail || 'Ошибка сброса пароля'))
    }

    const handlePromote = (userId) => {
        axios.post(`http://localhost:8000/admin/users/${userId}/promote`, null, {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        })
            .then(() => loadUsers())
            .catch(err => alert(err.response?.data?.detail || 'Ошибка назначения'))
    }

    const canManage = (targetUser) => {
        if (targetUser.id === currentUserId) return false
        if (targetUser.role === 'user') return true
        return role === 'superadmin'
    }

    const canDelete = (targetUser) => {
        return role === 'superadmin' && targetUser.id !== currentUserId
    }
    return (
        <div>
            <h2>Панель администратора — пользователи</h2>
            <table>
                <thead>
                    <tr>
                        <td>ID</td>
                        <td>Имя пользователя</td>
                        <td>Роль</td>
                        <td>Дата регистрации</td>
                        <td>Новый пароль</td>
                        <td>Действия</td>
                    </tr>
                </thead>
                <tbody>
                    {users.map((user) => (
                        <tr key={user.id}>
                            <td>{user.id}</td>
                            <td>{user.username}</td>
                            <td>{user.role}</td>
                            <td>{user.created_at}</td>
                            <td>
                                {canManage(user) && (
                                    <input
                                        type="text"
                                        value={newPassword[user.id] || ''}
                                        onChange={(e) => setNewPassword({ ...newPassword, [user.id]: e.target.value })}
                                    />
                                )}
                            </td>
                            <td>
                                {canManage(user) && (
                                    <button onClick={() => handleResetPassword(user.id)}>Сбросить пароль</button>
                                )}
                                {canDelete(user) && (
                                    <button onClick={() => handleDelete(user.id)}>Удалить</button>
                                )}
                                {role === 'superadmin' && user.role === 'user' && (
                                    <button onClick={() => handlePromote(user.id)}>Сделать админом</button>
                                )}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default Admin