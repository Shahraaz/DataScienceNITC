from matplotlib import pyplot as plt
years = [1950,1960,1980,1990,2000,2010]
gdp = [300.2,543.6,1075.9,1862.5,5979.6,10289.7]
#create a line chart, years on x axis and gpd on y axis
plt.plot(years,gdp,color="green",marker='o',linestyle="solid")
#add a label to y axis
plt.ylabel("Billions o Dollars")
plt.show()