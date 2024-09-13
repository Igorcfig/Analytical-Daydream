import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt


total = 1000
mu = total*0.1

hour = 3 
minutes = hour*60



distr = np.random.normal(mu,minutes)

current_sum = np.sum(distr)
scale = total/current_sum

distr_final = distr*scale
distr_final = np.round(distr_final).astype(int)

print(distr_final.sum(), distr_final[:20])



count, bins, ignored = plt.hist(x , 14 , density= True)
plt.show()

print(x.sum())

# hour = 3


