import React, { useState } from 'react'
import DeleteDir from './functions/DeleteDir'

const Delete = () => {
    const [ dir, setDir ] = useState('')
    return (
        <div>
            <h3>Удаление папки</h3>
            <input type="text" name="" id="" placeholder='Название папки' onChange={e => { setDir(e.target.value) }} />
            <button onClick={() => DeleteDir(dir)}>Удалить папку</button>
        </div>
    )
}

export default Delete
