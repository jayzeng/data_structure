#!/usr/bin/python
# en.wikipedia.org/wiki/Quicksort

def qsort(L):
    if len(L) <=1 : return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] \
           + qsort([ge for ge in L[1:] if ge >= L[0]])

if __name__ == '__main__':
     input_list = [5,4,3,2,1]

     print "Test passed" if qsort(input_list) == [1,2,3,4,5] else "Test Failed"
