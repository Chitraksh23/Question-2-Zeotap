def save_weather_data(city, weather_data):
    db.weather.insert_one({
        "city": city,
        "data": weather_data
    })
def get_daily_summary(city, date):
    return db.weather_summary.find_one({"city": city, "date": date})
def save_alert(city, alert_data):
    db.alerts.insert_one({
        "city": city,
        "alert": alert_data
    })
