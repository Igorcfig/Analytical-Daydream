import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt

x = np.random.poisson(30,10000)

count, bins, ignored = plt.hist(x , 14 , density= True)
plt.show()


