import numpy as  np
import matplotlib.pyplot as plt

class Queue:
    def __init__(self,total, minutes, type , mu, std):
        self.type = type
        self.total = total
        self.minutes = minutes
        self.mu = mu 
        self.std = std

    def time(self):
        time = list(range(0,self.minutes+1))
        return time 
    
    def distribution(self):
        
        if self.type == 'Normal':
            f1= 1/(self.std * (2*np.pi)**(1/2))
            norm = []
            for i in self.time():
                norm.append(f1* np.exp(-0.5 * ((i-self.mu)/self.std)**2 ))

            norm = [ int(i * self.total) for i in norm]
            scale  = self.total/sum(norm)
            norm = [ int(i * scale) for i in norm]
            
            return norm
        
        elif self.distribution != 'Normal':
            return 'Error Distribution'
        
    def len_queue(self, server):
        
        len_line = []
        distr = self.distribution() 
        len_line.append(distr[0])

        i=1
        validation = False

        
        while validation == False:
           
            if i <= (len(distr)-1):
                if len_line[i-1] <= 0:
                    add =  distr[i]
                    len_line.append(add)
                else:
                    add = len_line[i-1]+ distr[i] - server
                    if add < 0:
                        add=0
                    len_line.append(add)
            else:
                if len_line[i-1] <= 0:
                    validation = True
                else :
                    add = len_line[i-1] - server
                    if add < 0:
                        add =0 
                    len_line.append(add)            
            i = i+1

        return len_line 


hour = 3 
minutes = 3*60

test = Queue(1000,minutes,'Normal',minutes/2, 30)

line = test.len_queue(5)

plt.plot(list(range(0, len(line))),line)
plt.show()
    


