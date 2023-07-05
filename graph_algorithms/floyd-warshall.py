import example_graphs
from copy import deepcopy
from math import inf

# Floyd-Warshall algorithm, returns a matrix where D[i][j] is min path starting from i to j in a graph (inf if doesn't exist), input: Graph (matrix rep)
def floyd_warshall(G):
    n=len(G)

    D=[[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        D[i][i]=0
        for j in range(n):
            if G[i][j]:
                D[i][j]=G[i][j]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j!=k:
                    D[j][k]=min(D[j][k], D[j][i] + D[i][k])
    return D

# TESTS
# G=example_graphs.random_directed_waged_graph_matrix(4, 0.8, 1, 9)
# example_graphs.print_graph_matrix(G)
# res=floyd_warshall(G)
# print(res)