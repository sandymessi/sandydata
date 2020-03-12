
import os
print(os.getcwd())
import pandas aspd
df = pd.read_csv("Long_Lats.csv", delimiter=',', skiprows=0, low_memory=False)


import matplotlib.pyplot as plt
plt.scatter(x=df['Latitude'], y=df['Longitude'])
plt.show()