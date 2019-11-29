import numpy as np
import scipy.stats as stats


def categorize(sample):
	# Restrict sample to likert-range
	sample[sample < 1] = 1
	sample[sample > 7] = 7
	return sample.round()

<<<<<<< HEAD
def restrict(sample):
	sample[sample < 1] = 1
	sample[sample > 7] = 7
	return sample

def sampleIndependentNormal(numSamples=100, offset=0, discrete=False):
	"""
	errors are independently from normal distribution N(0,1)
	"""
	samples = np.random.normal(loc=offset, scale=1, size=numSamples)
	if discrete:
		return categorize(samples)
	return restrict(samples)

def sampleIndependentNormalNonConstantVariance(numSamples=100, offset=0, error_mean=0, discrete=False):
	"""
	errors are independently from normal distribution N(0,1)
	"""
	sigmas = np.random.uniform(1,25,size=numSamples)
	errors = np.random.normal(loc=error_mean, scale=sigmas, size=numSamples)
	sample = errors + offset
	if discrete:
		return categorize(sample)
	else:
		return sample

def sampleIndependentContinuousSymmetric(numSamples=100, offset=0, error_mean=0, discrete = False):
	"""
	errors are independent continuous symmetric: mean=median=0
	Logistic(0,1)
	"""
	errors = np.random.logistic(loc=error_mean, scale=1, size=numSamples)
	samples = offset + errors
	if discrete:
		return categorize(sample)
	return restrict(samples)


def sampleIndependentContinuousAsymmetric(numSamples=100, offset=0, discrete=False):
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
	samples = offset + errors
	if discrete:
		return categorize(samples)
	return restrict(samples)

def generateDependentSamplesLatentNormal(numSamples=100, offset=0, clusterScale=0.25, numClusters=2, discrete=False):
	"""
	draw cluster means from normal distribution
	Then draw samples from each of those clusters
	"""
	clusterMeans = np.random.normal(loc=offset,scale=1,size = numClusters)
	samples = []
	for c in clusterMeans:
	    c_samp = np.random.normal(loc=c,scale=clusterScale,size=int(numSamples/numClusters))
	    samples = np.concatenate((samples,c_samp))
	if discrete:
		return categorize(samples)
	return restrict(samples)

def generateDependentSamplesLatentLogistic(numSamples=100, offset=0, numClusters=2, discrete=False):
	"""
	draw cluster means from logistic distribution
	Then draw samples from Normal distribution centered around each cluster mean
	"""
	clusterMeans = np.random.logistic(loc=offset,scale=1,size = numClusters)
	samples = []
	for c in clusterMeans:
	    c_samp = np.random.normal(loc=c,scale=0.25,size=numSamples / numClusters)
	    samples = np.concatenate((samples,c_samp))
	if discrete:
		return categorize(discrete)
	return restrict(samples)
