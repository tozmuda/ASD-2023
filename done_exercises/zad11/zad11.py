# from egzP1atesty import runtests 


def titanic( W, M, D ):
    str=""
    for i in range(len(W)):
        str+=M[ord(W[i])-65][1]
    n=len(str)
    dp=[float('inf') for _ in range(n+1)]
    dp[0]=0
    for i in range(n+1):
        if dp[i]<float('inf'):
            for el in D:
                if i+len(M[el][1])<=n and M[el][1]==str[i:i+len(M[el][1])]:
                    dp[i+len(M[el][1])]=min(dp[i+len(M[el][1])],dp[i]+1)
    return dp[n]

# runtests ( titanic, recursion=False )