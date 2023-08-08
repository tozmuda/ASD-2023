# from egzP4btesty import runtests
from math import inf

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None


def sol(root, T):
  sum=0
  for i in range(len(T)):
    w=T[i].key
    v=root
    max_smaller=-inf

    while v!=None:
      if v.key<w:
        max_smaller=max(max_smaller, v.key)
        v=v.right
      else:
        v=v.left

    v=root
    min_bigger=inf
    while v!=None:
      if v.key>w:
        min_bigger=min(min_bigger, v.key)
        v=v.left
      else:
        v=v.right
    if min_bigger+max_smaller==2*w:
      sum+=w
    
  return sum
    
# runtests(sol, all_tests = True)