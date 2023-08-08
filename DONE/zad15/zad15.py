# from egzP3btesty import runtests 
from queue import PriorityQueue

def find(v, parent):
    if parent[v]!=v:
        v=find(parent[v], parent)
    return parent[v]

def union(u, v, parent, rank):
    u=find(u, parent)
    v=find(v, parent)
    if u==v: return False
    if rank[u]>rank[v]:
        parent[v]=u
        rank[u]+=rank[v]
    else:
        parent[u]=v
        rank[v]+=rank[u]
    return True
        

def lufthansa ( G ):
    n=len(G)

    edges=[]
    for i in range(n):
        for v, w in G[i]:
            if i<v:
                edges.append((i, v, w))
    edges.sort(key=lambda x: x[2], reverse=True)

    parent=[i for i in range(n)]
    rank=[1 for _ in range(n)]
    spining_sum=0
    max_not_taken=0
    all_sum=0
    flag=1
    for i in range(len(edges)):
        u, v, w = edges[i]
        all_sum+=w
        if union(u, v, parent, rank):
            spining_sum+=w
        elif flag:
            flag=False
            max_not_taken=w
        
    return all_sum-max_not_taken-spining_sum

# runtests ( lufthansa, all_tests=True )