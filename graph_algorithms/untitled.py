import example_graphs
from copy import deepcopy, copy

# Returns all strongly connected components as a list of lists of verticies, input: Graph (matrix rep, directed Graph)
def strongly_connected_components(Graph):
    # puts verticies in order of processing time in DFS
    n=len(Graph)
    time_of_processing=[]
    visited=[False for _ in range(n)]
    def DFS_visit1(G, v, visited):
        n=len(G)
        nonlocal time_of_processing
        visited[v]=True
        for i in range(n):
            if G[v][i] and not visited[i]:
                DFS_visit1(G, i, visited)
        time_of_processing.append(v)

    for i in range(n):
        if not visited[i]: DFS_visit1(Graph, i, visited)

    # inverts all edges
    G=deepcopy(Graph)
    for i in range(n):
        for j in range(i+1 , n):
            G[i][j], G[j][i] = G[j][i], G[i][j]
    
    # Now all verticies visited in one DFS_visit2 will be part of one strongly connected component if we start visiting in back order of time of proccesing
    def DFS_visit2(G, v, visited, comp):
        n=len(G)
        visited[v]=True
        comp.append(v)
        for i in range(n):
            if G[v][i] and not visited[i]:
                DFS_visit2(G, i, visited, comp)

    visited=[False for _ in range(n)]
    res=[]
    for i in range(n-1, -1, -1):
        if not visited[time_of_processing[i]]:
            comp=[]
            DFS_visit2(G, time_of_processing[i], visited, comp)
            res.append(copy(comp))
    return res


# TESTS
# G=example_graphs.random_directed_graph_matrix(8, 0.8)
# example_graphs.print_graph_matrix(G)
# res=strongly_connected_components(G)
# print(res)


