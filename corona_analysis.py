import pandas as pd
import matplotlib.pyplot as plt
import shapefile
from color import get_manual_color
from latest_cases import LatestCases
from pallete_legend import pallete_legend

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

# set border color and pallete color
border_color = 'white'
pallete_color = 'brown'
font_color = 'black'


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
	
def plot_text(ax, df, name):
	ax.text(
		df['Long'],
		df['Lat'], 
		name, 
		horizontalalignment='center',
		verticalalignment='center', 
		fontsize=8, 
		fontweight='bold',
		color=font_color
	)

# plot a single shape
# pass shape and record object as params
def plot_shape(ax, shape=None, record=None):
	points = shape.points
	county_name = record.NAME_TAG
	
	# Storing longitude and latitude in separate variables
	x_long, y_lat = get_longitude_and_latitude(points)
	
	# get the current county data from location dataframe
	cur1 = location[location.CountyName == county_name]
	
	if len(cur1.index):
		plot_text(ax, cur1, county_name)
		ax.plot(x_long, y_lat, color=border_color)
	
	# get current county data from county_proportion dataframe
	cur2 = county_proportion[county_proportion.CountyName == county_name]
	if len(cur2.index):
		color = get_manual_color(
			cur2.ConfirmedCovidCases.item(), 
			pallete_color
		)
		ax.fill(x_long, y_lat, color=color)
	
def plot_map(sf, figsize = (11,9)):
	fig, axes = plt.subplots(1, 2, gridspec_kw={'width_ratios': [25, 1]}, sharex=False, sharey=False, figsize=(19.2, 10.8))
	
	# plotting color pallete
	pallete_legend(axes[1], pallete_color)
	
	for shape in sf.shapeRecords():
		plot_shape(axes[0], shape.shape, shape.record)
	
	axes[0].title.set_text('Ireland County-wise Covid Cases in Proportion')
	axes[0].set_xlabel('Longitude')
	axes[0].set_ylabel('Latitude')
	
	plt.savefig('output/Ireland_covid_stat.png')
	plt.show()

plot_map(sf)

sf.close()
	