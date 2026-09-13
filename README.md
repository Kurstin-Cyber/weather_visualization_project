# Weather Visualization Project

## Project Overview

This Python capstone project collects current weather information from Timeanddate.com, cleans the data, stores it in a SQLite database, and creates a temperature visualization.

The project demonstrates a complete data pipeline:

Website → Selenium → Raw CSV → Pandas Cleaning → Clean CSV → SQLite Database → Visualization

## Technologies Used

- Python
- Selenium
- WebDriver Manager
- Pandas
- SQLite
- Matplotlib
- Git and GitHub

## Data Source

Weather data is collected from:

Timeanddate.com Weather Around The World

The Selenium scraper collects the city name and current temperature for cities displayed on the weather page.

## Project Workflow

### 1. Web Scraping

The scraper.py program uses Selenium WebDriver to open the Timeanddate.com weather page.

The program:

- Loads the weather webpage
- Waits for the weather table to appear
- Extracts city names
- Extracts temperatures
- Saves the scraped information to raw_weather_data.csv
- Includes timeout and error handling
- Closes the browser after the scraping process

The current successful scrape collects data for 47 cities.

### 2. Data Cleaning

The clean_data.py program uses Pandas to clean the scraped weather data.

The program:

- Reads raw_weather_data.csv
- Extracts the numeric temperature from the temperature values
- Converts temperatures to numeric values
- Removes rows with missing or invalid temperatures
- Saves the cleaned data to clean_weather_data.csv

The current cleaned dataset contains 47 cities.

### 3. SQLite Database

The cleaned and raw data are stored in:

db/weather_school.db

The database contains two tables:

- raw_weather_data
- clean_weather_data

Each table currently contains 47 rows.

### 4. Data Visualization

Matplotlib is used to create a horizontal bar chart showing current temperatures by city.

The chart is saved as:

images/weather_temperature_chart.png

The cities are sorted by temperature so the visualization is easier to compare.

## Project Structure

weather_visualization_project/

README.md

scraper.py

clean_data.py

raw_weather_data.csv

clean_weather_data.csv

db/

weather_school.db

images/

weather_temperature_chart.png

## How to Run the Project

### Step 1: Run the Web Scraper

Run:

py scraper.py

This collects the current weather data and saves it to raw_weather_data.csv.

### Step 2: Clean the Data and Update the Database

Run:

py clean_data.py

This cleans the scraped data, saves clean_weather_data.csv, updates the SQLite database, and creates the weather visualization.

## Current Project Results

The project has been successfully tested.

- Selenium successfully scraped 47 cities.
- raw_weather_data.csv contains 47 rows.
- clean_weather_data.csv contains 47 rows.
- The SQLite database contains two weather data tables.
- Both database tables contain 47 rows.
- The Matplotlib visualization was successfully generated.
- scraper.py and clean_data.py successfully compile without syntax errors.

## Error Handling

The Selenium scraper includes timeout handling for webpage loading and for locating the weather table.

The scraper also includes general error handling and ensures the browser is closed after the scraping process.

## Project Purpose

This project demonstrates the ability to:

- Collect data from a live website using Selenium
- Process and clean data using Pandas
- Store structured data using SQLite
- Create data visualizations using Matplotlib
- Build a Python data pipeline from collection through visualization
- Organize a Python project using Git and GitHub