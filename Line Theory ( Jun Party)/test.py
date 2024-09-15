def normal_dist(x, mean, sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

mean = 180 /2 
sd = 60
x = 180

# result = normal_dist(x, mean, sd)
# print(result)

time = list(range(0, 180+1)) 

z_score = (x -  mean)/ sd

prob = np.exp(-0.5* z_score**2)/(2*np.pi)
print(z_score)
print(prob)

# value = []
# for i in time:
#     value.append(normal_dist(i,mean,sd)) 

# print(value)

# print(min(value))

