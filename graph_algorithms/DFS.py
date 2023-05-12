import example_graphs

# Normal DFS algorithm, input: G - garph (matrix rep), s - starting verticy, output: array of integers - time required to get from s to all verticies with DFS 
def DFS(G,  s):
    curr_time=0
    def DFS_visit(G, v, time, parent, visited):
        nonlocal curr_time
        time[v]=curr_time
        curr_time+=1
        visited[v]=True
        for i in range(n):
            if G[v][i] and not visited[i]:
                parent[i]=v
                DFS_visit(G, i, time, parent, visited)

    n=len(G)
    visited=[False for _ in range(n)]
    parent=[False for _ in range(n)]
    time=[False for _ in range(n)]
    DFS_visit(G, s, time , parent,  visited)
    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i, time, parent, visited)
    return time

# TESTS
# G=example_graphs.random_directed_graph_matrix(5, 0.8)
# example_graphs.print_graph_matrix(G)
# tab=DFS(G, 0)
# print(tab)

