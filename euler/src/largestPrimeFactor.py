'''
Created on Jul 20, 2015

@author: c63937
Sieve of Eratosthenes
Find the largest prime factor of 600851475143
'''
a = 600851475143;
b = 2

while(b != a):
    if a % b == 0:
        c = a
        b = 2
        continue
    else:
        b += 1
     
print(c)   