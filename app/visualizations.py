import matplotlib.pyplot as plt
def plot_daily_summary(city):
    data = db.weather_summary.find({"city": city})
    dates = [entry["date"] for entry in data]
    temps = [entry["avg_temp"] for entry in data]
    plt.plot(dates, temps, label="Average Temperature")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Daily Temperature Summary for {city}")
    plt.legend()
    plt.savefig(f"{city}_temperature_summary.png")
