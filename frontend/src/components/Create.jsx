import React, { useState } from 'react'
import CreateDir from './functions/CreateDir'

const Create = () => {
    const [ dir, setDir ] = useState('')

    return (
        <div>
            <h3>Создание папки</h3>
            <input type="text" name="" id="" placeholder='Название папки' onChange={e => { setDir(e.target.value) }} />
            <button onClick={() => CreateDir(dir) }>Создать папку</button>
        </div>
    )
}

export default Create
