# Stable merge sort that sorts a list consisting of list / tuples by an index (ascending)

def merge(t, t1, t2, index):
    l1=len(t1)
    l2=len(t2)
    i=j=k=0
    while i<l1 and j<l2:
        if t1[i][index]<=t2[j][index]:
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

def merge_sort(t, index):
    l=len(t)
    if l>1:
        div=l//2
        t1, t2 = t[0:div], t[div: l]
        merge_sort(t1, index)
        merge_sort(t2, index)
        merge(t, t1, t2, index)


# TESTS:
# t=[(1, 2), (3, 50), (4, 20), (2, 12), (-1, 0), (20, 1)]
# merge_sort(t, 1)
# print(t)
