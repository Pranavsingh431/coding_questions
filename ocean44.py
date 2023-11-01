import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
#here we are importing matpolib,numpy and pandsa
data = pd.read_csv("c:/Users/sharm/Downloads/archive.zip")
#here we are putting the data
heights = data['Height(Inches)']
#relation between height and weight is calculated
weights = data['Weight(Pounds)']
correlation = heights.corr(weights)
print(f"{correlation:.3f}")

plt.scatter(heights,weights,alpha=0.5,label='Data Points')
fit = np.polyfit(heights,weights,deg=1)
fit_fn= np.poly1d(fit)


plt.plot(heights,fit_fn(heights),'r',label='Fitted line')
plt.xlabel('Height')
plt.ylabel('Weight')
#here this wll take value
plt.title('Height vs Weight')
plt.legend()
#for graph plot

plt.show()