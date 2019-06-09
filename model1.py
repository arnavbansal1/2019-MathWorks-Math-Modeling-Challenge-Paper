import numpy as np
'''
Matrix A is formatted as such 

S_0 	0    S_0(1-S_0-V_0) 	-S_0 V_0 
S_1 	0    S_1(1-S_1-V_1) 	-S_1 V_1
and so on
0 		V_0  V_0(1-S_0-V_0)		S_0 V_0  
0 		V_1  V_1(1-S_1-V_1)		S_1 V_1 
and so on

Vector b is just
[S_1 S_2 ... V_1 V_2 ...]

The output x is just
1-mu  1-xi  alpha  beta  gamma
'''
A = np.genfromtxt("matrix.csv", delimiter=",")
b = np.genfromtxt("vector.csv")
x = np.linalg.inv(np.matmul(A.T, A)).dot(A.T.dot(b)) 

# Comparing predictions to actual data
for i in range(len(b)):
	print(i, b[i], A.dot(x)[i])

# 2018 data below
s = [0.148739194]
v = [0.04210568085]


for i in range(10):
	s.append((x[0]*s[-1] + x[2]*s[-1]*(1-s[-1]-v[-1])) - x[4]*s[-1]*v[-1])
	v.append((x[1]*v[-1] + x[3]*v[-1]*(1-s[-1]-v[-1])) + x[4]*s[-1]*v[-1])

for i in range(len(s)):
	print(s[i], v[i])

# Searching for steady-state solution
for i in range(100):
	s.append((x[0]*s[-1] + x[2]*s[-1]*(1-s[-1]-v[-1])) - x[4]*s[-1]*v[-1])
	v.append((x[1]*v[-1] + x[3]*v[-1]*(1-s[-1]-v[-1])) + x[4]*s[-1]*v[-1])
print(s[-1])
print(v[-1])
