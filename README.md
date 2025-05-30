# DSA210_Project

## Project Proposal: The Impact of Weather Conditions on My Class Attendance

### Introduction

This project explores whether daily weather conditions influence my university class attendance. As a student living in Pendik, Istanbul, I rely on the campus shuttle for commuting. Therefore, shuttle usage is used as a proxy for attendance. The central question is whether factors such as temperature and precipitation affect my motivation or ability to attend class.

---

## Problem Statement

This study investigates the relationship between daily weather variables and my recorded class attendance. The aim is to determine:

- Whether cold or rainy days correlate with lower attendance,
- If class attendance shows weekly or seasonal patterns,
- Whether weather significantly affects attendance during exam weeks,
- If the influence of weather differs across weekdays.

---

## Research Questions

1. Is there a measurable relationship between weather conditions and attendance?
2. Are cold and rainy days associated with decreased attendance?
3. How do attendance patterns vary across weekdays and exam weeks?
4. Can we statistically confirm that bad weather impacts my likelihood of attending class?

---

## Dataset Overview

### Attendance Data

Manually collected over a period from February 10 to May 23, 2025. Dates corresponding to weekends, public holidays, and the earthquake-related university closure (April 24–25) were excluded.

Columns:
- `date`: calendar day
- `attendance`: binary (1 = attended, 0 = not attended)

### Weather Data

Collected via the Visual Crossing Weather API for Pendik, Istanbul (Latitude: 40.8902, Longitude: 29.3773).

Columns:
- `tempmax_c`: maximum temperature (°C)
- `tempmin_c`: minimum temperature (°C)
- `precip`: daily precipitation (mm)
- `conditions`: weather type (e.g., Rain, Snow, Clear)

---

## Methodology and Analysis Plan

1. **Data Preprocessing**
   - Merge attendance and weather data on the `date` column.
   - Filter out non-class days and handle missing values.

2. **Exploratory Data Analysis (EDA)**
   - Plot attendance against temperature and precipitation.
   - Create bar plots and box plots by weather type and weekday.
   - Investigate time trends and variability.

3. **Statistical Testing**
   - Conduct an independent samples t-test:
     - Group A: Cold (<10°C) and rainy (>0.2 mm) days
     - Group B: Other days
   - Test if Group A has significantly lower attendance.

4. **Regression Modeling**
   - Apply multiple linear regression to determine the predictive power of:
     - Maximum temperature
     - Precipitation

---

## Tools and Technologies

- Python (pandas, seaborn, matplotlib, scipy, statsmodels)
- Jupyter Notebook (Google Colab)
- Visual Crossing Weather API

---

## Expected Outcomes

- Identification of environmental conditions associated with poor attendance
- Statistical evidence on the relationship between weather and behavioral patterns
- Insights into the resilience of attendance during exam periods or across weekdays

---

## Limitations and Future Work

### Limitations

- Dataset reflects personal behavior and may not generalize
- Limited sample size, especially for rare conditions like snow
- External factors like health, workload, or motivation were not recorded

### Future Work

- Expand analysis to include more students and a longer time period
- Incorporate shuttle delay data or academic performance metrics
- Build a prediction model for daily attendance based on weather forecasts

---

## Conclusion

This project combines behavioral data with environmental data to analyze how weather affects class attendance. By using data science techniques learned in DSA210, this study demonstrates how real-world conditions can be measured, visualized, and tested using statistical tools. The results may provide insights not only into personal habits but also into broader academic planning and infrastructure decisions.
