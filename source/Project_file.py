import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/weather_report.csv')
dates = data["Date"]
max_temp = data["Max_Temp"]
min_temp = data["Min_Temp"]

plt.plot(dates, max_temp, marker='o', label="Max Temp")
plt.plot(dates, min_temp, marker='o', label="Min Temp")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Weather Report Graph")
plt.legend()
plt.tight_layout()
plt.savefig('output/report_graph.png')
plt.show()
