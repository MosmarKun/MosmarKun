from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import sqlite3

conn = sqlite3.connect('User.db',check_same_thread=False)
c = conn.cursor()
app = FastAPI()
users = {}

@app.post("/registerNewUser")
def registerNewUser(name,age,gender,major):
    c.execute("insert into users values (?,?,?,?)",(name,age,gender,major))
    print("values should be added successfully!")
    return name + ' Has been created'
