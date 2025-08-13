//Homepage of recommendations for both guest users and account users

//Login information frontend
import React, { useState } from "react";
import Select from 'react-select';
import { useLocation } from "react-router-dom";
import { useNavigate } from 'react-router-dom';
import newUser from "./login-page";
import guestUser from "./login-page";
import returningUser from "./login-page";
import axios from "axios";
import "./survey-page.css";

function Surveypage() {
  
  const[noiseLevel, setNoiseLevel] = useState("");
  const[busynessLevel, setBusynessLevel] = useState("");
  const[amenities, setAmenties] = useState("");
  const [errorMessage, seterrorMessage] = useState("");
  const [successMessage, setsuccessMessage] = useState("");

  const options = [
    { value: 1, label: 1 },
    { value: 2, label: 2 },
    { value: 3, label: 3 },
    { value: 4, label: 4 },
    { value: 5, label: 5 }
  ];

  const amenitiesOptions = [
    { value: "CAEN", label: "CAEN"},
    { value: "computers", label: "computers"},
    { value: "moniters", label: "moniters"},
    { value: "good number of outlets", label: "good number of outlets"},
    { value: "nearby food/cafes", label: "nearby food/cafes"},
    { value: "whiteboards", label: "whiteboards"},
    { value: "blackboards", label: "blackboards"},
    { value: "large tables", label: "large tables"},
    { value: "private rooms", label: "private rooms"},
    { value: "bright atmosphere", label: "bright atmosphere"},
    { value: "closeby to bus stops", label: "closeby to bus stops"},
    { value: "other", label: "other"}
  ];

  const restuarantBudgetOptions = [
    { value: "low end", label: "low end" },
    { value: "mid end", label: "mid end" },
    { value: "high end", label: "high end "},
    { value: "doesn't matter", label: "doesn't matter" }
  ];

  const northOrCentralPreference = [
    { value: "north", label: "north" },
    { value: "central", label: "central" },
    { value: "no preference", label: "no preference" }
  ];

  const outsideOrDiningOptions = [
    { value: "outside", label: "outside" },
    { value: "dining hall", label: "dining hall" },
    { value: "both", label: "both" },
    { value: "no preference", label: "no preference" }
  ];

  const fastFoodOrSitInOptions = [
    { value: "fast food", label: "fast food" },
    { value: "sit in", label: "sit in" },
    { value: "both", label: "both" },
    { value: "no preference", label: "no preference" }
  ];

  const cuisineOptions = [
    { value: "Indian", label: "Indian" },
    { value: "Chinese", label: "Chinese" },
    { value: "Japanese", label: "Japanese" },
    { value: "Korean", label: "Korean" },
    { value: "American", label: "American" },
    { value: "Middle Eastern", label: "Middle Eastern" },
    { value: "Mexican", label: "Mexican" },
    { value: "Thai", label: "Thai" },
    { value: "African", label: "African" },
    { value: "MDining Dining Halls and Mini Cafes (inside residental halls and libraries)", label: "MDining Dining Halls and Mini Cafes (inside residental halls and libraries)" },
    { value: "sit in", label: "sit in" },
    { value: "Other", label: "Other" }
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted");
  };

  //what the user sees
  return (

    <div>
      <h1>Survey page!</h1>
      <form onSubmit={handleSubmit}>
      <h2>What noise level are you comfortable with?</h2>
        <Select
          className="question"
          options={options}
          value={noiseLevel}
          onChange={(selectedOption) => setNoiseLevel(selectedOption)}
          placeholder="Select noise level"
        />
      <h2>What busyness levels are you comfortable with?</h2>
        <Select
          className="question"
          options={options}
          value={busynessLevel}
          onChange={(selectedOption) => setBusynessLevel(selectedOption)}
          placeholder="Select noise level"
        />
      <h2>Which of these amenities do you require for a study space?</h2>
        <Select
          className="question"
          options={amenitiesOptions}
          value={amenities}
          onChange={(selectedOption) => setAmenties(selectedOption)}
          placeholder="Select noise level"
        />
      <h2>What is your preferred budget for restaurants?</h2>
        <Select
          className="question"
          options={restuarantBudgetOptions}
          value={noiseLevel}
          onChange={(selectedOption) => setNoiseLevel(selectedOption)}
          placeholder="Select noise level"
        />
      <h2>How high of a deciding factor is price to you on a scale of 1 to 5?</h2>
        <Select
          className="question"
          options={options}
          value={noiseLevel}
          onChange={(selectedOption) => setNoiseLevel(selectedOption)}
          placeholder="Select noise level"
        />
      <h2>How far are you willing to travel to a location from central campus on a scale of 1 to 5?</h2>
        <Select
          className="question"
          options={options}
          value={noiseLevel}
          onChange={(selectedOption) => setNoiseLevel(selectedOption)}
          placeholder="Select noise level"
        />
      <h2>Do you prefer dining hall or outside of dining hall options</h2>
        <Select
          className="question"
          options={outsideOrDiningOptions}
          value={noiseLevel}
          onChange={(selectedOption) => setNoiseLevel(selectedOption)}
          placeholder="Select noise level"
        />
      <h2>Do you prefer fast food or sit in restaurants?</h2>
        <Select
          className="question"
          options={fastFoodOrSitInOptions}
          value={noiseLevel}
          onChange={(selectedOption) => setNoiseLevel(selectedOption)}
          placeholder="Select noise level"
        />
      <h2>What type of cuisine do you prefer?</h2>
        <Select
          className="question"
          options={cuisineOptions}
          value={noiseLevel}
          onChange={(selectedOption) => setNoiseLevel(selectedOption)}
          placeholder="Select noise level"
        />
      <button type="submit" className="login-page-submit-button">
        Submit 
      </button>
      {errorMessage && <div>{errorMessage}</div>}
      {successMessage && <div>{successMessage}</div>}
    </form>
    </div>

  );
}

export default Surveypage;
