# zad 5.11 Generator - zwraca kolejne wartości ciągu Fibonacciego.

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
 
ciag = fib(5)
# for i in ciag:
# 	print(i)
print(ciag)
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
