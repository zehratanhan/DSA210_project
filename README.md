# DSA210 Spring 2025 Final Project

**Project Title:** *How Does Weather Affect My Class Attendance?*

**Author:** Zehra Tanhan  
**Course:** DSA210 – Introduction to Data Science  
**Term:** Spring 2024–2025

---

## 🧠 Motivation
As a university student living in Pendik, Istanbul, I noticed that my willingness to attend class seemed to vary with the weather. This project explores whether weather factors like precipitation and temperature have a measurable effect on my class attendance.

---

## 📊 Data Source
- **Attendance Data:** Manually recorded in a CSV file including the date and whether I attended class (1 = yes, 0 = no).
- **Weather Data:** Retrieved using [Visual Crossing Weather API](https://www.visualcrossing.com/).
  - Location: Pendik, Istanbul (40.8902, 29.3773)
  - Time Period: February 10 – April 23, 2025
  - Variables: Daily maximum/minimum temperature, precipitation (mm), weather conditions

---

## 🔍 Exploratory Data Analysis (EDA)
### Summary:
- 50+ days of data were collected.
- Attendance rate was plotted against maximum temperature and precipitation.

### Key Visual Insights:
- Attendance tended to be **lower on colder and wetter days**.
- Scatter plots showed negative trends between attendance and both precipitation and cold temperatures.
- Categorized weather conditions (e.g., Rain, Snow, Clear) revealed that clearer days had higher attendance rates.

---

## 🧪 Hypothesis Testing
### Hypothesis:
- **H0 (Null):** Weather conditions do not affect my attendance.
- **H1 (Alternative):** Attendance is lower on cold (max temp < 8°C) and rainy (precipitation > 0.5 mm) days.

### Test Used:
- Independent samples **t-test** between:
  - Group A: Cold & rainy days
  - Group B: Other days

### Result:
- t = -0.372, p = 0.772
- Group A size: 2 days, Group B size: 48 days

### Conclusion:
- The test **did not find a statistically significant difference** in attendance between the two groups (p > 0.05).
- However, this is likely due to the **very small number of cold and rainy days** in the dataset. With more data, a significant effect might emerge.

---

## 📈 Limitations and Future Work
- **Sample Size:** More data, especially more cold and rainy days, would improve statistical power.
- **External Factors:** Illness, exam schedules, and transportation issues were not accounted for.
- **Improvements:** Automating attendance tracking and expanding to other students would improve generalizability.

---

## 📂 Project Structure
```
├── data/
│   ├── attendance.csv
│   └── weather.csv
├── analysis.ipynb
├── requirements.txt
└── README.md
```

---

## 🔧 Technologies Used
- **Python** (pandas, matplotlib, seaborn, scipy)
- **Visual Crossing API** for weather data
- **Jupyter Notebook** for analysis
- **GitHub** for version control

---

## 🧾 Citation and Academic Integrity
This project was completed individually. All AI assistance was documented. Data was collected and analyzed ethically. No part of the code or results was copied.

> "This project is a personal exploration of how weather may influence daily student behavior using data science."