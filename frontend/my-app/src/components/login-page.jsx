//Login information frontend
import React, { useState } from "react";
import axios from "axios";
import "./login-page.css";
import { useNavigate } from 'react-router-dom';

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, seterrorMessage] = useState("");
  const [successMessage, setsuccessMessage] = useState("");
  const navigate = useNavigate();

  const goToNewUser = () => {
      navigate('/new_user'); 
  };

  const goToHomepage = () => {
      navigate('/homepage'); 
  };

  const handleSubmit = async (event) => {
    event.preventDefault(); //means that the "default" field (empty strings) can't be submitted
    try {
      const response = await axios.post(
        `http://localhost:8000/post_user_and_pass?username=${username}&password=${password}`
      ); //post_user for creating users
      seterrorMessage("");
      setsuccessMessage("SUCCESS");
    } catch (error) {
      seterrorMessage("ERROR");
      setsuccessMessage("");

      console.error("Error:", error);
    }
  };

  //what the user sees
  return (
    <div>
    <h1>Welcome to Umich One-Stop-Shop</h1>
    <form onSubmit={handleSubmit}>
      <input
        className="login-page-username"
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        className="login-page-password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit" className="login-page-submit-button">
        Login
      </button>
      <button type="submit" className="login-page-submit-button" onClick = {goToHomepage}>
        Continue as a Guest
      </button>
      {errorMessage && <div>{errorMessage}</div>}
      {successMessage && <div>{successMessage}</div>}
      <button type="button" className="login-page-submit-button" onClick = {goToNewUser}>Create New Account</button>
    </form>
    </div>
  );
}

export default Login;
