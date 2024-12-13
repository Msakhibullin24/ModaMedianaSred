import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
import seaborn as sbn
import math

# Монета подбрасывается 3 раза. Интересующая нас случайная величина - количество выпадений орла
# 0 - решка, 1 - орел
coin = [0, 1]
# количество подбрасываний монеты
count = 3
# мат. ожидание и дисперсия генеральной совокупности
rv = sps.binom(n=3, p=0.5)
mu = rv.mean()
sigma2 = rv.var()

# Рассмотрим, как меняется распределение средних при разных объемах выборки
n = 100  # можно запустить при разных значениях n: 5, 10, 20, 30
# Число симуляций (количество выборок)
N = 1000
means = [] # в этот список будем сохранять средние арифметические по выборкам
for j in range(N):
    sample_mean = 0
    for i in range(n):
        value = 0
        for _ in range(count):  # вычисляем количество выпадений орла при 3х подбрасываниях
            value += np.random.choice(coin)
        sample_mean += value
    sample_mean /= n    # вычислили среднее арифметическое по выборке
    means.append(sample_mean) # сохранили в выборку средних

norm_rv = sps.norm(loc=mu, scale=math.sqrt(sigma2 / n)) # нормальное распределение в соответствии с ЦПТ

sbn.ecdfplot(means) # график эмпирической функции распределения
x = np.linspace(min(means), max(means))
y = norm_rv.cdf(x)  # функция нормального распределения
plt.plot(x, y, color='r')
plt.show()
