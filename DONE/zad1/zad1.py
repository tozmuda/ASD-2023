#Tomasz Żmuda

#W mojej implementacji funkcji iterujemy przez każdy ze znaków, podejrzewając że mogą być środkami palindromów.
#Dla każdego znaku znajdujemy największy palindorm jakiego może on być środkiem, zapisujemy do tablicy pomocniczej jego "promień" 
#Jest to ilość znaków o którą rozszerzyliśmy znak w obie strony aby uzyskać najdłuższy ciąg znaków będący palindromem
#"Promień" obliczamy dodatkową pętlą zagnieżdżoną iterując każdą stronę i sprawdzając identyczność znaków, w przypadku różnicy wychodzimy z pętli
#Na podstawie wpisanych już danych do tablicy jesteśmy w stanie z większą łatwością szacować "promienie" dla następnych znaków, co pozwoli nam ominąć pewną ilość operacji
#Robimy to na podstawie obecności palindomów w palindromach, a dokładniej ich symetryczności 
#Jednocześnie też w jednej ze zmiennych trzymamy największą długość palindromu (długość=2*"promień"+1) dotychczas spotkanego, i dla każdego znaku ją prównujemy

#Szacowany rząd złożoności: O(n)


# from zad1testy import runtests



def ceasar( s ):
    n=len(s)
    rad=0
    max_len=0
    pal=[0 for _ in range(n)]

    for i in range(1, n-1):
        if i<rad:
            pal[i]=min(pal[2*center-i], rad-i)
        while i-pal[i]-1>-1 and i+pal[i]+1<n and s[i-pal[i]-1]==s[i+pal[i]+1]:
            pal[i]+=1
        if i+pal[i]>rad:
            rad=i+pal[i]
            center=i
            max_len=max(max_len, 2*pal[i]+1)
            
    return max_len



# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( ceasar , all_tests = True )
