# quick sort (ascending) with random pivot

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

def quick_sort(t, a, b):
    if b-a>1:
        pivot=partition(t, a,b)
        quick_sort(t, a, pivot-1)
        quick_sort(t, pivot+1, b)

# TESTS:
# t=[1,42,1,3,4,21,4,3,14,2]
# n=len(t)
# quick_sort(t, 0, n-1)
# print(t)
            
