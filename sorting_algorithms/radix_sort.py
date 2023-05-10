# Radix sort (ascending) on list with all numbers of length k

# returns k'th digit of x
def kth_digit(x, k):
    return (x%(10**k))//(10**(k-1))

def counting_sort_by_digit(t, k):
    n=len(t)
    t_p=[0 for _ in range(10)]
    t_new=[0 for _ in range(n)]
    for i in range(n): t_p[kth_digit(t[i], k)]+=1
    for i in range(1, 10): t_p[i]+=t_p[i-1]
    for i in range(n): 
        t_new[t_p[kth_digit(t[i], k)]-1]=t[i]
        t_p[kth_digit(t[i], k)]-=1
    return t_new

def radix_sort(t, k):
    for i in range(1, k+1):
        t=counting_sort_by_digit(t, k)
    return t

# TESTS:
# t=[4350,5124,1231,5343,7534,2432,4121,4333,7555,1232]
# n=len(t)
# t=radix_sort(t, 4)
# print(t)
