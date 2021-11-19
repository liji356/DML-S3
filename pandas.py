import pandas as pd
weather={'day':['1/1/19','3/1/19','2/3/21'],
          'city':['TVM','KTM','Palakad'],
         'temp':['3','33','35'],
         'Humidity':['41','21','75'] }
df=pd.DataFrame(weather)
df.head(2)
df.tail(2)
df[0:3]
df['temp'].max()
g=df.groupby(['city'])
for city in g:
  print(city)
