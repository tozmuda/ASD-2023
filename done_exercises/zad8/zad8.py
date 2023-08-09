# from zad8testy import runtests
from queue import Queue, PriorityQueue

def BFS(M, i, j):
    n=len(M)
    m=len(M[0])
    if M[i][j]==0: return 0
    q=Queue()
    q.put((i,j, M[i][j]))
    sum=0
    while not q.empty():
        i, j, w=q.get()
        sum+=w
        M[i][j]=0
        for k in range(-1, 2, 2):
            if i+k>=0 and i+k<n and M[i+k][j]>0: q.put((i+k, j, M[i+k][j]))
        for k in range(-1, 2, 2):
            if j+k>=0 and j+k<m and M[i][j+k]>0: q.put((i, j+k, M[i][j+k]))
    return sum

def plan(T):
    n=len(T[0])
    tab=[0 for _ in range(n)]
    for i in range(n):
        tab[i]=BFS(T, 0, i)
    fuel=0
    cnt=0
    sources=PriorityQueue()
    for i in range(n-1):
        sources.put((-1)*tab[i])
        if fuel==0:
            fuel+=(-1)*sources.get()
            cnt+=1
        fuel-=1
    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( plan, all_tests = True )

