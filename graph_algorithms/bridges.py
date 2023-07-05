import example_graphs

# Algorithm that finds all bridges in a graph (matrix rep), returns list of tuples (edges)
def bridges(G):
    n=len(G)
    visited=[False for _ in range(n)]
    time=[None for _ in range(n)]
    low=[None for _ in range(n)]
    parent=[None for _ in range(n)]
    curr_time=0

    def low_min(G, v, visited, time, low, parent):
        n=len(G)
        res=time[v]
        for i in range(n):
            if G[v][i] and visited[i] and parent[v]!=i:
                res=min(res, low[i])
        return res
    
    def DFS_visit(G, v, visited, time, low, parent):
        nonlocal curr_time
        time[v]=curr_time
        curr_time+=1
        low[v]=time[v]
        n=len(G)
        visited[v]=True
        for i in range(n):
            if G[v][i] and not visited[i]:
                parent[i]=v
                DFS_visit(G, i, visited, time, low, parent)
        low[v]=low_min(G, v, visited, time, low, parent)
        
    
    for i in range(n):
        if not visited[i]: DFS_visit(G, i, visited, time, low, parent)
    bridges_tab=[]
    for i in range(n):
        if time[i]==low[i] and parent[i]!=None:
            bridges_tab.append((parent[i], i))
    return bridges_tab


# TESTS
# G=example_graphs.random_undirected_graph_matrix(4, 0.4)
# example_graphs.print_graph_matrix(G)
# res=bridges(G)
# print(res)