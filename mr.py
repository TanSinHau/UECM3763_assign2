import pylab as p
import numpy as np

#setup parameters
alpha = 1; theta = 0.064; sigma = 0.27; R0 = 3; 
n_path = 1000 #simulation of 1000 runs
n = n_partitions = 1000 #number of partitions within interval

#create Brownian Paths
t = p.linspace(0, 1, n+1)[:-1] 
dt = 1 / n
dB = p.randn(n_path, n+1) * p.sqrt(dt);  dB[:,0] = 0;
B = dB.cumsum(axis=1);

#generate R
R = p.zeros_like(B)
R[:,0] = R0
for col in range(n):
    R[:,col+1] = R[:,col] + (theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]
     
#plot 5 realizations  
R_plot= R[0:5,:-1]
p.plot(t,R_plot.transpose());
p.xlabel('Time, $t$');
p.ylabel('$R_t$');
p.title('5 Realizations of Mean Reversal Process with $\\alpha$ = '+ str(alpha)+'\n $\\theta$ = '+str(theta)+' and $\\sigma$ ='+str(sigma))
p.show()

#calculate the expectation value of R(1) 
R1 = p.array(R[:,-1]);
E_R1 = np.mean(R1)
print('Expected Value: E[R(1)] = ' + str(E_R1))

#calculate P[R(1)> 2]
Prob = sum(R1 > 2) / n_path
print('P[R(1)> 2] = ' + str(Prob)) 