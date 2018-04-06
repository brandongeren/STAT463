import pandas as pd

# this function takes as an argument the raw UCSD cell phone data
# it then converts it into an aggregate
# the aggregate has 5 rows: the ratings 1 through 5, and the frequency of each of those ratings
def aggregate_data(file_location):
	cols = ['unimportant1', 'unimportant2', 'rating', 'unimportant4']
	data = pd.read_csv(file_location, header=None, names=cols)
	data = data['rating']
	aggregates = data.value_counts()
	aggregates.to_csv('../amazon_data.csv', index=False)
