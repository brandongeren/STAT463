import pandas as pd
from bootstrap import *

# This should take as an argument the aggregated dataframe
def harmonic_mean(filename):
	aggregate_data = load_bootstrap_sample(filename)
	aggregate_data = aggregate_data.sort_index()
	counts = aggregate_data[0].values
	inverses = list(map(lambda i:1. / (i+1) * counts[i], range(len(counts))))
	harmonic_mean = sum(counts) / sum(inverses)
	return harmonic_mean

# The argument to this should be the dataframe of the raw bootstrapped data
def trimean(dataframe):
	descriptors = dataframe.describe()
	q1 = data.describe()[0][4]
	q2 = data.describe()[0][5]
	q3 = data.describe()[0][6]
	trimean = (q1 + 2 * q2 + q3) / 4
	return trimean
