import pandas as pd
import numpy as np
from estimators import *

def values_and_weights(filename):
	cols = ['rating', 'count']
	data = pd.read_csv(filename, header=None, names=cols)
	counts = data['count']
	ratings = data['rating']
	return ratings, counts

def bootstrap(values, weights=None, n=1, replace=True):
	sample = values.sample(n=n, replace=replace, weights=weights)
	sample.to_csv('../bootstrapped_data.csv', index=False)
	sample = sample.value_counts()
	sample.to_csv('../bootstrapped_data_value_counts.csv', index=False)

def load_bootstrap_sample(filename):
	data = pd.read_csv(filename, header=None)
	indices = np.flip(np.arange(1, len(data) + 1), axis=0)
	data.index = indices
	return data

def bootstrap_estimator(size, n, values, weights=None, replace=True):
	# repeat the sampling n times
	trimeans = []
	harmonic_means = []
	for i in range(n):
		print(i) 
		sample = values.sample(n=size, replace=replace, weights=weights)
		trimean_value = trimean(sample)
		print(trimean_value)
		trimeans.append(trimean_value)
		harmonic_mean_value = harmonic_mean(sample.value_counts())
		print(harmonic_mean_value)
		harmonic_means.append(harmonic_mean_value)
	return trimeans, harmonic_means
