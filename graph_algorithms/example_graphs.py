import random

# Craetes a random undirected graph (returns matrix), density - number from 0 to 1
def random_undirected_graph_matrix(n, density):
    G = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.random()<density:
                G[i][j] = 1
                G[j][i] = 1
    return G

# Creates a random undirected graph without double edges going back and forth (returns matrix), density - number from 0 to 1
def random_directed_graph_matrix(n, density):
    G = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.random()<density: 
                if random.random()<0.5: G[i][j]=1
                else: G[j][i]=1
    return G

# Prints graph in matrix representation
def print_graph_matrix(G):
    n=len(G)
    print("Graph: ")
    print("-"*3*n)
    for i in range(n):
        for j in range(n):
            print(G[i][j], end=', ')
        print()
    print("-"*3*n)


# TESTS
# G=random_undirected_graph_matrix(6, 0.6)
# print_graph_matrix(G)
