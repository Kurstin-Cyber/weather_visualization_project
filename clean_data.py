import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

input_file = "raw_weather_data.csv"
output_file = "clean_weather_data.csv"

try:
    df = pd.read_csv(input_file)
    print("Original data loaded successfully.")
    print(df.head())

    temperature = (
        df["Temperature"]
        .astype(str)
        .str.extract(r"(-?\d+)", expand=False)
    )

    df.loc[:, "Temperature"] = pd.to_numeric(temperature, errors="coerce")

    df = df.dropna(subset=["Temperature"]).copy()
    df.loc[:, "Temperature"] = df["Temperature"].astype(int)

    df.to_csv(output_file, index=False)
    print(f"Cleaned data successfully saved to {output_file}")
    print(df.head())

    db_path = "db/weather_school.db"

    with sqlite3.connect(db_path) as conn:
        df_raw = pd.read_csv(input_file)

        df_raw.to_sql("raw_weather_data", conn, if_exists="replace", index=False)
        df.to_sql("clean_weather_data", conn, if_exists="replace", index=False)

    print(f"Database successfully updated: {db_path}")
except Exception as e:
    print(f"An error occurred during data cleaning: {e}")


# Display

df = pd.read_csv("clean_weather_data.csv")

df = df.sort_values(by="Temperature", ascending=True)

plt.figure(figsize=(10, 14))

plt.barh(
    df["City"],
    df["Temperature"],
    color="royalblue",
    edgecolor="black",
    alpha=0.85
)

plt.xlabel("Temperature (°F)", fontsize=12, fontweight="bold")
plt.ylabel("City", fontsize=12, fontweight="bold")
plt.title("Current Global Temperatures by City", fontsize=14, fontweight="bold", pad=15)

plt.tight_layout()

chart_filename = "images/weather_temperature_chart.png"
plt.savefig(chart_filename, dpi=300)
print(f"Chart successfully saved to {chart_filename}")

plt.show()