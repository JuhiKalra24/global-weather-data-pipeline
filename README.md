# Global Weather Data Pipeline

## Project Overview

This project builds an automated data pipeline that collects real-time weather data using a public API and processes it using Python.

The pipeline extracts weather information for multiple cities, transforms the data into a structured format, and stores it for further analysis and visualization.

## Technologies Used

- Python
- Pandas
- Requests
- PostgreSQL
- SQL
- psycopg2-binary
- Power BI

## Project Architecture

Weather API → Python Script → Data Processing → PostgreSQL → Power BI Dashboard

## Data Pipeline Steps

1. Extract weather data from the Open-Meteo API.
2. Transform JSON responses into a structured DataFrame using Pandas.
3. Store the processed data in PostgreSQL database.
4. Perform SQL analysis on weather trends.
5. Visualize results using Power BI.

## Example Dataset

| timestamp | city | temperature | windspeed |
|----------|------|------------|----------|
| 2026-03-08 18:53 | Delhi | 29.7 | 4.2 |
| 2026-03-08 18:53 | Mumbai | 28.5 | 16.0 |

## Future Improvements

- Automate the pipeline using scheduling tools.
- Store data in cloud databases.
- Build real-time dashboards.