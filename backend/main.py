from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

# from datetime import date, datetime, time, timedelta
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
    allow_origins=origins,  # Allows listed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)


class User(BaseModel):
    # Constructor
    def _init_(self, username: str, password: str, survey: dict, recommendations: dict):
        self.username = username
        self.password = password
        self.survey = survey
        self.recommendations = recommendations

    username: str = Field(frozen=True)  # Required parameter
    password: str = Field(frozen=True)  # Required parameter
    survey: dict
    recommendations: dict

    class Config:
        schema_extra = {
            "username": "",
            "password": "",
            "survey": {},
            "recommendations": {},
        }


# Stores User Objects
#users_list = []
users_dict = {}


# Validates username and password
@app.get("/login_button")
async def login_button(username: str, password: str):
    login_success = False
    if users_dict[username]:
        login_success = True
    return login_success

#NOTE: for testing, get rid of later
@app.get("/get_all_users")
async def get_all_users():
    return users_dict;

#NOTE: for testing, get rid of later
@app.delete("/delete_all_users")
async def delete_all_users():
    users_dict.clear();
    return users_dict;


# NOTE:Need to add error message on frontend


# Creating and adding a new user login, including the survey
# @app.post("/post_user", response_model=User)
# async def store_user_password(username: str, password: str, survey: dict):
#     recommendations = model(survey)
#     print(recommendations)
#     my_user = User(
#         username=username, password=password, recommendations=recommendations
#     )
#     users_dict[username] = my_user
#     return my_user
#     # If request is 200 (success) -> frontend call ml model


# Creating a post for JUST a username and password, no survey and no recommendations (just the default ones)
@app.post("/post_user_and_pass", response_model=User)
async def store_user_password(username: str, password: str):
    recommendations = model()
    survey = {}
    my_user = User(
        username=username,
        password=password,
        survey=survey,
        recommendations=recommendations,
    )
    users_dict[username] = my_user
    return my_user

# adding the survey and resulting recommendations to a user
# for a new user (NOT a guest user) when they create an account for the first time
@app.post("/post_survey_answers", response_model=dict)
async def post_survey_answers(username: str, password: str, survey: dict):
    my_user = users_dict[username]
    my_user.survey = survey
    my_user.recommendations = model(survey)
    return survey

# Returning a random recommendation feed for guest users
@app.get("/get_random_feed")
async def get_random_feed():
    return model()

# Returns true if an existing account has the same username as a user who is making a new account
@app.get("/check_multiple_usernames")
async def check_multiple_usernames(new_user_username: str):
    duplicate_usernames = users_dict.get(new_user_username)
    if (duplicate_usernames == None):
        return False
    else:
        return True


# Lets the user update their preferences and changes their recommendations by redoing the survey
@app.patch("/change_recommendations")
async def change_recommendations(username: str, password: str, survey: dict):
    # changed user.recommendations as well
    user = users_dict[username]
    if user.username == username and user.password == password:
        # NOTE: check to see that these changes get "pushed" into the dict afterwards
        user.recommendations = model(survey)

    return model(survey)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
