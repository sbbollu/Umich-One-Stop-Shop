from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
#from datetime import date, datetime, time, timedelta
from fastapi.encoders import jsonable_encoder
from pydantic import Field

class Review(BaseModel):
    id: int = Field(frozen=True) #Required parameter
    location_id : int
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

class Location(BaseModel): #Will work for any location
    id: int = Field(frozen=True) #Required parameter
    name: str
    blue_bucks: bool
    dining_dollars: bool
    parameters: dict

    class Config:
        schema_extra = {
            "id" : 0,
            "name" : "",
            "parameters" : {}
        }

app = FastAPI()

#List of all reviews:
review_dict = {}

#List of all locations:
location_dict = {}

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
@app.post("/post_review", response_model=Review)
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
    
@app.patch("/edit_review/{id}", response_model=Review)
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
#________________________________________________________________________________________

#Enpoints for locations
#________________________________________________________________________________________
@app.post("/post_location", response_model=Location)
async def post_location(location: Location):
    location_dict[location.id] = location
    return location

@app.get("/get_locations")
async def get_locations():
    my_locations = []
    #Creates a new list of all reviews every time
    for item in location_dict.values():
        my_locations.append(item)
    return my_locations

@app.get("/get_location/{id}")
async def get_locations_by_id(id: int):
    my_locations = []
    #Creates a new list of all reviews every time
    for item in location_dict.values():
        if item.id == id:
            my_locations.append(item)
    return my_locations

@app.patch("/update_location/{id}")
async def update_review(id: int, location: Location):
    if location_dict[id]:
        old_location = location_dict[id] #Get the old location
        new_location_data = location.model_dump(exclude_unset=True) #Only the data from the old review that is being updated
        new_location = old_location.model_copy(update=new_location_data) 
        location_dict[id] = jsonable_encoder(new_location)
        return new_location
    else:
        raise HTTPException(status_code=404, detail="This location does not exist.")
    
@app.delete("/delete_review/{id}", response_model=Location)
#args: ID of the review to be deleted
async def delete_review(id: int):
    # Check if the review is in the review dictionary first before trying to delete the review
    if id in location_dict.keys():
        # Remove, get, and return the review
        location_to_delete = location_dict[id]
        del location_dict[id]
        return location_to_delete
    else:
        raise HTTPException(status_code=404, detail="This location does not exist.")
#___________________________________________________________________________________________
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)