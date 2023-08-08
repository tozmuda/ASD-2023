# Tomasz Żmuda

# W celu wykonania tego zadania zdecydowałem się posortować tablicę i wybierać największe wartości póki śnieg nie stopnieje,
# Jest to poprawne ponieważ w celu uzyskania tej samej ilości śniegu moglibyśmy po prostu wybierać te same pola śniegu z nie posortowanej tablicy, 
# w odpowiedniej kolejności aby nie topić innych wybranych (kolejność wybierania tych samych pól nie zmienia wyniku końcowego)
# Zastosowałem heap sort aby posortować tablicę rosnąco, więc interesujące mnie wartości były na końcu,
# Jednak przestawałem zrzucać elementy ze sterty na konieć tablicy w momencie gdy przestały mieć znaczenie (Zanim byśmy do nich doszli, już by stopniały)
# W ten sposób tablica była poprawnie posortowana tylko na samym końcu i właśnie z tamtąd braliśmy naszą sumę uwzględniając upływ dni
# from zad2testy import runtests


def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2

def heapify(t, i, n):
    max_i=i
    l=left(i)
    r=right(i)
    if l<n and t[l]>t[max_i]: max_i=l
    if r<n and t[r]>t[max_i]: max_i=r
    if max_i!=i:
        t[max_i], t[i]=t[i], t[max_i]
        heapify(t, max_i, n)

def build_heap(t):
    n=len(t)
    for i in range(parent(n-1), -1, -1):
        heapify(t, i, n)

def heap_sort(t):
    build_heap(t)
    n=len(t)
    i=0
    while n-1-i>0 and t[0]>i:
        t[0], t[n-1-i]=t[n-i-1], t[0]
        heapify(t, 0, n-i-1)
        i+=1


def snow( S ):
    n=len(S)
    heap_sort(S)
    day=sum=0
    i=0
    while n-i-1>0 and S[n-i-1]>day:
        sum+=S[n-i-1]-day
        day+=1
        i+=1
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( snow, all_tests = False )
