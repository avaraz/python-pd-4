#zad 5.6 test podanego iteratora
class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
 
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
        	raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
 
print([x for x in Wspak("matiW")])
print([x for x in Wspak("anaP")])
print([x for x in Wspak("aroseforP")])
