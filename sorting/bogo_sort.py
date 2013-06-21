#!/usr/bin/python
import random

# Famous stupid sort.
# http://en.wikipedia.org/wiki/Bogosort

def isInOrder(l):
    for idx, val in enumerate(l):
        if idx == 0: continue
        if val < l[idx - 1]: return False
    return True

def bogoSort(l):
    while True:
        # shuffle list
        random.shuffle(l)

        if isInOrder(l):
            return l

if __name__ == '__main__':
     input_list = [5,4,3,2,1]

     print "Test passed" if bogoSort(input_list) == [1,2,3,4,5] else "Test Failed"
