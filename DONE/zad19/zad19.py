# Tomasz Żmuda

# Tworzę tablicę krawędzi i sortuję ją według wag, zapisuję w tablicy Ver
# Następnie patrzę na krawędzie od tej z najmniejszą wagą i próbuję stworzyć takie drzewo, które zawiera ją i (n-2) następnych z tablicy Ver
# Jeśli się udało, to stworzone drzewo jest tym wynikowym więc zwracam jego wagę,
# Jeśli nie, próbuję stworzyć drzewo z kolejną krawędzią z tablicy (o ile pozostała licznba krawędzi do dyspozycji jest większa, bądź równa (n-1))

# Szacowana złożoność obliczeniowa: O(VElog*E), gdzie V to liczba wierzchołków w grafie a E to liczba krawędzi

# from kol2testy import runtests

def beautree(G):
    n=len(G)

    Ver1=[]
    for i in range(n):
        for v, w in G[i]:
            Ver1.append((w, i, v))
    Ver1.sort(key=lambda x: x[0])
    Ver=[Ver1[i] for i in range(0, len(Ver1), 2)]

    def find_parent(v, parent):
        if parent[v]!=v:
            p=find_parent(parent[v], parent)
            parent[v]=p
            return p
        return v
    
    def union(v, u, parent, rank):
        v=find_parent(v, parent)
        u=find_parent(u, parent)
        if v==u: return False
        if rank[v]>rank[u]:
            parent[u]=v
            rank[v]+=rank[u]
        else:
            parent[v]=u
            rank[u]+=rank[v]
        return True
    
    for i in range(len(Ver)-n+2):
        wage=0
        rank=[1 for _ in range(n)]
        parent=[a for a in range(n)]
        flag=True
        for j in range(i, i+(n-1)):
            if not union(Ver[j][1], Ver[j][2], parent, rank):
                flag=False
                break
            wage+=Ver[j][0]
        if flag: return wage
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( beautree, all_tests = True )
