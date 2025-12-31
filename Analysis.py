# -----------------------------------------
# COVID-19 Data Analysis & Impact Insights
# -----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load Dataset
# -------------------------------
data = pd.read_csv(r"C:\Users\gaura\OneDrive\Desktop\COVID-19-Data-Analysis\Covid_Data.csv.csv")

print("\n--- Dataset Preview ---")
print(data)

# -------------------------------
# 2. Global Summary
# -------------------------------
total_confirmed = data["Confirmed"].sum()
total_recovered = data["Recovered"].sum()
total_deaths = data["Deaths"].sum()

print("\n--- Global COVID Summary ---")
print("Total Confirmed Cases:", total_confirmed)
print("Total Recovered Cases:", total_recovered)
print("Total Deaths:", total_deaths)

# -------------------------------
# 3. Rate Calculations
# -------------------------------
data["Recovery_Rate (%)"] = (data["Recovered"] / data["Confirmed"]) * 100
data["Death_Rate (%)"] = (data["Deaths"] / data["Confirmed"]) * 100

print("\n--- Recovery & Death Rates ---")
print(data[["Country", "Recovery_Rate (%)", "Death_Rate (%)"]])

# -------------------------------
# 4. Top Affected Countries
# -------------------------------
top_affected = data.sort_values(by="Confirmed", ascending=False)

print("\n--- Top Affected Countries ---")
print(top_affected[["Country", "Confirmed"]])

# -------------------------------
# 5. Visualizations
# -------------------------------

# Confirmed Cases Bar Chart
plt.figure()
plt.bar(data["Country"], data["Confirmed"])
plt.title("Country-wise Confirmed COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.show()

# Recovery vs Death Bar Chart
plt.figure()
plt.bar(data["Country"], data["Recovered"], label="Recovered")
plt.bar(data["Country"], data["Deaths"], label="Deaths")
plt.title("Recovery vs Death Comparison")
plt.xlabel("Country")
plt.ylabel("Number of Cases")
plt.legend()
plt.show()

# Death Distribution Pie Chart
plt.figure()
plt.pie(data["Deaths"], labels=data["Country"], autopct="%1.1f%%")
plt.title("Death Percentage Distribution by Country")
plt.show()

# -------------------------------
# 6. Key Observations
# -------------------------------
print("\n--- Key Observations ---")
print("1. USA has the highest confirmed and death cases.")
print("2. India shows a strong recovery rate.")
print("3. Germany and UK have relatively lower death rates.")
print("4. Recovery trends are stronger than death trends globally.")
