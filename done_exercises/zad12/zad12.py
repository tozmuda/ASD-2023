# from egzP1btesty import runtests 
from queue import PriorityQueue
from math import inf

def turysta( G, D, L ):
    size=0
    for v, u, w in G:
        size=max(size, u+1)
    new_G=[[] for _ in range(size)]
    for v, u, w in G:
        new_G[v].append((u, w))
        new_G[u].append((v, w))
    dist=[[inf for _ in range(4)] for _ in range(size)]
    q=PriorityQueue()
    for u, w in new_G[D]:
        dist[u][3]=w
        q.put((w, u, 3))
    while not q.empty():
        w, v, to_go=q.get()
        if dist[v][to_go]==w:
            if to_go==0 and v==L: return w
            elif to_go>0:
                for u1, w1 in new_G[v]:
                    if dist[u1][to_go-1]>w+w1:
                        dist[u1][to_go-1]=w+w1
                        q.put((dist[u1][to_go-1], u1, to_go-1))
    return None


# runtests ( turysta )