# Stable merge sort (ascending)

def merge(t, t1, t2):
    l1=len(t1)
    l2=len(t2)
    i=j=k=0
    while i<l1 and j<l2:
        if t1[i]<=t2[j]:
            t[k]=t1[i]
            i+=1
        else:
            t[k]=t2[j]
            j+=1
        k+=1
    while i<l1 and k<l1+l2:
        t[k]=t1[i]
        i+=1
        k+=1
    while j<l2 and k<l1+l2:
        t[k]=t2[j]
        j+=1
        k+=1

def merge_sort(t):
    l=len(t)
    if l>1:
        div=l//2
        t1, t2 = t[0:div], t[div: l]
        merge_sort(t1)
        merge_sort(t2)
        merge(t, t1, t2)


# TESTS:
# t=[1,42,1,3,4,21,4,3,14,2]
# merge_sort(t)
# print(t)
