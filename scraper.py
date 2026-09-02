import csv
import os
import pandas as pd
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.set_page_load_timeout(60)

try:
    url = "https://www.timeanddate.com/weather/"
    print("Fetching URL...")
    try:
        driver.get(url)
    except WebDriverException as e:
        print(f"Network warning during driver.get(): {e}. Continuing if elements are present...")

    wait = WebDriverWait(driver, 20)
  
    wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "table.zebra")))

    rows = driver.find_elements(By.CSS_SELECTOR, "table.zebra tbody tr")
    print("Rows found:", len(rows))

    scraped_data = []

    city_elements = driver.find_elements(By.CSS_SELECTOR, "table.zebra tbody tr td:nth-child(1) a")
    temp_elements = driver.find_elements(
         By.CSS_SELECTOR, "table.zebra tbody tr td:nth-child(4)"
    )

    print("Cities found:", len(city_elements))
    print("Temperatures found:", len(temp_elements))

   

    for city_element, temp_element in zip(city_elements, temp_elements):
        try:
            city = city_element.text.strip()
            temp = temp_element.text.strip()

            if city and temp:
                scraped_data.append({"City": city, "Temperature": temp})
        except Exception:
            continue
        
    print(f"Successfully extracted {len(scraped_data)} rows of data.")
  

    csv_filename = "raw_weather_data.csv"

    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["City", "Temperature"])
            writer.writeheader()
            for row in scraped_data:
                writer.writerow(row)

    print(f"Successfully scraped data and saved to {csv_filename}")

    db_dir = "db"
    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, "weather_school.db")

    df = pd.read_csv(csv_filename)
    df = df.dropna().drop_duplicates()

    with sqlite3.connect(db_path) as conn:
        df.to_sql("weather_data", conn, if_exists="replace", index=False)

    print("Successfully loaded scraped data into the SQLite database!")
    
except TimeoutException:
        print("Could not find the weather table within the waiting period.")
except Exception as e:
        print(f"An error occurred during web scraping: {e}")
finally:
    driver.quit()