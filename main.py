import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import pearsonr, ttest_ind

# 1. Load Data
file_path = "final_merged_attendance_weather.csv"
df = pd.read_csv(file_path, parse_dates=["date"])

# 2. Data Cleaning
print("Missing values:")
print(df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)

# 3. Correlation Analysis
correlation_matrix = df[["attendance", "tempmax_c", "tempmin_c", "precip"]].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# 4. Visualizations
# Attendance vs Max Temp
plt.figure(figsize=(8, 6))
sns.scatterplot(x="tempmax_c", y="attendance", data=df)
plt.title("Attendance vs Max Temperature")
plt.xlabel("Max Temperature (°C)")
plt.ylabel("Attendance")
plt.show()

# Attendance vs Precipitation
plt.figure(figsize=(8, 6))
sns.scatterplot(x="precip", y="attendance", data=df)
plt.title("Attendance vs Precipitation")
plt.xlabel("Precipitation (mm)")
plt.ylabel("Attendance")
plt.show()

# Attendance over Time
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['attendance'], marker='o')
plt.title("Attendance Over Time")
plt.xlabel("Date")
plt.ylabel("Attendance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Attendance by Weather Type
df["weather_type"] = df["conditions"].str.extract(r"^(Snow|Rain)").fillna("Clear/Cloudy")
plt.figure(figsize=(8, 6))
sns.boxplot(x="weather_type", y="attendance", data=df)
plt.title("Attendance by Weather Type")
plt.xlabel("Weather Type")
plt.ylabel("Attendance")
plt.show()

# 5. Regression Analysis
X = df[["tempmax_c", "precip"]]
y = df["attendance"]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

# 6. Hypothesis Testing
# Define cold and wet days
df["cold"] = df["tempmax_c"] < 10
df["wet"] = df["precip"] > 0.2
df["cold_and_wet"] = df["cold"] & df["wet"]

group_a = df[df["cold_and_wet"]]["attendance"]
group_b = df[~df["cold_and_wet"]]["attendance"]

# T-test
t_stat, p_val = ttest_ind(group_a, group_b, equal_var=False)
print("T-statistic:", t_stat)
print("P-value:", p_val)
print("Group A size:", len(group_a))
print("Group B size:", len(group_b))

# 7. Additional Analysis
# Attendance by Weekday
df["weekday"] = df["date"].dt.day_name()
plt.figure(figsize=(8,6))
sns.barplot(x="weekday", y="attendance", data=df,
            order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
plt.title("Average Attendance by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Attendance")
plt.tight_layout()
plt.show()

# Weekly Precipitation Trend
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["precip"], marker="o", color="blue")
plt.title("Weekly Precipitation Trend")
plt.xlabel("Date")
plt.ylabel("Precipitation (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
