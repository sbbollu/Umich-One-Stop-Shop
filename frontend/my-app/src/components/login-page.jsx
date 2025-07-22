//Login information frontend
import React, { useState } from "react";
import axios from 'axios';

function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [survey, setSurvey] = useState("");
    const [errorMessage, seterrorMessage] = useState("");
    const [successMessage, setsuccessMessage] = useState("");

    const handleSubmit = async (event) => {
    event.preventDefault(); //can't submit empty field
    try {
        const response = await axios.post("http://localhost:8000/post_user_and_pass", {
            username: username,
            password: password
        }); //post_user for creating users
      
        seterrorMessage('');
        setsuccessMessage('SUCCESS');
    } 
    catch (error) {
        seterrorMessage('ERROR');
        setsuccessMessage('');
        
        console.error("Error:", error);
    }
  };

  //what the user sees
  return (
    <form onSubmit={handleSubmit}>
      <input className='input'
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input className='input'
        type="text"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      {/* <input className='input'
        type="text"
        value={survey}
        onChange={(e) => setSurvey(e.target.value)}
        placeholder="Survey"
      /> */}
      <button type="submit" className="button">Login</button>
        {errorMessage && <div>{errorMessage}</div>}
        {successMessage && <div>{successMessage}</div>}
    </form>
  );
}

export default Login;