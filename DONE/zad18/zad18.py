# from egzP8btesty import runtests

def bellman_ford(G):
    n=len(G)
    for i in range(n):
        for v in range(n):
            for u in range(n):
                G[u][v]=min(G[u][v], G[u][i]+G[i][v])

def robot( G, P ):
    n=len(G)
    inf=float('inf')
    M=[[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for v, d in G[i]:
            M[i][v] = d
    bellman_ford(M)

    dist=0
    for i in range(len(P)-1):
        dist+=M[P[i]][P[i+1]]

    return dist
    
# runtests(robot, all_tests = True)
