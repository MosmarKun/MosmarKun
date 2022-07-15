from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import sqlite3

class User(BaseModel):
    name:str
    age:int
    gender:str
    major:str
users = {}
x = 0
for user in dbUsers:
    users[dbUsers[x][0]] = {"name":dbUsers[x][1],"age":dbUsers[x][2],"gender":dbUsers[x][3],"major":dbUsers[x][4]}
    x = x + 1


app = FastAPI()

@app.get("/getUsers")
def getUsers():
    print(dbUsers)
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
