# quick select

from random import randint

def partition(t, a, b):
    r=randint(a,b)
    t[r], t[b] = t[b], t[r]
    pivot=t[b]
    print(pivot)
    j=a
    i=a-1
    while j<b:
        if t[j]<=pivot:
            i+=1
            t[j], t[i] = t[i], t[j]
        j+=1
    t[i+1], t[b] = t[b], t[i+1]
    return i+1

def quick_select(t, a, b, k):
    pivot=partition(t, a, b)
    if pivot==k: return
    elif pivot>k: quick_select(t, a, pivot-1, k)
    else: quick_select(t, pivot+1, b, k)

# TESTS:
# t=[1,42,1,3,4,21,4,3,14,2]
# n=len(t)
# quick_select(t, 0, n-1, 5)
# print(t)
            
