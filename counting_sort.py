# Counting sort (ascending) on list with all numbers less than k

def counting_sort(t, k):
    n=len(t)
    t_p=[0 for _ in range(k)]
    t_new=[0 for _ in range(n)]
    for i in range(n): t_p[t[i]]+=1
    for i in range(1, k): t_p[i]+=t_p[i-1]
    for i in range(n): 
        t_new[t_p[t[i]]-1]=t[i]
        t_p[t[i]]-=1
    return t_new

# TESTS:
# t=[0,5,1,3,4,2,4,3,5,2]
# n=len(t)
# t=counting_sort(t, 6)
# print(t)

