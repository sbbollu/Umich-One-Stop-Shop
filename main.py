from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class Review(BaseModel):
    id: int | None = None
    location: str
    rating: int
    review: str
    date: datetime

app = FastAPI()

#List of al reviews
review_list = []

def validate_review(rating: int):
    if (rating < 1 or rating > 5):
        return False
    else:
        return True
    
@app.get("/")
async def homepage():
    return {"message": "Welcome to Umich One Stop Shop"}

@app.post("/post_review")
async def post_review(review: Review):
    if validate_review(review.rating):
        review_list.append(review)
        return review
    else:
        raise HTTPException(status_code=404, detail="Rating should be between 1 and 5 inclusive")
    
@app.get("/get_list")
async def get_reviews():
    my_list = []
    for item in review_list:
        my_list.append(item)
    return my_list
    
@app.get("/get_average_rating")
async def get_average_rating(location: str):
    counter = 0
    total_rating = 0
    for item in review_list:
        if item.location == location:
            counter += 1
            total_rating += item.rating
    if counter == 0:
        raise HTTPException(status_code=404, detail="This location currently has no ratings")
    else:
        avg_rating = total_rating/counter
        return avg_rating

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


