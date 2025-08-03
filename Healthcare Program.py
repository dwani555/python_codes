# covid_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV with raw string to avoid unicode issues
file_path = r"C:\Users\sreenivas\PycharmProjects\PythonProject1\covid_19_clean_complete.csv"
df = pd.read_csv(file_path, parse_dates=["Date"])

# Display basic info
print("Dataset Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Rename columns for consistency
df = df.rename(columns={
    "Country/Region": "Country",
    "Province/State": "State",
    "Confirmed": "ConfirmedCases",
    "Deaths": "DeathCases",
    "Recovered": "RecoveredCases"
})

# Fill missing values
df["State"] = df["State"].fillna("")

# Get the latest date
latest_date = df["Date"].max()
print(f"\n Latest Date in Dataset: {latest_date.date()}")

# ==== 1. Global Trends Over Time ====
global_daily = df.groupby("Date")[["ConfirmedCases", "DeathCases", "RecoveredCases"]].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=global_daily, x="Date", y="ConfirmedCases", label="Confirmed")
sns.lineplot(data=global_daily, x="Date", y="DeathCases", label="Deaths")
sns.lineplot(data=global_daily, x="Date", y="RecoveredCases", label="Recovered")
plt.title("Global COVID-19 Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ==== 2. Top 10 Countries by Confirmed Cases ====
latest_data = df[df["Date"] == latest_date]
country_summary = latest_data.groupby("Country")[["ConfirmedCases", "DeathCases", "RecoveredCases"]].sum()
top_countries = country_summary.sort_values(by="ConfirmedCases", ascending=False).head(10)

print("\nTop 10 Countries by Confirmed Cases:\n", top_countries)

# Melt for barplot
top_countries_plot = top_countries.reset_index().melt(
    id_vars="Country",
    value_vars=["ConfirmedCases", "DeathCases", "RecoveredCases"],
    var_name="CaseType",
    value_name="Count"
)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_countries_plot, x="Country", y="Count", hue="CaseType")
plt.title("Top 10 Countries by COVID-19 Cases (Latest Date)")
plt.xlabel("Country")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==== 3. Country-Specific Trend (e.g., India) ====
selected_country = "India"
country_data = df[df["Country"] == selected_country].groupby("Date")[["ConfirmedCases", "DeathCases", "RecoveredCases"]].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=country_data, x="Date", y="ConfirmedCases", label="Confirmed")
sns.lineplot(data=country_data, x="Date", y="DeathCases", label="Deaths")
sns.lineplot(data=country_data, x="Date", y="RecoveredCases", label="Recovered")
plt.title(f"COVID-19 Trend in {selected_country}")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()