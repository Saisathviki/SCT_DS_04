import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Load the dataset
file_path = "archive/US_Accidents_March23.csv"  # Updated path
df = pd.read_csv(file_path)

# Display basic info
print(f"Dataset Shape: {df.shape}")
print(f"Column Names: {df.columns}")

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Convert time columns to datetime format with 'mixed' format handling
df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='mixed', errors='coerce')
df['End_Time'] = pd.to_datetime(df['End_Time'], format='mixed', errors='coerce')

# Check for any NaT values after conversion
print("\nMissing datetime values:")
print(df[['Start_Time', 'End_Time']].isna().sum())

# Additional analysis (optional)
print("\nSeverity Level Distribution:")
print(df['Severity'].value_counts())

# Save the cleaned dataset
df.to_csv("archive/cleaned_US_Accidents.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_US_Accidents.csv'.")

road_factors = ['Crossing', 'Junction', 'Traffic_Signal', 'Bump', 'Railway']
road_accidents = df[road_factors].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=road_accidents.index, y=road_accidents.values, palette='coolwarm')
plt.title('Accidents Related to Road Conditions')
plt.xlabel('Road Condition Factor')
plt.ylabel('Number of Accidents')
plt.show()

weather_counts = df['Weather_Condition'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=weather_counts.index, y=weather_counts.values, palette='viridis')
plt.title('Top 10 Weather Conditions in Accidents')
plt.xlabel('Weather Condition')
plt.xticks(rotation=45)
plt.ylabel('Number of Accidents')
plt.show()

df['Hour'] = df['Start_Time'].dt.hour
plt.figure(figsize=(12, 6))
sns.countplot(x=df['Hour'], palette='magma')
plt.title('Accidents by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()

top_cities = df['City'].value_counts().head(5)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_cities.index, y=top_cities.values, palette='rocket')
plt.title('Top 5 Cities with Most Accidents')
plt.xlabel('City')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Severity'], y=df['Temperature(F)'], palette='coolwarm')
plt.title('Impact of Temperature on Accident Severity')
plt.xlabel('Severity Level')
plt.ylabel('Temperature (F)')
plt.show()