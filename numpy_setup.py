import numpy as np

world_alcohol = np.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=1)
#print(world_alcohol[1,:])
totals = {}
year_match = world_alcohol[:,0] == '1989'
year = world_alcohol[year_match]
countries = ['Norway','Canada','Mexico','Sweden','Denmark','Vietnam','Finland']
for country in countries:
    is_country = year[:,2] == country
    country_consumption = year[is_country,:]
    alcohol_column = country_consumption[:,4]
    is_empty = alcohol_column == ''
    alcohol_column[is_empty] = "0"
    alcohol_column = alcohol_column.astype(float)
    totals[country] = alcohol_column.sum()
#print(totals)
highest_value = 0
highest_key = None

for key, value in totals.items():
    if value > highest_value:
        highest_value = value
        highest_key = key
print(highest_key, totals[highest_key])
