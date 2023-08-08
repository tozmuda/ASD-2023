# from egz1btesty import runtests
from queue import Queue
from collections import deque

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):

  # wypełniam tablicę szerokości
  widths=[]
  q=deque()
  q.append((T, 0))
  while q:
    v, h = q.popleft()
    v.x=h
    if(len(widths)==h): widths.append(1)
    else: widths[h]+=1

    if v.right: q.append((v.right, h+1))
    if v.left: q.append((v.left, h+1))

  # rekurencyjnie dla każdego wierzchołka wyliczam wysokość najdłuższego dziecka
  def rek(v):
    if v.left!=None or v.right!=None:
      res=0
      if v.right!=None:
        max_ch=rek(v.right)
        res=max(res, max_ch)
      if v.left!=None:
        max_ch=rek(v.left)
        res=max(res, max_ch)
      v.x=res
      return v.x
    else:
      return v.x
  rek(T)


  # Wyznaczam największą szerokość
  max_ind=None
  max_width=0
  for i in range(len(widths)):
    if widths[i]>=max_width:
      max_width=widths[i]
      max_ind=i

  # usuwam krawędzie
  q=deque()
  q.append((T, 0))
  deleted=0
  while q:
    v, h=q.popleft()
    if h!=max_ind:
      if v.right:
        if v.right.x<max_ind: deleted+=1
        else: q.append((v.right, h+1))
      if v.left:
        if v.left.x<max_ind: deleted+=1
        else: q.append((v.left, h+1))
    else:
      if v.right: deleted+=1
      if v.left: deleted+=1

  return deleted


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( wideentall, all_tests = False )