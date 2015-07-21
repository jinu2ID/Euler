'''
Created on Jul 21, 2015

@author: c63937
'''
import math

def reverse(n):
    reversed = 0
    while n > 0:
        reversed = 10 * reversed + (n % 10)
        n = int(n/10)
    return reversed

largestPalindrome = 0

for i in range (100, 999):
    
    for j in range (i, 999):
        
        if((reverse(i*j) == i*j) and (i*j > largestPalindrome)):
            
            largestPalindrome = i * j
            

print(largestPalindrome)
