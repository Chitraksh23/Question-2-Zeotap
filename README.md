# Weather Monitoring System
A real-time data processing system to monitor weather data for major Indian cities. This system retrieves data from OpenWeatherMap API, stores it in MongoDB, and provides daily summaries, visualizations, and alerting.
## Setup
1. **Install Docker and Docker Compose.**
2. **Configure API Key**: Add your OpenWeatherMap API key to `app/fetcher.py`.
3. **Build and Run**:
   ```bash
   docker-compose up --build
