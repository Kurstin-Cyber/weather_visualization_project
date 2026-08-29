import matplotlib.pyplot as plt
import pandas as pd

input_file = "raw_weather_data.csv"
output_file = "clean_weather_data.csv"

try:
    df = pd.read_csv(input_file)
    print("Original data loaded successfully.")
    print(df.head())

    df["Temperature"] = df["Temperature"].astype(str).str.extract(r"(-?\d+)")[0]

    df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")

    

    df = df.dropna(subset=["Temperature"])
    df["Temperature"] = df["Temperature"].astype(int)

    
    df.to_csv(output_file, index=False)
    print(f"Cleaned data successfully saved to {output_file}")
    print(df.head())

except Exception as e:
    print(f"An error occurred during data cleaning: {e}")


##Display

df = pd.read_csv("clean_weather_data.csv")

df = df.sort_values(by="Temperature", ascending=True)

plt.figure(figsize=(10,14))

plt.barh(df["City"], df["Temperature"], color="royalblue", edgecolor="black", alpha=0.85)

plt.xlabel("Temperature (°F)", fontsize=12, fontweight="bold")
plt.ylabel("City", fontsize=12, fontweight="bold")
plt.title("Current Global Temperatures by City", fontsize=14, fontweight="bold", pad=15)

plt.tight_layout()

chart_filename= "weather_temperature_chart.png"
plt.savefig(chart_filename, dpi=300)
print(f"Chart successfully saved to {chart_filename}")

plt.show()