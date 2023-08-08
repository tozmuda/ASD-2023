# from zad5testy import runtests
from queue import PriorityQueue

# Tomasz Żmuda
# Zamieniam reprezenatcję grafu na macierzową zawierającą wagi krawędzi, pomiędzy każdą parą wierzchołków z własnością zagięcia czasoprzestrzeni wstawiam krawędź o wadze 0
# Wykonuję algorytm Dijkstry do momentu kiedy znajdę czas przelotu do wierzchołka b, zwracam wynik
# Szacowany rząd złożoności O(V^2) gdzie V to liczba wierzchołków

def spacetravel( n, E, S, a, b ):
    visited=[False for _ in range(n)]
    time=[None for _ in range(n)]
    G=[[None for _ in range(n)] for _ in range(n)]
    for el in E:
        G[el[0]][el[1]]=el[2]
        G[el[1]][el[0]]=el[2]
    for el1 in S:
        for el2 in S:
            if el1!=el2:
                G[el1][el2]=0
                G[el2][el1]=0
    q=PriorityQueue()
    q.put((0, a))
    
    while not q.empty():
        v=q.get()
        if not visited[v[1]]:
            if v[1]==b: return v[0]
            visited[v[1]]=True
            time[v[1]]=v[0]
            for i in range(n):
                if G[v[1]][i]!=None and not visited[i]: q.put((v[0]+G[v[1]][i], i))
    return time[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( spacetravel, all_tests = False )