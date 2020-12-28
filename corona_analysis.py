import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import shapefile
from colorpallete import colorpallete

# reading data from csv file, df -> dataframe
df = pd.read_csv('data/cases_by_county_ireland.csv')

# getting latest covid confirmed cases
latest = df.tail(26)
location = latest[[
	'CountyName', 
	'Long', 
	'Lat'
]]

totalCases = latest['ConfirmedCovidCases'].sum()
proportion = latest['ConfirmedCovidCases']/totalCases*100

countyProportion = pd.DataFrame([latest['CountyName'], proportion]).transpose()

# store the shapefile Reader object to sf
sf = shapefile.Reader("map/counties.shp")

shapes = sf.shapes()
records = sf.records()

def getcolor(porportion):
	porp = porportion.item()
	cpallete = colorpallete('red')
	if 0 <= porp < 17:
		return cpallete[0]
	elif 17 <= porp < 34:
		return cpallete[1]
	elif 34 <= porp < 51:
		return cpallete[2]
	elif 51 <= porp < 67:
		return cpallete[3]
	elif 67 <= porp < 84:
		return cpallete[4]
	else:
		return cpallete[5]

# plot a single shape
# pass shape and record object as params
def plot_shape(shape=None, record=None):
	# get bbox and store in bbox variables
	bbox = shape.bbox
	
	# extracting points from shape object
	points = shape.points
	
	# get the county name
	county_name = record.NAME_TAG
	
	# creating an empty array with number of rows equals len(points) and with one column
	x_long = []
	y_lat = []
	
	# extracting longitudes and latitude from points into separate variables
	x_long.append(points[0][0])
	y_lat.append(points[0][1])
	
	for i in range(1, len(points)):
		x_long.append(points[i][0])
		y_lat.append(points[i][1])
		
		if(x_long[0] == points[i][0]):
			if(y_lat[0] == points[i][1]):
				break
	
	# getting location from 
	cur = location[location.CountyName == county_name]
	if len(cur.index):
		plt.text(cur['Long'], cur['Lat'], county_name, horizontalalignment='center', verticalalignment='center', fontsize=8, fontweight='bold')
		
		# plot the map using x and y coordinates
		plt.plot(x_long, y_lat, color='#D8FF93')
		
	current = countyProportion[countyProportion.CountyName == county_name]
	
	if len(current.index):
		color = getcolor(current.ConfirmedCovidCases)
		plt.fill(x_long, y_lat, color=color)
	
	# show grid
	plt.grid()
	
def plot_map(sf, x_lim = None, y_lim = None, figsize = (11,9)):
	plt.figure(figsize = figsize)
	id=0
	for shape in sf.shapeRecords():
		plot_shape(shape.shape, shape.record)
	
	plt.title('Ireland Map')
	plt.xlabel('Longitude')
	plt.ylabel('Latitude')
	
	plt.show()
	
plot_map(sf)

#calling the function and passing required parameters to plot the full map
sf.close()
	