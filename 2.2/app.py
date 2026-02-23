from fastapi import FastAPI
from models import Feedback

feedbackes = []

app = FastAPI()

@app.post("/feedback")
async def feedback(feedback: Feedback):
    feedbackes.append(feedback.message)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}
