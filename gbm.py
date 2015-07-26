import pylab as p
import numpy as np

#setup parameters
mu = 0.1; sigma = 0.26; S0 = 39;
n_path = 1000 #simulation of 1000 runs
n = n_partitions = 1000 #number of partitions within interval

#create Brownian Paths
t = p.linspace(0,3,n+1);
dB = p.randn(n_path,n+1) / p.sqrt(n/3); dB[:,0] = 0;
B=dB.cumsum(axis=1);

#calculate stock prices
nu = mu - sigma*sigma/2.0
S = p.zeros_like(B); S[:,0] = S0
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:])

#plot 5 realizations
S_plot = S[0:5]
p.plot(t,S_plot.transpose());
p.xlabel('Time,t')
p.ylabel('Stock Price, RM')
p.show()

#calculate expectation value and variance of S(3)
S3 = p.array(S[:,-1])
E_S3 = np.mean(S3)
Var_S3 = np.var(S3)
print('Expected Value: E[S(3)] = ' + str(E_S3))
print('Variance: Var[S(3)] = ' + str(Var_S3))

# Calculate P[S(3)> 39]
Prob = sum(S3 > 39) / len(S3 > 39)
print('P[S(3)> 39] = ' + str(Prob))

# Calculate E[S(3) | S(3) > 39]
Exp = sum(S3 * (S3 > 39)) / sum(S3 > 39)
print('E[S(3) | S(3) > 39] = ' + str(Exp))