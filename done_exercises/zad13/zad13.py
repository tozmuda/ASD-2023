# from egzP2btesty import runtests
from math import log10

class Node:
    def __init__(self, val=0):
        self.val=val
        self.right=None
        self.left=None

def append_right(root: Node):
    new=Node(0)
    root.right=new

def append_left(root: Node):
    new=Node(0)
    root.left=new

def build_tree(root: Node, word):
    while len(word)>=0:
        root.val+=1
        if len(word)>0:
            c=word[len(word)-1]
            if c=='1':
                if root.right==None: append_right(root)
                root=root.right
            if c=='0':
                if root.left==None: append_left(root)
                root=root.left
            word=word[0:len(word)-1]
        else: break

def find_val(root: Node, word):
    for i in range(len(word)-1, -1, -1):
        if root==None:
            return 1
        c=word[i]
        if c=='1':
            root=root.right
        elif c=='0':
            root=root.left
    return root.val


def kryptograf( D, Q ):    
    root=Node(0)
    for i in range(len(D)):
        build_tree(root, D[i])
    product=0
    for i in Q:
        product+=log10(find_val(root, i))
    return product

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
# runtests(kryptograf, all_tests = 3)