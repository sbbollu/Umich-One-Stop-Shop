from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
#from datetime import date, datetime, time, timedelta
from fastapi.encoders import jsonable_encoder
from pydantic import Field
from ml_model import model

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# List of origins that should be permitted to make cross-origin requests
origins = [
    "http://localhost:3000",  # React dev server
    "http://localhost:8000",
    # Add other frontend URLs if deployed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows listed origins
    allow_credentials=True,
    allow_methods=["*"],              # Allows all HTTP methods
    allow_headers=["*"],              # Allows all headers
)

class User(BaseModel):
    #Constructor
    def _init_(self, username: str, password: str, recommendations: dict):
        self.username = username
        self.password = password
        self.recommendations = recommendations

    username: str = Field(frozen=True) #Required parameter
    password: str = Field(frozen=True) #Required parameter
    recommendations: dict

    class Config:
        schema_extra = {
            "username" : "",
            "password" : "",
            "recommendations" : {}
        }

#Stores User Objects
users_list = [] 

#Validates username and password
@app.get("/login_button")
async def login_button(username: str, password: str):
    login_success = False
    for user in users_list:
        if(user.username == username and user.password == password):
            login_success = True
    return login_success

#NOTE:Need to add error message on frontend

#Creating and adding a new user login, including the survey
@app.post("/post_user", response_model=User)
async def store_user_password(username: str, password: str, survey: dict):
    recommendations = model(survey)
    print(recommendations)
    my_user = User(username=username, password=password, recommendations=recommendations)
    users_list.append(my_user)
    return my_user
    #If request is 200 (success) -> frontend call ml model

#Creating a post for JUST a username and password, no survey
@app.post("/post_user_and_pass", response_model=User)
async def store_user_password(username: str, password: str):
    recommendations = model()
    print(recommendations)
    my_user = User(username=username, password=password, recommendations=recommendations)
    users_list.append(my_user)
    return my_user

#Returning a random recommendation feed for guest users
@app.get("/get_random_feed")
async def get_random_feed():
    return model()

#Lets the user update their preferences and changes their recommendations
@app.patch("/change_recommendations")
async def change_recommendations(username: str, password: str, survey: dict):
    #changed user.recommendations as well
    for user in users_list:
        if(user.username == username and user.password == password):
            user.recommendations = model(survey)

    return model(survey)

  
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)