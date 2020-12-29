import pandas as pd
import shapefile

class LatestCases:
	'''LatestCases deal with latest covid cases
		params -> path to csv
		params -> number of counties/district present in csv file'''
		
	def __init__(self, path, num_of_counties):
		'''create pandas dataframe and store it in df variable
		get latest data using tail method of dataframe'''
		
		self.df = pd.read_csv(path)
		self.latest = self.df.tail(num_of_counties)
		
	def location(self, column_names):
		'''returns dataframe containing latitude and longitude of each county
		expects list of 3 column names'''
		
		return self.latest[[
			column_names[0], 
			column_names[1], 
			column_names[2]
		]]
		
	def sum(self, column_name):
		'''returns total sum of passed column name
		expects column name as string'''
		
		return self.latest[column_name].sum()

	def proportion(self, column_name):
		'''returns pandas series containing proportion of confirmed cases from total cases'''
		
		return self.latest[column_name] / self.sum(column_name) * 100
		
	def county_wise_proportion(self, column_names):
		'''accepts list of 2 column names -> countyName column and 
		confirmedcase column name should be passed
		
			returns pandas dataframe containing column_names[0] 
		column and calculated column_names[1] column on each county
		Note: column_names[1] is proportion of total cases'''
		
		return pd.DataFrame([
			self.latest[column_names[0]], 
			self.proportion(column_names[1])
		]).transpose()