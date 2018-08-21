# -*- coding: utf-8 -*-
import pandas as pd
ds1=pd.read_csv('movie_metadata.csv',encoding="ISO-8859-1")
ds1.head()
ds1.shape
ds1.info()
ds1.imdb_score.describe()
ds1['movie_title']   # display movie_title column
ds1['duration'][:10]  # First 10 records of duration column
ds1[['budget','gross']] # select multiple columns
ds1[ds1['duration'] > 120] # select movie more than 2 hr duration

### Remove incomplete rows ####
ds1.country=ds1.country.fillna('') # Will put empty string
ds1.duration=ds1.duration.fillna(ds1.duration.mean()) # will put mean value of duration table
ds1.dropna() # Dropping all rows with any NA values 
ds1.dropna(how='all') # drop rows that have all NA values
ds1.dropna(thresh=5) # at least 5 non-null values, and greater than that will be deleted
ds1.dropna(subset=['title_year'])  # don’t want to include any movie that doesn’t have information on when the movie came out

### Deal with error-prone columns ###
### axis=1 for Column and axis=0 for row it is default

ds1.dropna(axis=1, how='all') # drop the columns with that are all NA values
ds1.dropna(axis=1, how='any') # Drop all columns with any NA values
import matplotlib.pyplot as plt
fig=plt.gcf()
plt.plot()
fig=savefig("mvgraph.png")
