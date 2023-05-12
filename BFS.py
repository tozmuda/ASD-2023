import example_graphs
from queue import Queue

# Simple BFS, input: G - graph (matrix rep), s - starting verticy, output: array of distances from starting verticy (False if unachievable)
def BFS(G, s):
    n=len(G)
    queue=Queue()
    queue.put(s)
    dist=[False for _ in range(n)]
    dist[s]=0
    visited=[False for _ in range(n)]
    visited[s]=True
    parent=[False for _ in range(n)]
    while(not queue.empty()):
        v=queue.get()
        for i in range(n):
            if G[v][i] and not visited[i]:
                visited[i]=True
                parent[i]=v
                dist[i]=dist[v]+1
                queue.put(i)
    return dist



# TESTS
# G = example_graphs.random_undirected_graph_matrix(6, 0.6)
# res=BFS(G, 0)
# example_graphs.print_graph_matrix(G)
# print(res)