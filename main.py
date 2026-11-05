import random

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
    def is_proper(self, setup):
        n = len(setup)
        for i in range(n):
            for j in range(i + 1, n):
                kolumna_i = setup[i]
                kolumna_j = setup[j]

                if kolumna_i == kolumna_j:
                    return False

                if abs(i - j) == abs(kolumna_i - kolumna_j):
                    print("Konflikt kolumny: " + str(kolumna_i) + " - " + str(kolumna_j))
                    return False
        return True

    def attempt_generation(self):
        approved_cache = []
        tryout_cache = []
        for row in range(7):
            print("\n\n\n\n")
            available_cells = [0,1,2,3,4,5,6,7]
            for used in approved_cache:
                available_cells.remove(used)
            print("stan dostępnych miejsc przed pętlą: " + str(available_cells))
            print("zatwierdzona częściowa plansza: " + str(approved_cache   ))

            for chance in range(len(available_cells)):
                candidate_cell = available_cells[random.randint(0, len(available_cells)-1)]
                print(str(candidate_cell))
                tryout_cache.append(candidate_cell)
                result = self.is_proper(tryout_cache)
                available_cells.remove(candidate_cell)


                if result == True:
                    approved_cache = tryout_cache
                    tryout_cache = approved_cache.copy()
                    print("wiersz poprawnie wygenerowany")
                    break
                tryout_cache = approved_cache.copy()
                print("\n")
            else:
                print("Niepowodzenie w generowaniu planszy")
                return

        self.krolowe = tuple(approved_cache)
        print("Plansza poprawnie wygenerowana")

# Wyświetlenie położenia wszystkich królowych danego obiektu planszy
def iter(plansza):
    for i in plansza:
        print(i)

p1 = Plansza(())
p1.attempt_generation()