//Homepage of recommendations for both guest users and account users

//Login information frontend
import React, { useState } from "react";
import axios from "axios";
import "./new-user.css";

function Homepage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, seterrorMessage] = useState("");
  const [successMessage, setsuccessMessage] = useState("");

  


  //what the user sees
  return (
    <div>
    <h1>Homepage</h1>

    </div>
  );
}

export default Homepage;
