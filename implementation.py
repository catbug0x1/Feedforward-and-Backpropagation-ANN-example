import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

i1,i2=0.05,0.10
t1,t2=0.01,0.99

w1,w2,w3,w4=0.15,0.20,0.25,0.30
w5,w6,w7,w8=0.40,0.45,0.50,0.55

b1,b2=0.35,0.60
lr=0.5

# Feedforward
h1=sigmoid(i1*w1+i2*w2+b1)
h2=sigmoid(i1*w3+i2*w4+b1)

o1=sigmoid(h1*w5+h2*w6+b2)
o2=sigmoid(h1*w7+h2*w8+b2)

# Error
E_total=0.5*(t1-o1)**2+0.5*(t2-o2)**2

print("Output:",o1,o2)
print("Total Error:",E_total)