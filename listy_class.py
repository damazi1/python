class Lista:
    def __init__(self):
        self.wartosc = []
        # print(type(self.wartosc))

    def isEmpty(self):
        if (len(self.wartosc) == 0):
            print("Lista jest pusta")
            return True
        else:
            return False

    def wartoscFront(self):
        if (not self.isEmpty()):
            print("Wartość na poczatku listy ", self.wartosc[0])

    def wartoscBack(self):
        if (not self.isEmpty()):
            print("Wartość na końcu listy ", self.wartosc[len(self.wartosc) - 1])

    def wartosc_pozycja(self, pozycja):
        print("Lista [", pozycja, "]=", self.wartosc(pozycja))

    def push_back(self, liczba):
        self.wartosc += [liczba]

    def push_front(self, liczba):
        self.wartosc = [liczba] + self.wartosc

    def size(self):
        print(len(self.wartosc))

    def wyswietl_lista(self):
        # for i in self.wartosc:
        #    print(i)
        print(self.wartosc)