import numpy as np
import matplotlib.pyplot as plt

ARRAY_LEN = 10000
NUM_OF_ARRAYS = 10

x = np.random.rand(ARRAY_LEN)
for i in range(0, NUM_OF_ARRAYS - 2):
    x +=  np.random.rand(ARRAY_LEN)

num_bins = 10
n, bins, patches = plt.hist(x, num_bins)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')

plt.show()