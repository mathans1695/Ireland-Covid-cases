import pandas as pd
import matplotlib.pyplot as plt
import shapefile
from color import get_color
from latest_cases import LatestCases

# instantiating LatestCases, pass path and number of counties
latest_cases = LatestCases('data/cases_by_county_ireland.csv', 26)

# location of each county(latitude and longitude)
loc_col_names = ['CountyName', 'Long', 'Lat']
location = latest_cases.location(loc_col_names)

# county wise covid confirmed cases proportion
prop_col_names = ['CountyName', 'ConfirmedCovidCases']
county_proportion = latest_cases.county_wise_proportion(prop_col_names)

# store the shapefile Reader object to sf
sf = shapefile.Reader("map/counties.shp")
shapes = sf.shapes()
records = sf.records()

def get_longitude_and_latitude(points):
	longitude = []
	latitude = []
	
	# appending first point
	longitude.append(points[0][0])
	latitude.append(points[0][1])
	
	# appending remaining points
	for i in range(1, len(points)):
		longitude.append(points[i][0])
		latitude.append(points[i][1])
		
		# stops, when polygon reaches it's starting point
		if(longitude[0] == points[i][0] and latitude[0] == points[i][1]):
			break
			
	return (longitude, latitude)
	
def plot_text(df, name):
	plt.text(
		df['Long'],
		df['Lat'], 
		name, 
		horizontalalignment='center',
		verticalalignment='center', 
		fontsize=8, 
		fontweight='bold'
	)

# plot a single shape
# pass shape and record object as params
def plot_shape(shape=None, record=None):
	points = shape.points
	county_name = record.NAME_TAG
	
	# Storing longitude and latitude in separate variables
	x_long, y_lat = get_longitude_and_latitude(points)
	
	# get the current county data from location dataframe
	cur1 = location[location.CountyName == county_name]
	
	if len(cur1.index):
		plot_text(cur1, county_name)
		plt.plot(x_long, y_lat, color='black')
	
	# get current county data from county_proportion dataframe
	cur2 = county_proportion[county_proportion.CountyName == county_name]
	if len(cur2.index):
		color = get_color(cur2.ConfirmedCovidCases.item(), 'red')
		plt.fill(x_long, y_lat, color=color)
	
def plot_map(sf, figsize = (11,9)):
	plt.figure(figsize = figsize)
	
	for shape in sf.shapeRecords():
		plot_shape(shape.shape, shape.record)
	
	plt.title('Ireland County-wise Covid Cases in Proportion')
	plt.xlabel('Longitude')
	plt.ylabel('Latitude')
	
	plt.show()

plot_map(sf)

sf.close()
	