# Tomasz Żmuda

# W moim roziwązaniu na początku przechodzę przez graf algorytmem BFS przypisując każdemu wierzchołkowi wartość odległości od wierczhołka s oraz jego rodzica
# Następnie przechodzę przez główną najkrótszą drogę w grafie od wierzchołka t do s przy pomocy tablicy parent
# W każdym wierczhołku sprawdzam czy mogę usunąć krawędź pomiędzy nim a jego rodzice, żeby wydłużyć drogę z s do t (sprawdzając odległości jego sąsiadów od s) 
# Uwzględniam przy tym istnienie innych najkrótszych dróg prowadzących do t pomijając tą krawędź

# Szacowany rząd złożoności O(E+V), gdzie E to ilość krawędzi w G a V to ilość wierzchołków w G

# from zad4testy import runtests
from collections import deque

def BFS(G, s, visited, parent, dist):
    queue=deque()
    n=len(G)
    dist[s]=0
    visited[s]=True
    queue.append(s)
    while len(queue)>0:
        el=queue.popleft()
        for w in G[el]: 
            if not visited[w]:
                visited[w]=True
                queue.append(w)
                parent[w]=el
                dist[w]=dist[parent[w]]+1

def measure_loop(G, w1, w2, parent, dist):
    min_w=10^12
    while w1!=w2:
        for el in G[w2]:
            if dist[el]<dist[w2] and parent[w2]!=el:
                min_w=min(measure_loop(G, parent[w1], el, parent, dist), min_w)
        w1=parent[w1]
        w2=parent[w2]
    return dist[w1]
                

def longer( G, s, t ):
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    dist=[None for _ in range(n)]
    BFS(G, s, visited, parent, dist)
    w=t
    in_loop_until=dist[w]
    visited=[False for _ in range(n)]
    while parent[w]!=None:
        for el in G[w]:
            if dist[el]<dist[w] and parent[w]!=el:
                in_loop_until=min(measure_loop(G, parent[w], el, parent, dist), in_loop_until)
        for el in G[w]:
            if dist[el]>=dist[w] and not visited[w] and in_loop_until>=dist[w]:
                return (parent[w], w)
        visited[w]=True
        w=parent[w]

    

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( longer, all_tests = True )