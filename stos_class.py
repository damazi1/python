class Stos:
    def __init__(self):
        self.wartosc = []
        # print(type(self.wartosc))

    def isEmpty(self):
        if (len(self.wartosc) == 0):
            print("Stos jest pusty")
            return True
        else:
            return False

    def peek(self):
        if (not self.isEmpty()):
            print("Wartość na wierzchu stosu ",
                  self.wartosc[len(self.wartosc) - 1])
            return self.wartosc[len(self.wartosc) - 1]

    def push(self, liczba):
        if (type(liczba) == list):
            for i in liczba:
                self.push(i)
        else:
            self.wartosc += [liczba]

    def size(self):
        print("Rozmiar stosu", len(self.wartosc))
        self.isEmpty()
        return len(self.wartosc)

    def wyswietl_stos(self):
        # for i in self.wartosc:
        #    print(i)
        print(self.wartosc)