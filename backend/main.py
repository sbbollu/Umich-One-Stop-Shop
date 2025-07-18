from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
#from datetime import date, datetime, time, timedelta
from fastapi.encoders import jsonable_encoder
from pydantic import Field
from ml_model import model

class User(BaseModel):
    #NOTE: might delete
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

app = FastAPI()

#Validate username and password
@app.get("/login_button")
async def login_button(username: str, password: str):
    login_success = False
    for user in users_list:
        if(user.username == username and user.password == password):
            login_success = True
    return login_success

#NOTE:Need to add error message on frontend

#Creating and adding a new user login:
@app.post("/post_user", response_model=User)
async def store_user_password(username: str, password: str, survey: dict):
    recommendations = model(survey)
    print(recommendations)
    my_user = User(username=username, password=password, recommendations=recommendations)
    users_list.append(my_user)
    return my_user
    #If request is 200 (success) -> frontend call ml model

#Returning a random recommendation feed for guest users
@app.get("/get_random_feed")
async def get_random_feed():
    return model()

@app.patch("/change_recommendations")
async def change_recommendations(username: str, password: str, survey: dict):
    #NOTE: change user.recommendations as well
    for user in users_list:
        if(user.username == username and user.password == password):
            user.recommendations = model(survey)

    return model(survey)

  
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)