import pandas as pd
ds=pd.read_csv('Game_medal.csv',encoding="ISO-8859-1")
ds.head()
ds.tail()
ds.describe()
ds.shape
ds.shift
ds.info
ds.NOC
ds.plot()
import matplotlib.pyplot as plt
plt.plot(ds.Edition)
plt.plot(ds.Edition,label="Year of event ")
plt.plot(ds.Edition,linewidth=2.5,color="blue")
fig=plt.gcf()
ds.plot()
fig=savefig('Dips_18.png')

