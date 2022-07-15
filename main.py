from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import sqlite3


conn = sqlite3.connect('User.db',check_same_thread=False)
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
    c.execute("insert into users values (?,?,?,?)",(user.name,user.age,user.gender,user.major))
    print("values should be added successfully!")
    return users

@app.delete("/deleteUserById")
def deleteUser(userId:int):
    c.execute("delete from users where rowid = 2")
    c.execute("select rowId,* from users")
    users = c.fetchall()

    return users
