# from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def knapsack(dp, S, C, V, i):
  if S<0: return -inf
  if i>=len(C): return 0
  if dp[i][S]!=None: return dp[i][S]
  d1=knapsack(dp, S-C[i], C, V, i+1) + V[i]
  d2=knapsack(dp, S, C, V, i+1)
  dp[i][S]=max(d1, d2)
  return dp[i][S]


def wybory(T):
  sum=0
  
  for el in T:
    S=el.fundusze
    C=[]
    V=[]
    p=el
    while p!=None:
      V.append(p.wyborcy)
      C.append(p.koszt)
      p=p.next

    dp=[[None for _ in range(S+1)] for _ in range(len(C))]
    sum+=knapsack(dp, S, C, V, 0)
  return sum


# runtests(wybory, all_tests = True)