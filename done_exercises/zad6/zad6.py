# Tomasz Żmuda

# W mojej propozycji rozwiązania tworzę graf skierowany w którym n wierzchołków to pracownicy, kolejne n to maszyny i ostatnie dwa to start i sink
# W grafie skonstruowanym w ten sposób maksymalny przepływ z start do sink będzie maksymalną liczbą pracowników mogących jednocześnie pracować
# W celu wykonania zadania korzystam z algorytmu Floyda - Fulkersona z pomocą algorytmu DFS korzystającym ze struktury stosu

# Szacowana złożoność obliczeniowa O(V * E^2), gdzie V to liczba pracowników a E to liczba krawędzi w skonstruowanym grafie

# from zad6testy import runtests
from collections import deque

def binworker( M ):
    n=len(M)
    G=[[] for _ in range((2*n)+2)]
    for i in range(n):
        for el in M[i]:
            G[i].append(el+n)
        G[2*n].append(i)
        G[i+n].append((2*n)+1)
    # print(G)

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

    cnt=0
    path=find_path(G, 2*n, (2*n)+1)
    while path:
        cnt+=1
        for i in range(len(path)-1):
            G[path[i]].append(path[i+1])
            G[path[i+1]].remove(path[i])
        path=find_path(G, 2*n, (2*n)+1)
    
    return cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( binworker, all_tests = False )
