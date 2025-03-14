# DSA210_Project

## **Project Proposal: The Impact of Weather Conditions on Class Attendance for Off-Campus Students**

###  Introduction
Class attendance is a critical factor in academic success. However, various external factors can influence a student’s decision to attend classes, particularly **weather conditions**.

###  Problem Statement
This project aims to explore the relationship between **weather conditions** and **my class attendance habits**. Since I live off-campus and rely exclusively on the **shuttle service** to commute, my **shuttle usage serves as a direct proxy** for whether I attended class on a given day.

By analyzing historical weather data, my shuttle usage records, and my **class schedule**, I seek to understand:
- How **different weather conditions** (e.g., rain, temperature, wind) impact class attendance.
- Whether **extreme weather** (e.g., heavy rain, storms, extreme cold) significantly reduces attendance.
- If there are **certain classes** that I always attend regardless of the weather.
- Whether **exam weeks affect my attendance decisions**, especially under poor weather conditions.

---

##  Research Questions
This project will address the following key questions:
1. How do **weather variables** (temperature, precipitation, humidity, wind) correlate with my **class attendance**?
2. Can **weather data be used to predict** whether I will attend class?
3. Are there specific **classes that I prioritize**, attending them regardless of weather conditions?
4. During **exam weeks**, does my attendance behavior change even under adverse weather conditions?

---

##  Data Collection

###  **1. Attendance Data (Shuttle Usage & Class Schedule)**
Since I **only use the shuttle when attending classes**, shuttle usage will serve as a **proxy variable** for my class attendance. Additionally, I will track my **daily class schedule** to analyze whether certain courses impact my attendance behavior.

**Data Points Tracked:**
- `date` → The day of the recorded instance.
- `shuttle_used (binary)` → 1 if I took the shuttle (attended class), 0 if I did not (skipped class).
- `departure_time` → The time I left for class.
- `alternative_transportation` → If applicable, which alternative mode I used (walking, bus, etc.).
- `daily_class_schedule` → The list of courses I have on that specific day.
- `exam_week (binary)` → 1 if the day falls within an exam period, 0 otherwise.

### ☁️ü **2. Weather Data**
Weather data will be collected via an API (e.g., OpenWeather) and merged with my attendance dataset.

**Weather Variables Collected:**
- `temperature_min (°C)` → Minimum temperature of the day.
- `temperature_max (°C)` → Maximum temperature of the day.
- `precipitation (mm)` → Amount of rainfall/snowfall.
- `weather_condition` → Categorical (sunny, cloudy, stormy, etc.).

---

##  Methodology & Analysis Plan

- **Visualizing the frequency of class attendance** under different weather conditions.
- Checking **trends over time** (seasonal effects, patterns).
- Using the **information learned in DSA210** to analyze the data properly.
- Identifying **priority classes** that I attend regardless of weather.
- Marking **exam weeks** to determine if attendance changes under poor weather conditions.

---

##  Expected Outcomes
- **Identification of weather conditions** that negatively impact attendance.
- **Potential correlations between extreme weather and skipped classes**.
- **Insights into class prioritization**: Are there classes that I never miss?
- **Exam week trends**: Does bad weather affect my attendance during exams?

---

##  Limitations & Future Work

###  **Limitations**
- **Personal Dataset**: Results are based on my attendance behavior and may not generalize to other students.
- **Unaccounted External Factors**: Class schedule changes, exam periods, or personal reasons could influence attendance.
- **Short-Term Study**: The dataset will only cover a limited timeframe.

###  **Future Work**
- Expanding the study to **multiple students** to obtain generalized patterns.
- Integrating **real-time shuttle tracking data** for improved accuracy.
- Exploring **university-wide attendance data** to validate findings.


---

## 🎯 Conclusion
This project will analyze the **impact of weather conditions on my class attendance**, using **shuttle usage as an indirect indicator** and incorporating **class schedule & exam weeks** for deeper insights. The findings could provide insights into **student commuting behavior, class prioritization, and exam attendance trends in adverse weather conditions**.


