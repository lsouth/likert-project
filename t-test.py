import numpy as np
from samplingFunctions import *
import scipy.stats

num_iterations = 10
treatments = ["control","v1","v2","v3","v4","v5"]
sample_sizes = [30,100,500]
medians = range(1,8)
h0_median = 4

if __name__ == "__main__":

    with open("t-test-one-sided.csv", "w") as f:
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
                            # v1: Errors from Independent Normal not centered at zero, still constant variance.
                            data = sampleIndependentNormal(numSamples=sample_size, offset=median, error_mean=np.random.normal(size=1))
                        if treatment == "v2":
                            # v2: Errors from Independent Normal centered at zero, but non-constant variance.
                            data = sampleIndependentNormalNonConstantVariance(numSamples=sample_size, offset=median)
                        if treatment == "v3":
                            # v3: Errors are independent but drawn from a logistic distribution.
                            data = sampleIndependentContinuousSymmetric(numSamples=sample_size,offset=median)
                        if treatment == "v4":
                            # v4: Errors are dependent and drawn from a Normal distribution.
                            data = generateDependentSamplesLatentNormal(numSamples=sample_size,offset=median)
                        if treatment == "v5":
                            # v5: Errors are independent and from Normal distribution, but data is discretized.
                            data = sampleIndependentNormal(numSamples=sample_size,offset=median,discrete=True)
                        test_result = scipy.stats.ttest_1samp(data,popmean=h0_median)
                        t_stat = test_result[0]
                        two_sided_p_val = test_result[1]
                        one_sided_p_val = two_sided_p_val / 2
                        p_val = one_sided_p_val if t_stat > 0 else 1 - one_sided_p_val
                        p_vals.append(p_val)
                    p_value = np.mean(p_vals)
                    sd = np.std(p_vals)
                    lower = np.percentile(p_vals,5)
                    upper = np.percentile(p_vals,95)
                    f.write("%d,%s,%d,%d,%.9f,%.9f,%.9f,%.9f\n" % (id,treatment,sample_size,median,p_value,sd,lower,upper))
                    id += 1
