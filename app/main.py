from flask import jsonify, request
from app import app, fetcher, processor, alerts
@app.route("/start")
def start_fetching():
    fetcher.start_scheduler()
    return jsonify({"status": "Fetching started"}), 200
@app.route("/summary/<city>")
def daily_summary(city):
    data = processor.calculate_daily_summary(city)
    return jsonify(data)
@app.route("/alerts/<city>")
def get_alerts(city):
    alerts = db.alerts.find({"city": city})
    return jsonify([alert for alert in alerts])
