from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import sqlite3

conn = sqlite3.connect('User.db',check_same_thread=False)
c = conn.cursor()
app = FastAPI()
users = {}

@app.get("/registerNewUser")
def registerNewUser(name,age,gender,major):
    c.execute("insert into users values (?,?,?,?)",(name,age,gender,major))
    print("values should be added successfully!")
    return name + ' Has been created'

@app.get("/selectUsers")
def deleteUser():
    c.execute("select * from users")
    users = c.fetchall()
    return users
