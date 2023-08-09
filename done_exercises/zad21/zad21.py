# Tomasz Żmuda

# Tworzę dodatkowy graf w którym krawędzie mają zwiększone koszta (takie jak po napadzie, w stanie ścigania)
# Puszczam algorytm dijkstry z wierzchołka s (aby uzyskać najkrótszą ścieżkę z s do każdego wierzchołka) oraz z wierzhołka t (analogicznie)
# Następnie rozpatruję każdy zamek, czy opłaca się go obrabowć licząc sumę ścieżki z s do zamku i z zamku do t odejmując ilość złota w zamku
# Nie zapominam o przypadku gdzie najlepiej jest nie rabować żadnego zamku

# Szacowana złożoność O(E * log(V)) <=> O(V^2 * log(V))

# from egz1Atesty import runtests
from queue import PriorityQueue

def gold(G,V,s,t,r):
  n=len(G)
  inf=float('inf')
  # Tworzenie grafu w stanie po napadzie O(E)
  G_wanted=[[] for _ in range(n)]
  for i in range(n):
    for u, d in G[i]:
      G_wanted[i].append((u, (d*2)+r))

  # dijkstra O(E * log(V))
  def dijkstra(G, s):
    n=len(G)
    inf=float('inf')
    dist=[inf for _ in range(n)]
    dist[s]=0
    visited=[False for _ in range(n)]
    q=PriorityQueue()
    q.put((0, s))
    while not q.empty():
      d, v = q.get()
      if not visited[v]:
        visited[v]=True
        for u, w in G[v]:
          if dist[u]>dist[v]+w:
            dist[u]=dist[v]+w
            q.put((dist[u], u))
    return dist
  dist=dijkstra(G, s)
  dist_wanted=dijkstra(G_wanted, t)

  # Dla każdego zamku sprawdzenie czy opłaca się go rabować O(V)
  min_path=dist[t]
  for i in range(n):
    min_path=min(min_path, dist[i] + dist_wanted[i] - V[i])
  return min_path

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( gold, all_tests = True )
