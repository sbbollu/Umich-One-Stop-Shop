import logo from "./logo.svg";
import "./App.css";
import Login from "./components/login-page";
import React, { useState } from "react";
import { HiLibrary } from "react-icons/hi";
import { MdRestaurant } from "react-icons/md";
import { FaShoppingCart } from "react-icons/fa";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Umich One-Stop-Shop</h1>
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            alignItems: "flex-start",
          }}
        >
          <HiLibrary className="library-icon" />
          <MdRestaurant className="restaurant-icon" />
          <FaShoppingCart className="shopping-cart" />
        </div>

        <Login />
      </header>
    </div>
  );
}

export default App;
