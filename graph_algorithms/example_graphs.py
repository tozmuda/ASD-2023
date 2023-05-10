import random

# Craetes a random undirected graph (returns matrix)
def random_undirected_graph_matrix(n):
    G = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.randint(0, 2)==1:
                G[i][j] = 1
                G[j][i] = 1
    return G

# Creates a random undirected graph without double edges going back and forth (returns matrix)
def random_directed_graph_matrix(n):
    G = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.randint(0, 2)==1: 
                if random.randint(0, 2)==1: G[i][j]=1
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
# G=random_directed_graph_matrix(6)
# print_graph_matrix(G)
