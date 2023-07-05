import example_graphs
from math import inf

# bellman-ford algorithm, returns list of distances to verticies or False if a negative cycle exists
def bellman_ford(G, v):
    n=len(G)
    dist=[inf for _ in range(n)]
    dist[v]=0

    for i in range(n):
        for j in range(n):
            if G[i][j]:
                dist[j]=min(dist[j], dist[i]+G[i][j])
                
    for i in range(n):
        for j in range(n):
            if G[i][j] and dist[j]>dist[i]+G[i][j]: return False
    return dist

# TESTS
# G=example_graphs.random_directed_waged_graph_matrix(8, 0.7, -3, 9)
# example_graphs.print_graph_matrix(G)
# res=bellman_ford(G, 0)
# print(res)