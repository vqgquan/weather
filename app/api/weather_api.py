from fastapi import APIRouter
from app.services.fetch_weather import get_weather

router = APIRouter()

@router.get("/weather")
def weather():
    return get_weather()