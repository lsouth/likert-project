import numpy as np
from samplingFunctions import *
import scipy.stats

num_iterations = 10
treatments = ["control","v1","v2","v3","v4"]
sample_sizes = [30,100,500]
medians = range(1,8)
h0_median = 4

if __name__ == "__main__":

    with open("wilcoxon-test.csv", "w") as f:
        f.write("id,treatment,sample_size,median,p_value,sd,lower,upper\n")
        id = 1
        data = None
        for median in medians:
            for sample_size in sample_sizes:
                for treatment in treatments:
                    p_vals = []
                    for i in range(num_iterations):
                        if treatment == "control":
                            data = sampleIndependentNormal(numSamples=sample_size, offset=median)
                        if treatment == "v1":
                            # v1: Errors are independent and not centered at zero.
                            data = sampleIndependentNormal(numSamples=sample_size, offset=median, error_mean=np.random.normal(size=1))
                        if treatment == "v2":
                            # v2: Errors are independent and from a continuous asymmetric distribution.
                            data = sampleIndependentContinuousAsymmetric(numSamples=sample_size, offset=median)
                        if treatment == "v3":
                            # v3: Errors are dependent and drawn from a Normal distribution.
                            data = generateDependentSamplesLatentNormal(numSamples=sample_size,offset=median)
                        if treatment == "v4":
                            # v4: Errors are independent and from Normal distribution, but data is discretized.
                            data = sampleIndependentNormal(numSamples=sample_size,offset=median,discrete=True)
                        test_result = scipy.stats.wilcoxon(x=data - h0_median,alternative="greater")
                        t_stat = test_result[0]
                        p_val = test_result[1]
                        p_vals.append(p_val)
                    p_value = np.mean(p_vals)
                    sd = np.std(p_vals)
                    lower = np.percentile(p_vals,5)
                    upper = np.percentile(p_vals,95)
                    f.write("%d,%s,%d,%d,%.9f,%.9f,%.9f,%.9f\n" % (id,treatment,sample_size,median,p_value,sd,lower,upper))
                    id += 1
