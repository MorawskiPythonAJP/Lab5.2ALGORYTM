# Klasa planszy
class Plansza:
    # Inicjalizacja obiektu planszy
    def __init__(self, krolowe):

        self.krolowe = krolowe
        self._index = 0

    # Pobranie długości krotki z królowymi
    def __len__(self):
        return len(self.krolowe)

    # Zwracanie ciągu znaków dla obiektu planszy
    def __str__(self):
        return "Położenie królowych (wiersz: kolumna): " + str(self.krolowe)

    # Inicjalizacja do iterowania
    def __iter__(self):
        self._index = 0
        return self

    # Jedno przejście przez pętle
    def __next__(self):
        if self._index < len(self.krolowe):
            pozycja = (self._index, self.krolowe[self._index])
            self._index += 1
            return pozycja
        else:
            raise StopIteration

    # Znajdowanie konfliktów na planszy
    def czy_poprawne(self):
        n = len(self.krolowe)
        for i in range(n):
            for j in range(i + 1, n):
                kolumna_i = self.krolowe[i]
                kolumna_j = self.krolowe[j]

                if kolumna_i == kolumna_j:
                    return False

                if abs(i - j) == abs(kolumna_i - kolumna_j):
                    return False
        return True

# Wyświetlenie położenia wszystkich królowych danego obiektu planszy
def iter(plansza):
    for i in plansza:
        print(i)
# Testy

p1 = Plansza((1,3,0))
print(p1)
print("Długość: " +  str(len(p1)))
print("test konfliktu planszy, brak konfliktów: " + str(p1.czy_poprawne()))
print("\n")

p2 = Plansza((1,1,0))
print(p2)
print("test konfliktu planszy, brak konfliktów: " + str(p2.czy_poprawne()))
print("\n")

p3 = Plansza((1,2,3))
print(p3)
print("test konfliktu planszy, brak konfliktów: " + str(p3.czy_poprawne()))
print("\n")

p4 = Plansza(())
print(p4)
print("Długość: " +  str(len(p4)))
print("test konfliktu planszy, brak konfliktów: " + str(p4.czy_poprawne()))
print("\n")

print("Test funkcji iter()")
iter(p1)