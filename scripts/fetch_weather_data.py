import requests
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(
    filename="../logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():

    logging.info("Weather pipeline started")

cities = {
    "Delhi": (28.61, 77.23),
    "Mumbai": (19.07, 72.87),
    "Bangalore": (12.97, 77.59),
    "Chennai": (13.08, 80.27),
    "Kolkata": (22.57, 88.36),
    "Hyderabad": (17.38, 78.48),
    "London": (51.50, -0.12),
    "Paris": (48.85, 2.35),
    "Berlin": (52.52, 13.40),
    "Rome": (41.90, 12.49),
    "Madrid": (40.41, -3.70),
    "New York": (40.71, -74.00),
    "Los Angeles": (34.05, -118.24),
    "Toronto": (43.65, -79.38),
    "Tokyo": (35.67, 139.69)
}

    weather_data = []

    for city, coords in cities.items():

        logging.info(f"Fetching weather data for {city}")

        lat, lon = coords

        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

        response = requests.get(url)

        data = response.json()

        record = {
            "timestamp": datetime.now(),
            "city": city,
            "temperature": data["current_weather"]["temperature"],
            "windspeed": data["current_weather"]["windspeed"],
            "winddirection": data["current_weather"]["winddirection"]
        }

        weather_data.append(record)

    df = pd.DataFrame(weather_data)

    df.to_csv("../data/weather_data.csv", mode="a", header=False, index=False)

    logging.info("Weather data saved successfully")


if __name__ == "__main__":

    main()
