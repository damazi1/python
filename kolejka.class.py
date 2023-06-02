class Queue:
    def __init__(self):
        self.wartosc = []

    def isEmpty(self):
        if (len(self.wartosc) == 0):
            print("Kolejka jest pusta")
            return True
        else:
            return False

    def enqueue(self, item):
        self.wartosc.insert(0,item)

    def dequeue(self):
        return self.wartosc.pop()

    def size(self):
        return len(self.wartosc)

    def wyswietl_kolejka(self):
        print(self.wartosc)

    def wartoscFront(self):
        if (not self.isEmpty()):
            print("Wartość na poczatku kolejki ", self.wartosc[0])

    def wartoscBack(self):
        if (not self.isEmpty()):
            print("Wartość na końcu kolejki ", self.wartosc[len(self.wartosc) - 1])
