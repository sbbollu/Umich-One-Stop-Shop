//Homepage of recommendations for both guest users and account users

//Login information frontend
import React, { useState } from "react";
import { useLocation } from "react-router-dom";
import newUser from "./login-page";
import guestUser from "./login-page";
import returningUser from "./login-page";
import axios from "axios";
import "./new-user.css";

function Homepage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, seterrorMessage] = useState("");
  const [successMessage, setsuccessMessage] = useState("");

  const location = useLocation();
  const loginType = location.state?.loginType || "";
  let content;
  
  if (loginType === "guestUser") {
    content = <p>Welcome, Guest!</p>;
  } 
  else if (loginType === "returningUser") {
    content = <p>Welcome back!</p>;
  } 
  //for users that just created a new account
  else if (loginType === "newUser") {
    content = <p>Welcome new user!</p>;
  }
  else{
    content = <p>Error</p>;
  }


  //what the user sees
  return (

    <div>
      <h1>Homepage</h1>
      {content}
    </div>

  );
}

export default Homepage;
