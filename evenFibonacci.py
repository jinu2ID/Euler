'''
Created on Jul 20, 2015

@author: c63937
'''

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        #print(a)
    return a

sum = 0
i = 0
tracker = 0

while(tracker < 4000000):
    tracker = fib(i)
    if tracker % 2 == 0:
        sum += tracker
    i += 1
     
print(sum)

print(fib(33))