# Tomasz Żmuda

# Moje rozwiązanie polega na tym aby na początku przeiterować przez każdy element tablicy 
# i w razie gdy jego rewers jest mniejszy (pod względem alfabetycznym), zamienimy element na jego rewers
# W ten sposób przy rozważaniu wyrazów równoważnych będziemy szykać wyrazów identycznych
# Następnie sortujemy tablicę alfabetycznie i szukamy najdłuższego ciągu identycznych wyrazów

# Szacowana złożoność O(N + log(n)) 


# from zad3testy import runtests

def merge(t, t1, t2):
    n1=len(t1)
    n2=len(t2)
    i=j=k=0
    while i<n1 and j<n2:
        if t1[i]<=t2[j]:
            t[k]=t1[i]
            i+=1
        else:
            t[k]=t2[j]
            j+=1
        k+=1
    while i<n1:
        t[k]=t1[i]
        i+=1
        k+=1
    while j<n2:
        t[k]=t2[j]
        j+=1
        k+=1
    return t


def merge_sort(t):
    n=len(t)
    if n>1:
        t1=t[0:n//2]
        t2=t[n//2:n]
        merge_sort(t1)
        merge_sort(t2)
        merge(t,t1,t2)

def strong_string(T):
    n=len(T)
    for i in range(n):
        n1=len(T[i])
        if T[i]>T[i][::-1]:
            T[i]=T[i][::-1]
    merge_sort(T)
    max_cnt=1
    cnt=1
    for i in range(1, n):
        if T[i-1]==T[i]:
            cnt+=1
            max_cnt=max(max_cnt, cnt)
        else:
            cnt=1
    return max_cnt


# # zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( strong_string, all_tests=True )
