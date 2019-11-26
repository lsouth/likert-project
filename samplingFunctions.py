import numpy as np
import scipy.stats as stats


def categorize(sample):
	# Restrict sample to likert-range
	sample[sample < 1] = 1
	sample[sample > 7] = 7
	return np.floor(sample)

def sampleIndependentNormal(numSamples=100, offset=0):
	"""
	errors are independently from normal distribution N(0,1)
	"""
	sample = np.random.normal(loc=offset, scale=1, size=numSamples)
	return categorize(sample)

def sampleIndpendentContinuousSymmetric(numSamples=100, offset=0):
	"""
	errors are independent continuous symmetric: mean=median=0
	Logistic(0,1)
	"""
	errors = np.random.logistic(loc=0, scale=1, size=numSamples)
	sample = offset + errors
	return categorize(sample)

def sampleIndependentContinuousAsymmetric(numSamples=100, offset=0):
	"""
	errors are independent, continuous, median=0, but Asymmetric
	Gumbel Distribution:
		parameters: mu: location
					beta: scale
		constant: gamma - Euler- Mascheroni constant ~= 0.577216
		
		mean := mu + beta * gamma
		median := mu - beta * ln(ln(2))
	"""
	# Define Parameters so that median is 0 and mean > 0
	beta = 1
	mu = np.log(np.log(2))
	errors = stats.gumbel_r.rvs(loc=mu, scale=beta, size=numSamples)
	sample = offset + errors
	return categorize(sample)

def generateDependentSamplesLatentNormal(numSamples=100, numClusters=2):
	"""
	draw cluster means from normal distribution
	Then draw samples from each of those clusters
	"""
	clusterMeans = np.random.normal(loc=4,scale=1,size = numClusters)
	samples = []
	for c in clusterMeans:
	    c_samp = np.random.normal(loc=c,scale=0.25,size=numSamples)
	    samples = np.concatenate((samples,c_samp))
	return categorize(samples)

def generateDependentSamplesLatentLogistic(numSamples=100, numClusters=2):
	"""
	draw cluster means from normal distribution
	Then draw samples from each of those clusters
	"""
	clusterMeans = np.random.logistic(loc=4,scale=1,size = numClusters)
	samples = []
	for c in clusterMeans:
	    c_samp = np.random.normal(loc=c,scale=0.25,size=numSamples)
	    samples = np.concatenate((samples,c_samp))
	return categorize(samples)
	    
