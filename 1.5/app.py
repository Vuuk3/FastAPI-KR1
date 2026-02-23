from fastapi import FastAPI, Body
from models import User

app = FastAPI()

def is_adult(age):
    return age >= 18

@app.post("/user")
async def users(data = Body()):
    user = User(name=data["name"], age=data["age"])
    return {"name": user.name, "age": user.age, "is_adult": is_adult(user.age)}
