import requests
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.models import save_weather_data
API_KEY = 'YOUR_API_KEY'
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url).json()
    data = {
        "main": response["weather"][0]["main"],
        "temp": response["main"]["temp"] - 273.15,
        "feels_like": response["main"]["feels_like"] - 273.15,
        "dt": datetime.now()
    }
    save_weather_data(city, data)
def start_scheduler():
    scheduler = BackgroundScheduler()
    for city in CITIES:
        scheduler.add_job(lambda: fetch_weather(city), 'interval', minutes=5)
    scheduler.start()
