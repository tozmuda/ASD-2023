import example_graphs
from copy import deepcopy

# Checks for euler cycle in graph (matrix rep), returns the cycle as list or False if cycle doesn't exist
def euler_cycle(Graph):
    G=deepcopy(Graph)
    n=len(G)
    for i in range(n):
        sum=0
        for j in range(n):
            sum+=G[i][j]
        if sum%2!=0:
            return False
    v=0
    cycle=[]
    def euler_visit(G, v, cycle):
        n=len(G)
        for i in range(n):
            if G[v][i]:
                G[v][i]=0
                G[i][v]=0
                euler_visit(G, i, cycle)
        cycle.append(v)
    euler_visit(G, v, cycle)
    return cycle

# TESTS
# G=example_graphs.random_undirected_graph_matrix(6, 0.5)
# example_graphs.print_graph_matrix(G)
# cycle=euler_cycle(G)
# print(cycle)