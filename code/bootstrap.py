import pandas as pd
import numpy as np

def values_and_weights(filename):
	cols = ['rating', 'count']
	data = pd.read_csv(filename, header=None, names=cols)
	counts = data['count']
	ratings = data['rating']
	return ratings, counts

def bootstrap(values, weights=None, n=1, replace=True):
	sample = values.sample(n=n, replace=replace, weights=weights)
	sample = sample.value_counts()
	sample.to_csv('../bootstrapped_data.csv', index=False)

def load_bootstrap_sample(filename):
	data = pd.read_csv(filename, header=None)
	indices = np.flip(np.arange(1, len(sample) + 1))
	data.index = indices
	return data
