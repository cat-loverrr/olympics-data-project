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