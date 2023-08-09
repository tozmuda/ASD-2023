# Tomasz Żmuda

# Dla każdej kolumny przechodzę raz w górę i dół, przechowuję dwie wartości dla każdego pola (dp_up oraz dp_down) jedna z nich odnosi się do chodzenia od dołu a druga z góry
# Gdy biorę pod uwagę następną kolumnę dla każdego pola porównuję wartości z poprzedniej kolumny, z góry i z dołu i biorę max. 
# W ten sposób dla pola [i, j] max(dp_up[i][j], dp_down[i][j]) będzie wynikiem dla tego pola

#Szacowana złożoność O(n^2)

# from zad7testy import runtests
from math import inf

def maze( L ):
    n=len(L)
    dp_up=[[-1 for _ in range(n)] for _ in range(n)]
    dp_down=[[-1 for _ in range(n)] for _ in range(n)]
    dp_down[0][0]=0
    i=1
    while i<n and L[i][0]=='.':
        dp_down[i][0]=i
        i+=1
    for i in range(1, n):
        for j in range(n):
            if L[j][i]=='.':
                if dp_up[j][i-1]>=0 or dp_down[j][i-1]>=0:
                    dp_down[j][i]=max(dp_up[j][i-1] + 1, dp_down[j][i-1] + 1)
                if j>0 and dp_down[j-1][i]>=0:
                    dp_down[j][i]=max(dp_down[j][i], dp_down[j-1][i] + 1)
        for j in range(n-1, -1, -1):
            if L[j][i]=='.':
                if dp_up[j][i-1]>=0 or dp_down[j][i-1]>=0:
                    dp_up[j][i]=max(dp_up[j][i-1] + 1, dp_down[j][i-1] + 1)
                if j<n-1 and dp_up[j+1][i]>=0:
                    dp_up[j][i]=max(dp_up[j][i], dp_up[j+1][i] + 1)
    return max(dp_up[n-1][n-1], dp_down[n-1][n-1])



# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( maze, all_tests = True )
