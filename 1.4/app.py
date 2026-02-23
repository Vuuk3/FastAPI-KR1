from fastapi import FastAPI
from models import User

app = FastAPI()

user = User(id=1, name="Артур")

@app.get("/users")
async def users():
    return {"id": user.id, "name": user.name}
