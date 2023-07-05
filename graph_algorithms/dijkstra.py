import example_graphs
from math import inf

def dijkstra(G, v):
    n=len(G)
    visited=[False for _ in range(n)]
    dist=[inf for _ in range(n)]
    dist[v]=0
    min_ind=v
    min_val=0
    while min_val!=inf:
        visited[min_ind]=True
        for i in range(n):
            if G[min_ind][i] and not visited[i]:
                dist[i]=min(dist[i], dist[min_ind]+G[min_ind][i])
        min_val=inf
        for i in range(n):
            if not visited[i] and min_val>dist[i]:
                min_val=dist[i]
                min_ind=i
    return dist

# TESTS
# G=example_graphs.random_directed_waged_graph_matrix(8, 0.7, 1, 9)
# example_graphs.print_graph_matrix(G)
# res=dijkstra(G, 0)
# print(res)