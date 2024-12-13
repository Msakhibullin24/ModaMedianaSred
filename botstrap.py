from scipy.stats import bootstrap

sample = [185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171]

sample = (sample,)  # samples must be in a sequence
res_mean = bootstrap(sample, np.mean, confidence_level=0.9)
res_std = bootstrap(sample, np.std, confidence_level=0.9)
print("Доверительный интервал для среднего: \n", res_mean.confidence_interval)
print("Доверительный интервал для стандартного отклонения: \n", res_std.confidence_interval)
