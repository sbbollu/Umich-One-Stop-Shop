from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
#from datetime import date, datetime, time, timedelta
from fastapi.encoders import jsonable_encoder
from pydantic import Field

class Review(BaseModel):
    review_id: int = Field(frozen=True) #Required parameter
    location_id : int
    location_name: str
    rating: int
    review: str
    date: str

    class Config:
        schema_extra = {
            "review_id" : 0,
            "location_name" : "",
            "rating" : 5,
            "review" : 0,
            "date" : ""
        }

class Location(BaseModel): #Will work for any location
    location_id: int = Field(frozen=True) #Required parameter
    location_name: str
    blue_bucks: bool
    dining_dollars: bool
    parameters: dict

    class Config:
        schema_extra = {
            "location_id" : 0,
            "location_name" : "",
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

@app.get("/generate_review_id")
async def generate_review_id():
    counter = 0
    while review_dict[counter]:
        counter += 1
    return counter

@app.get("/generate_location_id")
async def generate_location_id():
    counter = 0
    while location_dict[counter]:
        counter += 1
    return counter

#Post a review
@app.post("/post_review", response_model=Review)
async def post_review(review: Review):
    #If the review is valid, add it to the list of reveiws
    if validate_review(review.rating):
        review_dict[review.review_id] = review
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
@app.get("/get_review_location_name")
async def get_review_location(location_name: str):
    my_list = []
    #Gets all reviews for a specific location
    for item in review_dict.values():
        if item.location_name == location_name:
            my_list.append(item)
    return my_list

@app.get("/get_review_location_id")
async def get_review_location_id(location_id: int):
    my_list = []
    #Gets all reviews for a specific location
    for item in review_dict.values():
        if item.location_id == location_id:
            my_list.append(item)
    return my_list

#Get requests for average rating of a location  
@app.get("/get_average_rating")
async def get_average_rating(location_id: int):
    counter = 0
    total_rating = 0
    for item in review_dict.values():
        if item.location_id == location_id:
            counter += 1
            total_rating += item.rating
    if counter == 0:
        raise HTTPException(status_code=404, detail="This location currently has no ratings.")
    else:
        avg_rating = total_rating / counter
        return avg_rating 
    
@app.patch("/edit_review/{review_id}", response_model=Review)
#args: ID of the review to be edited, new review that will replace the old review 
async def update_review(review_id: int, review: Review):
    if review_dict[review_id]:
        old_review = review_dict[review_id] #Get the old review
        new_review_data = review.model_dump(exclude_unset=True) #Only the data from the old review that is being updated
        new_review = old_review.model_copy(update=new_review_data) 
        review_dict[review_id] = jsonable_encoder(new_review)
        return new_review
    else:
        raise HTTPException(status_code=404, detail="This review does not exist.")

@app.delete("/delete_review", response_model=Review)
#args: ID of the review to be deleted
async def delete_review(review_id: int):
    # Check if the review is in the review dictionary first before trying to delete the review
    if review_id in review_dict.keys():
        # Remove, get, and return the review
        review_to_delete = review_dict[review_id]
        del review_dict[review_id]
        return review_to_delete
    else:
        raise HTTPException(status_code=404, detail="This review does not exist.")
#________________________________________________________________________________________

#Enpoints for locations
#________________________________________________________________________________________
@app.post("/post_location", response_model=Location)
async def post_location(location_name: Location):
    location_dict[location_name.location_id] = location_name
    return location_name

@app.get("/get_locations")
async def get_locations():
    my_locations = []
    #Creates a new list of all reviews every time
    for item in location_dict.values():
        my_locations.append(item)
    return my_locations

@app.get("/get_location/{location_id}")
async def get_locations_by_id(location_id: int):
    my_locations = []
    #Creates a new list of all reviews every time
    for item in location_dict.values():
        if item.location_id == location_id:
            my_locations.append(item)
    return my_locations

@app.patch("/update_location/{location_id}")
async def update_review(location_id: int, location_name: Location):
    if location_dict[location_id]:
        old_location = location_dict[location_id] #Get the old location
        new_location_data = location_name.model_dump(exclude_unset=True) #Only the data from the old review that is being updated
        new_location = old_location.model_copy(update=new_location_data) 
        location_dict[location_id] = jsonable_encoder(new_location)
        return new_location
    else:
        raise HTTPException(status_code=404, detail="This location does not exist.")
    
@app.delete("/delete_review/{review_id}", response_model=Location)
#args: ID of the review to be deleted
async def delete_review(review_id: int):
    # Check if the review is in the review dictionary first before trying to delete the review
    if review_id in location_dict.keys():
        # Remove, get, and return the review
        location_to_delete = location_dict[review_id]
        del location_dict[review_id]
        return location_to_delete
    else:
        raise HTTPException(status_code=404, detail="This location does not exist.")
#___________________________________________________________________________________________
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)