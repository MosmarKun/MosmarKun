from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyodbc

app = FastAPI()
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=(LocalDB)\MSSQLLocalDB;"
    "Database=Test;"
    "Trusted_Connection=yes;"
)
x = 0
y = 0
Go = 0
cursor = conn.cursor()
cursor.execute("Select * from Users")
usersDB = cursor.fetchall()
users = {}
cursor.commit()

for row in usersDB:
    users[x] = {"Username": usersDB[x][0], "Password": usersDB[x][1]}
    x = x + 1


def Insert(username, password):
        cursor.execute('Insert into Users values(?,?);',
                      (username, password))
        cursor.commit()


def GetUser(name):
    cursor.execute('Select * from Users where name = ?;',
                   (name))
    for row in cursor:
        print(f'row={row}')
    cursor.commit()


@app.get("/getUsers")
def GetUsers():
    return users


@app.post("/registerNewUser")
def registerNewUser(username, password):
    for row in users:
        if (users[row]['Username'] == username):
            raise HTTPException(status_code=404, detail='Username is taken')
            return 'Bad'
    Insert(username, password)
    users[len(users)+1] = {"Username": username, "Password": password}
    return users[len(users)]



@app.get("/getUser")
def getUser(name):
        GetUser(name)
