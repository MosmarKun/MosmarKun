from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import sqlite3


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

@app.delete("/deleteUserById")
def deleteUser(userId:int):
    c.execute("delete from users where rowid = 2")
    c.execute("select rowId,* from users")
    users = c.fetchall()

    return users
