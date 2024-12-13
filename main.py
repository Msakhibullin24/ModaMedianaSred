# Расчёт моды, медианы и среднего с помощью библиотек numpy и scipy
import numpy as np
from scipy import stats
sample = np.array([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])
# в numpy почему-то нет моды
print('mode:', stats.mode(sample))
print('median:', np.median(sample))
print('mean:', np.mean(sample))
print(len(sample))
