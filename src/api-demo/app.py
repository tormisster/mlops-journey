from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Lead(BaseModel):
    page_views: int
    asked_price: bool

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(lead: Lead):
    score = min(lead.page_views * 10, 70) + (30 if lead.asked_price else 0)
    return {"score": score, "likely_to_enroll": score >= 50}
