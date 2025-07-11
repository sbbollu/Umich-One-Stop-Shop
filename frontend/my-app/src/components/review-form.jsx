import React, { useState } from "react";

function ReviewForm() {
  const [id, setId] = useState("");
  const [location_id, setLocationId] = useState("");
  const [location, setLocation] = useState("");
  const [rating, setRating] = useState("");
  const [review, setReview] = useState("");
  const [date, setDate] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/post_review", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id,
          location_id,
          location,
          rating,
          review,
          date,
        }),
      });
      const result = await response.json();
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        value={id}
        onChange={(e) => setId(e.target.value)}
        placeholder="ID"
      />
      <button type="submit">Submit</button>
    </form>
  );
}

export default ReviewForm;
