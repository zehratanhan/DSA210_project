# DSA210_project
# Project Proposal: The Impact of Weather Conditions on Class Attendance for Off-Campus Students

**Introduction**
Class attendance is a critical factor in academic success. However, various external factors can influence a student’s decision to attend classes, particularly weather conditions. 

**Problem Statement**
This project aims to explore the relationship between weather conditions and my class attendance habits. Since I live off-campus and rely exclusively on the shuttle service to commute, my shuttle usage serves as a direct proxy for whether I attended class on a given day.

By analyzing historical weather data and my shuttle usage records, I seek to understand:
- How different weather conditions (e.g., rain, temperature, wind) impact class attendance.
- Whether extreme weather (e.g., heavy rain, storms, extreme cold) significantly reduces attendance.

**Research Questions**
This project will address the following key questions:
1. How do weather variables (temperature, precipitation, humidity, wind) correlate with my class attendance?
2. Can weather data be used to predict whether I will attend class?

---

**Data Collection**

**1. Attendance Data (Shuttle Usage)**
Since I only use the shuttle when attending classes, shuttle usage will serve as a proxy variable for my class attendance. I will collect the data from mySU.

- Data Points Tracked:
  - `date` → The day of the recorded instance.
  - `shuttle_used (binary)` → 1 if I took the shuttle (attended class), 0 if I did not (skipped class).
  - `departure_time` → The time I left for class.
  - `alternative_transportation` → If applicable, which alternative mode I used (walking, bus, etc.).
  
**2. Weather Data**
Weather data will be collected via an API (e.g., OpenWeather) and merged with my shuttle usage dataset.

- Weather Variables Collected:
  - `temperature_min` (°C) → Minimum temperature of the day.
  - `temperature_max` (°C) → Maximum temperature of the day.
  - `precipitation` (mm) → Amount of rainfall/snowfall.
  - `weather_condition` → Categorical (sunny, cloudy, stormy, etc.).

---

**Methodology & Analysis Plan**

- Visualizing the frequency of class attendance under different weather conditions.
- Checking trends over time (seasonal effects, patterns).
- Using the informations that i learned in DSA210 class and use this informations to use the data properly.

---

**Expected Outcomes**
Identification of weather conditions that negatively impact attendance.  
Potential correlations between extreme weather and skipped classes.   
 

---

**Limitations & Future Work**
 **Limitations**
- Personal Dataset: Results are based on my attendance behavior and may not generalize to other students.
- Unaccounted External Factors: Class schedule changes, exam periods, or personal reasons could influence attendance.
- Short-Term Study: The dataset will only cover a limited timeframe.

 **Future Work**
- Expanding the study to multiple students to obtain generalized patterns.
- Integrating real-time shuttle tracking data for improved accuracy.
- Exploring university-wide attendance data to validate findings.

---

 **Conclusion**
This project will analyze the impact of weather conditions on my class attendance, using shuttle usage as an indirect indicator. The findings could provide insights into student commuting behavior, potentially informing university policies on transportation and attendance strategies in response to extreme weather conditions.

---
