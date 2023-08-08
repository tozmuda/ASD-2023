# from egzP5atesty import runtests 
from collections import deque

def inwestor ( T ):
    n=len(T)
    stack=deque()
    stack.append(-1)
    stack.append(0)
    left=[-1 for _ in range(n)]
    right=[n for _ in range(n)]

    i=0
    while i<n:
        if len(stack)==1 or T[stack[len(stack)-1]]<=T[i]:
            left[i]=stack[len(stack)-1]
            stack.append(i)
            i+=1

        elif T[stack[len(stack)-1]]>T[i]:
            ind=stack.pop()
            right[ind]=i

        else:
            ind=stack.pop()
            left[i]=left[ind]
            stack.append(i)
            i+=1
    
    max_sum=-float('inf')
    for i in range(n):
        max_sum=max(max_sum, T[i]*(right[i]-left[i]-1))

    # print(left)
    # print(right)


    return max_sum

# runtests ( inwestor, all_tests=True )