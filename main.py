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
    def is_proper(self):
        n = len(self.krolowe)
        for i in range(n):
            for j in range(i + 1, n):
                kolumna_i = self.krolowe[i]
                kolumna_j = self.krolowe[j]

                if kolumna_i == kolumna_j:
                    return False

                if abs(i - j) == abs(kolumna_i - kolumna_j):
                    #print("Konflikt kolumny: " + str(kolumna_i) + " - " + str(kolumna_j))
                    return False
        return True

    # Funkcja generator losująca i sprawdzająca wolne miejsca w danym rzędzie
    def candidate_generator(self, available_cells, safe_cache):
        while len(available_cells) > 0:
            #print("pozostało miejsc:" + str(len(available_cells)))
            candidate_cell = available_cells[random.randint(0, len(available_cells) - 1)]
            self.krolowe.append(candidate_cell)
            available_cells.remove(candidate_cell)
            result = self.is_proper()

            if result:
                safe_cache = self.krolowe.copy()
                #print("out suc" + str(safe_cache))
                yield True, safe_cache
            else:
                self.krolowe = safe_cache.copy()
                #print("in cont" + str(safe_cache))
                yield from self.candidate_generator(available_cells, safe_cache)
        else:
            #print("f")
            yield False, safe_cache

    # Pojedyńcza próba wygenerowania poprawnej planszy
    def attempt_generation(self):
        self.krolowe = []
        safe_cache = []
        for row in range(8):
            #print("row " + str(row))
            available_cells = [0,1,2,3,4,5,6,7]
            for used in safe_cache:
                available_cells.remove(used)
            #print("pre func " + str(safe_cache))
            potential_cell, safe_cache = next(self.candidate_generator(available_cells, safe_cache))
            #print("post func " + str(safe_cache))

            if not potential_cell:
                #print("Niepowodzenie w generowaniu planszy")
                self.krolowe = ()
                return
        else:
            #print("Powodzenie w generowaniu planszy")
            #self.iter_display()
            self.krolowe = tuple(self.krolowe)

    # Generuje nowe plansze puki nie otrzyma poprawnej
    def get_correct_board(self):
        self.attempt_generation()
        if len(self.krolowe) == 0:
            self.get_correct_board()

    # Wyświetlenie położenia wszystkich królowych danego obiektu planszy
    def iter_display(self):
        for i in self.krolowe:
            display_row = ""
            for j in range(i):
                display_row += "_"
            display_row += "Q"
            for j in range(7 - i):
                display_row += "_"
            print(display_row)
        print("\n")

# Wygenerowanie wszystkich możliwych poprawnych plansz
def get_all_correct_boards():
    c_boards = list()
    while len(c_boards) < 92:
        px = Plansza(())
        px.get_correct_board()
        for j in c_boards:
            if px.krolowe == j.krolowe:
                break
        else:
            c_boards.append(px)

            #Odkomentować, by wyświetlić graficznie wszystkie 92 plansze
            #px.iter_display()

    return c_boards

# Nadrzędny wątek

# Ekstrakcja wszystkich 92 możliwych kombinacji królowych na planszy zgodnych z zasadami
boards = get_all_correct_boards()

print("Trzy przykładowe poprawne plansze")
for x in range(3):
    print("Rozwiązanie: " + str(x+1))
    print(str(boards[x]))
    boards[x].iter_display()

print("Liczba znalezionych poprawnych planszy: " + str(len(boards)))