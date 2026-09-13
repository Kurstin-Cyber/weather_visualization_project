import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"

options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--user-data-dir=C:/temp/selenium_weather")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

driver.set_page_load_timeout(60)


try:
    url = "https://www.timeanddate.com/weather/"
    print("Fetching URL...")

    try:
        driver.get(url)

    except TimeoutException:
        print("Page load timed out, but continuing with the page that loaded...")

    print("Page title:", driver.title)
    print("Current URL:", driver.current_url)

    wait = WebDriverWait(driver, 30)

    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "table.zebra")
        )
    )

    city_elements = driver.find_elements(
        By.CSS_SELECTOR,
        "table.zebra tbody tr td:nth-child(1) a"
    )

    temp_elements = driver.find_elements(
        By.CSS_SELECTOR,
        "table.zebra tbody tr td:nth-child(4)"
    )

    print("Cities found:", len(city_elements))
    print("Temperatures found:", len(temp_elements))

    scraped_data = []

    for city_element, temp_element in zip(
        city_elements,
        temp_elements
    ):
        try:
            city = city_element.text.strip()
            temp = temp_element.text.strip()

            if city and temp:
                scraped_data.append(
                    {
                        "City": city,
                        "Temperature": temp
                    }
                )

        except Exception:
            continue

    print(
        f"Successfully extracted "
        f"{len(scraped_data)} rows of data."
    )

    if not scraped_data:
        raise ValueError("No weather data rows were successfully parsed.")

    raw_csv_filename = "raw_weather_data.csv"

    with open(
        raw_csv_filename,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["City", "Temperature"]
        )

        writer.writeheader()
        writer.writerows(scraped_data)

    print(
        f"Successfully scraped data and saved to "
        f"{raw_csv_filename}"
    )


except TimeoutException:
    print(
        "Could not find the weather table within "
        "the waiting period."
    )

except Exception as e:
    print(f"An error occurred during web scraping: {e}")

finally:
    driver.quit()