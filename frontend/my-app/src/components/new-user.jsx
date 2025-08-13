//Login information frontend
import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import axios from "axios";
import "./new-user.css";

function NewUser() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, seterrorMessage] = useState("");
  const [successMessage, setsuccessMessage] = useState("");
  const [confirmPassword, setconfirmPassword] = useState("");
  const [checkPassword, setCheckPassword] = useState(true);

  const navigate = useNavigate();
  const [loginType, setLoginType] = useState("");

  // const checkDuplicateUsernames = async (event) => {
  //   event.preventDefault(); //means that the "default" field (empty strings) can't be submitted
  //   try {
  //     const response = await axios.post(
  //       `http://localhost:8000/check_multiple_usernames?new_username=${username}`
  //     ); //post_user for creating users
  //     seterrorMessage("");
  //     setsuccessMessage("SUCCESS");
  //   } catch (error) {
  //     seterrorMessage("ERROR");
  //     setsuccessMessage("");

  //     console.error("Error:", error);
  //   }
  // };

  const handleSubmit = async (event) => {
    event.preventDefault(); //means that the "default" field (empty strings) can't be submitted
    try {
      seterrorMessage("");

      const checkDuplicateUsernames = await axios.get(
        `http://localhost:8000/check_multiple_usernames?new_user_username=${username}`
      );

      

      if (password !== confirmPassword) {

        setCheckPassword(false);
        seterrorMessage("Passwords do not match");
        
      }
      else {

        
        console.log(checkDuplicateUsernames.data);

        if (checkDuplicateUsernames.data == false) {
          const response = await axios.post(
            `http://localhost:8000/post_user_and_pass?username=${username}&password=${password}`
          ); //post_user for creating users

          seterrorMessage("");
          setsuccessMessage("SUCCESS");
          navigate('/surveypage', { state: { loginType: "guestUser" } });
        }
        else {
          seterrorMessage("Username already exists, try a different one");
        }

      }
      
      } catch (error) {
        seterrorMessage("ERROR");
        setsuccessMessage("");

        console.error("Error:", error);
      }

      setUsername("");
      setPassword("");
      setconfirmPassword("");
  };

  //what the user sees
  return (
    <div>
    <h1>Create a New Account</h1>
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
      <input
        className="login-page-password"
        type="password"
        value={confirmPassword || ""}
        onChange={(e) => setconfirmPassword(e.target.value)}
        placeholder="Confirm Password"
      />
      <button type="submit" className="login-page-submit-button">
        Create Account
      </button>
      {errorMessage && <div>{errorMessage}</div>}
      {successMessage && <div>{successMessage}</div>}
    </form>
    </div>
  );
}

export default NewUser;
