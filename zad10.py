# zad 5.10 Generator - wykorzystuje pakiet itertools i generuje kombinacje 
# 3 elementowe bez powtórzeń na zbiorze 10 elementowym.

import itertools as it
 
kombo = (x for x in it.combinations(range(9), 3))
# czy to wciąż generator, jeśli użyje pętli for?
# for i in kombo:
# 	print(i)
print(kombo)
print(next(kombo))
print(next(kombo))
print(next(kombo))
print(next(kombo))