import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Show the first 5 rows
print(df.head())

# Show the column names
print(df.columns)

print(df['Sport'].value_counts().head())

print(df['Sex'].value_counts())

print(df.describe())

print(df['NOC'].nunique())
print(df['NOC'].unique())

# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(older_athletes[['Name', 'Age', 'Sport']].head())


# Athletes from Australia in Swimming
combo_filter = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
print(combo_filter[['Name', 'Team', 'Sport']].head())

# Sort by height
sorted_by_height = df.sort_values(by='Height', ascending=False)
print(sorted_by_height[['Name', 'Height', 'Sport']].head())

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head())

# Count missing values in each column
print(df.isnull().sum())

# Drop rows missing both height and weight
df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)

# Fill missing medals with 'None'
df_cleaned['Medal'] = df_cleaned['Medal'].fillna('None')

# Fill missing ages with average age
avg_age = df_cleaned['Age'].mean()
df_cleaned['Age'] = df_cleaned['Age'].fillna(avg_age)
import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Count missing values in each column
print(df.isnull().sum())

print("")
print("")
print("")


# Drop rows missing both height and weight
df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)

print("")
print("")
print("")

# Fill missing medals with 'None'
df_cleaned.loc[:, 'Medal'] = df_cleaned['Medal'].fillna('None')

# Fill missing ages with average age
avg_age = df_cleaned['Age'].mean()
df_cleaned.loc[:, 'Age'] = df_cleaned['Age'].fillna(avg_age)

print(df_cleaned.head())
# Unique values in 'Sex' and 'Medal'
print(df_cleaned['Sex'].unique())
print(df_cleaned['Medal'].unique())
# Check again for missing values

print(df_cleaned.isnull().sum())

# Get stats after cleaning
print(df_cleaned.describe())
# Save your cleaned version
df_cleaned.to_csv("athlete_events_cleaned.csv", index=False)