import logo from "./logo.svg";
import "./App.css";
import React, { useState } from "react";
import { HiLibrary } from "react-icons/hi";
import { MdRestaurant } from "react-icons/md";
import { FaShoppingCart } from "react-icons/fa";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './components/login-page';
import NewUser from './components/new-user';
import Homepage from './components/homepage';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            gap: "20px",
            alignItems: "flex-start",
          }}
        >
          <HiLibrary className="library-icon" />
          <MdRestaurant className="restaurant-icon" />
          <FaShoppingCart className="shopping-cart" />
        </div>

        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/new_user" element={<NewUser />} />
            <Route path="/homepage" element={<Homepage />} />
          </Routes>
        </BrowserRouter>
      </header>
    </div>
  );
}

export default App;
