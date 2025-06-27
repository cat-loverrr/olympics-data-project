
# How many columns are in the dataset?

There are fourteen columns.

# Name 3 of them and explain what they represent.

Name - The name of the competitor

Season - What season the games were held in.

Sport - What sport the competitor participated in.

# What do the first 5 rows show?

ID                      Name Sex   Age  Height  Weight            Team  NOC        Games  Year  Season       City          Sport                             Event Medal
0   1                 A Dijiang   M  24.0   180.0    80.0           China  CHN  1992 Summer  1992  Summer  Barcelona     Basketball       Basketball Men's Basketball   NaN
1   2                  A Lamusi   M  23.0   170.0    60.0           China  CHN  2012 Summer  2012  Summer     London           Judo      Judo Men's Extra-Lightweight   NaN
2   3       Gunnar Nielsen Aaby   M  24.0     NaN     NaN         Denmark  DEN  1920 Summer  1920  Summer  Antwerpen       Football           Football Men's Football   NaN
3   4      Edgar Lindenau Aabye   M  34.0     NaN     NaN  Denmark/Sweden  DEN  1900 Summer  1900  Summer      Paris     Tug-Of-War       Tug-Of-War Men's Tug-Of-War  Gold
4   5  Christine Jacoba Aaftink   F  21.0   185.0    82.0     Netherlands  NED  1988 Winter  1988  Winter    Calgary  Speed Skating  Speed Skating Women's 500 metres   NaN


# What are the top 5 sports?
Athletics, Gymnastics, Swimming, Shooting and Cycling.

# How many male vs female athletes?
Theres is 196594 male athletes, and 74522 female athletes.

# What’s the average age?
approx. 25 years old.



# What’s the oldest and youngest athlete?

Oldest - 97 years old.
Youngest - 10 years old.

# Are there any columns with missing or strange values?
Not yet.

# Three country codes
1) AZE - Azerbaijan
2) KSA - Saudi Arabia
3) ROU - Romania



# What’s one thing you learned about the Olympics dataset?
I learnt that you can use code to gain quick information, rather than having to look through the whole thing.

# What did you find challenging in setting up or running Pandas?
At first, the pandas didn't work on my personal laptop, so I had to redownload it and redo everything on the school laptop in order for it to work and use pandas.

# What’s something you'd like to analyse next?
Maybe some financial tables.



# What do these filters do?

The first filter sorts through the data and finds women athletes, whilst the second filter find athletes over the age of 35.

# How many rows were returned? Use len().

Five rows were returned for each filter.

# Write a filter for athletes from Australia in Swimming

# Athletes from Australia in Swimming
combo_filter = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
print(combo_filter[['Name', 'Team', 'Sport']].head())

# Sort by height, then weight.

# Sort by height
sorted_by_height = df.sort_values(by='Height', ascending=False)
print(sorted_by_height[['Name', 'Height', 'Sport']].head())

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head())

# Which 3 columns have the most missing values?
Height, weight and medal.
# Why might this happen in real-world Olympic data?
This might happen when people were unable to obtain the data, or the data wasnt accurate.
# How many rows did you remove?
I removed 206853 rows.
# What are the pros and cons of dropping data?
The pros of dropping data would be being able to use accurate data, but the cons are not having that important data anymore, accurate or not.
# Replace missing Weight with average weight
avg_weight = df_cleaned['Weight'].mean()
df_cleaned['Weight'] = df_cleaned['Weight'].fillna(avg_weight)
# Did cleaning improve the dataset?
Yes, there's now no more missing or incorrect values.
What questions could now be answered more confidently?

# Open the CSV in Excel or Sheets. Is it readable, complete, and useful?
Yes, it is.


# What was the dirtiest column in the dataset?
Medals were the dirtiest column.

# How did you decide when to drop vs fix missing data?

# Why is data cleaning so important in real-world projects?
Data cleaning is important so it's easier to read and get information thats needed.
# Are labels readable?
Yes, they're readable.
# Does the chart title clearly explain what’s shown?
Yes, the title is accurate in what is shown.


