# importing pandas package
import pandas as pd

#reading our csv into the variable df

df = pd.read_csv('Desktop/Resources/cities.csv')

#changing our info to df
df.to_html('data.html', index=False)
# this will save data to file

#saved data has been asigned to string and html
table = df.to_html()

#Checking if it printed correctly
print(table)

#Learned this cool code to export it to an html so it's not that messy
#It was exported to USER
df.to_html('table.html')
