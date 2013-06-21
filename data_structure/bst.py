#!/usr/bin/python
# Binary Search Tree

def isBst(node, min_val, max_val):
    if not node:
        return True
    else:
        if not(min_val < node.key and node.key < max_val):
            return False
        if not isBst(node.left, min_val, node.key):
            return False
        return isBst(node.right, node.key, max_val)

class node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

if __name__ == '__main__':
    n = node(8)

    print "Test passed" if isBst(n, 7, 9) else "Test Failed"
    print "Test passed" if not isBst(n, 9, 9) else "Test Failed"
    print "Test passed" if not isBst(n, 12, 1) else "Test Failed"
