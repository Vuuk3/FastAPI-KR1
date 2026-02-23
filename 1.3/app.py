from fastapi import Body, FastAPI

app = FastAPI()

@app.post("/calculate")
async def calculate(data = Body()):
    return {"result": data["num1"] + data["num2"]}
