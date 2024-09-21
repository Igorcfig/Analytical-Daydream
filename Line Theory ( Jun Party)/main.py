import numpy as  np
# import pandas as pd
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
    # print(1)
    
    wait_time = []
    len_line = []
    len_line.append(arrive[0])

    i=1
    validation = False

    # print(i)
    while validation == False:
        # print()
        if i <= (len(arrive)-1):
            if len_line[i-1] <= 0:
                add =  arrive[i]
                len_line.append(add)
            else:
                add = len_line[i-1]+ arrive[i] - server
                len_line.append(add)
        else:
            if len_line[i-1] <= 0:
                validation = True
            else :
                add = len_line[i-1] - server
                len_line.append(add)

            # print('3')
            
         
        i = i+1

    return len_line 


distr = dist_normal(mu = minutes/2 , std = 30 ,t = time)


distr = [ int(i * total) for i in distr]
scale  = total/sum(distr)
# print(sum(distr))
distr = [ int(i * scale) for i in distr]




print(sum(distr))

df = line(distr,5)
print(len(df))

print(df)


plt.plot(list(range(0, len(df))),df)
plt.show()
    
print(len(df))

