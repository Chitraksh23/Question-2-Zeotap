from app.models import get_daily_summary, save_weather_data
def calculate_daily_summary(city):
    data = db.weather.find({"city": city})
    temps = [entry["data"]["temp"] for entry in data]
    main_conditions = [entry["data"]["main"] for entry in data]
    daily_summary = {
        "city": city,
        "date": datetime.now().date(),
        "avg_temp": sum(temps) / len(temps),
        "max_temp": max(temps),
        "min_temp": min(temps),
        "dominant_condition": max(set(main_conditions), key=main_conditions.count)
    }
    db.weather_summary.insert_one(daily_summary)
