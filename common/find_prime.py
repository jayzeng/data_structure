#!/usr/bin/python
import random

# Find a prime number

def findPrime(l):
    for i in range(2,8):
        l = filter(lambda x:x == i or x % i and x > 0, l)
    return l

if __name__ == '__main__':
     input_list = [100,5,4,3,2,1,-1,101]
     print "Test passed" if findPrime(input_list) == [5,3,2,1,101] else "Test Failed"
