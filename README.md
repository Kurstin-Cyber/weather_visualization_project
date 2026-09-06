# Weather-Visualization-Project

# Python Capstone Project: Web Scraping & Database Integration

## Project Overview
This project is an automated data pipeline and analytics tool. It utilizes **Selenium** to scrape live weather information from the web, processes and cleans the raw data using **Pandas**, and securely stores the structured dataset into a local **SQLite** database. 

## Features
- **Automated Web Scraping:** Uses Selenium with an eager page-load strategy and headless-ready configurations to extract real-time data efficiently.
- **Data Cleaning & Transformation:** Employs Pandas to inspect, handle missing values, drop duplicates, and prepare data for database insertion.
- **Relational Database Storage:** Automatically creates a local `db/` directory and loads the cleaned data into an indexed SQLite database (`weather_school.db`).
- **Robust Error Handling:** Features built-in timeout handling, network warnings, and `try-except-finally` blocks to guarantee graceful resource management and clean browser shutdowns.

## Project Structure
weather_visualization_project/
│
├── db/
│   └── weather_school.db
├── images/
│   └── weather_temperature_chart.png
├── venv/
├── clean_data.py
├── clean_weather_data.csv
├── raw_weather_data.csv
├── README.md
└── scraper.py