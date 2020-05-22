# zad 4.3 wykorzystuje komendę with, zapisuje kilka linijek tekstu do pliku a następnie wyswietla je na ekranie

with open("text.txt", "w+") as plik: 
    plik.write("Iteratory to zlo.\n")
    plik.write("Zlituje sie Pan.") 

with open("text.txt", "r") as plik:
    for otworz in plik:
        print(otworz)