# from egzP7atesty import runtests 
from collections import deque

def akademik( T ):
    n=len(T)
    M=[[]for _ in range(2*n+2)]
    for i in range(n):
        for j in range(3):
            if T[i][j]!=None: M[i].append(T[i][j]+n)
    for i in range(n):
        M[2*n].append(i)
        M[i+n].append(2*n+1)

    def find_path(G, s, t):
        path=[]
        visited=[False for _ in range(len(G))]
        visited[s]=True
        parent=[None for _ in range(len(G))]
        def DFS_visit(G, v, t, visited, parent):
            stack=deque()
            stack.append(v)
            while stack:
                v=stack.pop()
                if v==t: return True
                for el in G[v]:
                    if not visited[el]:
                        parent[el]=v
                        visited[el]=True
                        stack.append(el)
        DFS_visit(G, s, t, visited, parent)
        if parent[t]==None: return False
        while t!=None:
            path.append(t)
            t=parent[t]
        return path
    
    cnt1=0
    path=find_path(M, 2*n, (2*n)+1)
    while path:
        cnt1+=1
        for i in range(len(path)-1):
            M[path[i]].append(path[i+1])
            M[path[i+1]].remove(path[i])
        path=find_path(M, 2*n, (2*n)+1)

    cnt2=0
    for i in range(n):
        if T[i][0]==None: cnt2+=1
    
    return n-cnt1-cnt2

# print(akademik([(2, 3, None), (0, 1, 3), (0, 2, None), (1, 3, 4), (2, 3, None)]))
# runtests ( akademik )