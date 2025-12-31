# COVID-19 Data Analysis 📊🦠

This project analyzes COVID-19 data to uncover trends, visualize key metrics, and provide actionable insights using Python.

---

## 🚀 Project Overview

- **Dataset:** `Covid_Data.csv` containing daily COVID-19 cases and deaths.  
- **Objective:** Explore and analyze pandemic trends, peaks, and patterns.  
- **Tech Stack:** Python, Pandas, Matplotlib, Seaborn.  

**Key Highlights:**
- Daily confirmed cases vs deaths 📈  
- Region-wise / country-wise comparison 🌍  
- Trend smoothing using moving averages  
- Data-driven insights from visualizations  

---

## 📁 Project Files

- `Analysis.py` → Python script for data cleaning, analysis, and chart plotting  
- `Covid_Data.csv` → Dataset of COVID-19 cases and deaths  
- `README.md` → Project overview, setup instructions, and insights (this file)  

---

## 📊 Analysis & Charts

The `Analysis.py` script generates the following:

### 1️⃣ Daily Cases vs Deaths
- Visualizes the trend of daily confirmed cases against deaths.
- Peaks and waves of the pandemic are clearly visible.

### 2️⃣ Moving Average Trend
- Smooths out daily fluctuations.
- Helps identify long-term trends.

### 3️⃣ Region-wise Comparison
- Highlights top affected regions/countries.
- Allows quick comparison between regions.

**Insights:**
- Sharp peaks indicate major outbreaks.  
- Death trends usually lag behind confirmed cases.  
- Certain regions show consistent high case counts — actionable for health planning.

*Pro Tip:* Use Plotly/Dash for interactive charts in the next iteration.

---

## 💻 How to Run

```bash
# Install required libraries
pip install pandas matplotlib seaborn

# Run the analysis
python Analysis.py
