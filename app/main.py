from fastapi import FastAPI
from app.api.weather_api import router as weather_router

app = FastAPI()
app.include_router(weather_router)

@app.get("/")
def root():
    return {"message":"this is root"}