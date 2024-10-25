from app.models import save_alert
THRESHOLDS = {
    "temp": 35,  # Example: alert if temp > 35
}
def check_alerts(city, data):
    if data["temp"] > THRESHOLDS["temp"]:
        alert_data = {
            "condition": "Temperature Exceeded",
            "value": data["temp"]
        }
        save_alert(city, alert_data)
