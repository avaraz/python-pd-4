#zad 4.1 generuje liczby podzielne przez 4 i zapisuje je do pliku

plik = open("liczby.txt","w+")

for x in range(21):
    if x % 4 == 0:
        lista = [x]
        plik.writelines(str(x))
        print(lista)