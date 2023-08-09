# from egzP4atesty import runtests 

def bin_search(T, x):
    a=0
    b=len(T)-1
    while True:
        i=(b+a)//2
        if T[i]==x or a==b:
            break
        elif T[i]>x: b=max(i-1, a)
        else: a=min(i+1, b)
    if T[i]==x or T[a]==x: return i
    elif T[a]>x: return a
    else: return a+1

def mosty ( T: list ):
    T.sort(key=lambda x: (x[0], x[1]))
    LIS=[]
    for i in range(len(T)):
        if len(LIS)==0 or LIS[len(LIS)-1]<=T[i][1]:
            LIS.append(T[i][1])
        else:
            ind=bin_search(LIS, T[i][1])
            LIS[ind]=T[i][1]
    return len(LIS)

# runtests ( mosty, all_tests=True )