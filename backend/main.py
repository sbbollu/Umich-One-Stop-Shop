from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
#from datetime import date, datetime, time, timedelta
from fastapi.encoders import jsonable_encoder
from pydantic import Field

class Review(BaseModel):
    id: int = Field(frozen=True) #Required parameter
    location: str
    rating: int
    review: str
    date: str

    class Config:
        schema_extra = {
            "id" : 0,
            "location" : "",
            "rating" : 5,
            "review" : 0,
            "date" : ""
        }

class Places(BaseModel):
    id: int = Field(frozen=True) #Required parameter

    class Config:
        schema_extra = {
            "id" : 0
        }

class Restaurant(BaseModel):
    id: int = Field(frozen=True) #Required parameter

    class Config:
        schema_extra = {
            "id" : 0
        }

app = FastAPI()

#List of all reviews
review_dict = {}

# Function that validates the ratings to see if they are between 1 and 5
def validate_review(rating: int):
    if (rating < 1 or rating > 5):
        return False
    else:
        return True
    
#Endpoints for reviews
#_________________________________________________________________________________    
#Get request for the homepage
@app.get("/")
async def homepage():
    return {"message": "Welcome to Umich One Stop Shop."}

#Post a review
@app.post("/post_review")
async def post_review(review: Review):
    #If the review is valid, add it to the list of reveiws
    if validate_review(review.rating):
        review_dict[review.id] = review
        return review
    #If the review is invalid, raise an exception
    else:
        raise HTTPException(status_code=404, detail="Rating should be between 1 and 5 inclusive.")

#Get request for entire review list  
@app.get("/get_list")
async def get_reviews():
    my_list = []
    #Creates a new list of all reviews every time
    for item in review_dict.values():
        my_list.append(item)
    return my_list

#Get requests for reviews of a particular location 
@app.get("/get_review_location")
async def get_review_location(location: str):
    my_list = []
    #Gets all reviews for a specific location
    for item in review_dict.values():
        if item.location == location:
            my_list.append(item)
    return my_list

#Get requests for average rating of a location  
@app.get("/get_average_rating")
async def get_average_rating(location: str):
    counter = 0
    total_rating = 0
    for item in review_dict.values():
        if item.location == location:
            counter += 1
            total_rating += item.rating
    if counter == 0:
        raise HTTPException(status_code=404, detail="This location currently has no ratings.")
    else:
        avg_rating = total_rating/counter
        return avg_rating 
    
@app.patch("/edit_review", response_model=Review)
#args: ID of the review to be edited, new review that will replace the old review 
async def update_review(id: int, review: Review):
    if review_dict[id]:
        old_review = review_dict[id] #Get the old review
        new_review_data = review.model_dump(exclude_unset=True) #Only the data from the old review that is being updated
        new_review = old_review.model_copy(update=new_review_data) 
        review_dict[id] = jsonable_encoder(new_review)
        return new_review
    else:
        raise HTTPException(status_code=404, detail="This review does not exist.")
    
#Add delete review:
#_________________________________________________________________________________

@app.delete("/delete_review", response_model=Review)
#args: ID of the review to be deleted
async def delete_review(id: int):
    # Check if the review is in the review dictionary first before trying to delete the review
    if id in review_dict.keys():
        # Remove, get, and return the review
        review_to_delete = review_dict[id]
        del review_dict[id]
        return review_to_delete
    else:
        raise HTTPException(status_code=404, detail="This review does not exist.")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)