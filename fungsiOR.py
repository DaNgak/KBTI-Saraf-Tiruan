from random import choice
from numpy import array, dot, random
from matplotlib import pyplot as plt
# fungsi matematika
unit_step = lambda y: 0 if y < 0 else 1
# dua entri pertama pada array adalah nilai inputan, entri ketiga pada array adalah nilai bias/threshold
data_training = [ # data training adalah fungsi OR
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 1),
    (array([1, 0, 1]), 1),
    (array([1, 1, 1]), 1),
]
# pemilihan 3 angka acak antara 0 dan 1 sebagai initial weight
w = random.rand(3)
errors = [] # menyimpan nilai error untuk dapat di visualisai
teta = 0.2 # variabel pengontrol learning rate
n = 100 # jumlah banyaknya learning iterations
# training process
for i in range(n):
    y, expected = choice(data_training)
    result = dot(w, y)
    error = expected - unit_step(result)
    errors.append(error)
    w += teta * error * y # learning rule
# Hasil pembelajaran (fungsi logika OR)
for y, _ in data_training:
    result = dot(y, w)
    print("{}: {} -> {}".format(y[:2], result, unit_step(result)))
# Visualisasi proses training (plot errors)
plt.ylim([-1, 1])
plt.plot(errors)
plt.show()

