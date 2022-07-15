from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    gender:str
    major:str
users = {}


app = FastAPI()

@app.get("/getUsers")
def getUsers():
    return users

@app.get("/getUserById/{userId}")
def getUser(userId:int):
    return users[userId]

@app.get("/getUserByName/{userName}")
def getUser(userName:str):
    for userId in users:
        if users[userId]["name"] == userName:
            return users[userId]
    raise HTTPException.Http404

@app.post("/registerNewUser")
def registerNewUser(user:User):
    users[len(users) + 1] = user
    print("values should be added successfully!")
    return users
    
@app.delete("/deleteUserById")
def deleteUser(userId:int):
    return users
