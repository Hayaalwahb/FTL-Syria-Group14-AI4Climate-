# Eastern Syria Agro-Climate: Water Scarcity & Early-Warning Framework

FTL Syria AI4Climate Hackathon — Group 14

---

## 📌 Project Overview
This project presents an end-to-end climate analysis and early-warning framework for the Al-Jazira / Eastern Syria region using historical meteorological data from NASA POWER (2006–2025). 

By calculating the Standardized Precipitation Index (SPI) alongside temperature and evapotranspiration metrics, our analysis quantifies multi-year drought severity and provides actionable insights for climate resilience and sustainable agricultural planning.

---

## 🎯 Key Objectives & Research Question
* Primary Research Question: How have precipitation patterns and drought occurrences shifted across Eastern Syria over the past two decades (2006–2025), and how can Python-driven analysis power an early-warning system for regional agricultural protection?
* Compute monthly and annual climate indices (SPI-3 / SPI-12).
* Detect extreme climate events, drought cycles, and heat anomalies.
* Deliver visualisations and recommendations for local decision-makers.

---

## 📊 Dataset Specifications
* Source: NASA POWER (Prediction Of Worldwide Energy Resources) API / CSV Data.
* Geographical Scope: Eastern Syria / Al-Jazira Agricultural Zone.
* Time Horizon: 2006 – 2025 (20 Years of Daily/Monthly Observations).
* Variables Analyzed:
  * PRECTOTCORR: Corrected Total Precipitation (mm)
  * T2M: Temperature at 2 Meters (°C)
  * T2M_MAX / T2M_MIN: Maximum and Minimum Daily Temperatures (°C)
  * ALLSKY_SFC_SW_DWN: All Sky Surface Shortwave Downward Irradiance

---

## 🛠️ Tech Stack & Dependencies
* Programming Language: Python 3.10+
* Environment: Jupyter Notebook / VS Code
* Core Libraries:
  * Data Processing: pandas, numpy
  * Scientific / Statistical: scipy, statsmodels
  * Visualisation: matplotlib, seaborn
  * API / Networking: requests

---

## 🚀 Repository Structure
`text
.
├── climate_analysis.ipynb                      # Main Analysis & Visualisation Notebook
├── Eastern_Syria_Agro_Climate_Group14...pdf   # Final Presentation (7 Slides)
└── README.md                                   # Project Documentation
