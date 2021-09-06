import { useState } from "react"

export default function Home() {

  const [value, setValue] = useState([])
  const [username, setUsername] = useState('')
  const [age, setAge] = useState('')
  const [email, setEmail] = useState('')

  
  const handleOnClick = async () => {
    const res = await fetch('http://192.168.1.30:5000/')
    const data = await res.json()
    console.log(data)
    setUsername( data.username )
    setAge( data.age )
    setEmail( data.email )
  }

  return (
    <div>
      <input type="button" value="click" onClick={handleOnClick} />
      <h1>username is {username}</h1>
      <h1>age is {age}</h1>
      <h1>email is {email}</h1>
    </div>
  )
}
