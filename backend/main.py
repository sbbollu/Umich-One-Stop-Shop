from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
#from datetime import date, datetime, time, timedelta
from fastapi.encoders import jsonable_encoder
from pydantic import Field
from .ml_model import model

class User(BaseModel):
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

#Error message on frontend

#New user login:
@app.post("/post_user")
async def store_user_password(username: str, password: str):
    recommendations = model()
    my_user = {'username' : username, 
               'password' : password,
               'recommendations': recommendations}
    users_list.append(my_user)
    #If request is 200 (success) -> frontend call ml model
  
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)