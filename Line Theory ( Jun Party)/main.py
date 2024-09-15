import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt


total = 1000

hour = 3
minutes = hour*60
segundos = minutes*60
time = list(range(0, minutes+1))

def dist_normal(mu, std, t):
    f1= 1/(std * (2*np.pi)**(1/2))
    norm = []

    for i in t:
        norm.append(f1* np.exp(-0.5 * ((i-mu)/std)**2 ))
    
    return norm

def line(arrive, server):
    
    wait_time = []
    len_line = []

    for i in arrive:
        


distr = dist_normal(mu = minutes/2 , std = 30 ,t = time)

distr = [ int(i * total) for i in distr]
print(distr)

    


