# API-INTEGRATION-AND-DATA-VISUALIZATION
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# API CONFIG
# -----------------------------
API_KEY = "5022f50fad82003d81f1260d7f47e3c4"   
CITY = "Delhi"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# -----------------------------
# FETCH DATA
# -----------------------------
response = requests.get(URL)
data = response.json()

temps = []
dates = []

for item in data["list"]:
    temps.append(item["main"]["temp"])
    dates.append(item["dt_txt"])

# -----------------------------
# VISUALIZATION
# -----------------------------
sns.set()
plt.figure(figsize=(10,5))
plt.plot(dates[:10], temps[:10])
plt.xticks(rotation=45)
plt.title("Temperature Forecast for bhopal")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
