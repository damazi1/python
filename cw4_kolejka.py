class Kolejka:
    def __init__(self):
        self.wartosc = []
        #print(type(self.wartosc))
    
    def isEmpty(self):
        if(len(self.wartosc) == 0):
            print("Kolejka jest pusta")
            return True
        else:
            return False

    def head(self):
        if(not self.isEmpty()):
            print ("Wartość na początku kolejki ", self.wartosc[0])
            return self.wartosc[0]

    def enqueue(self, liczba):
        if(type(liczba) == list):
            for i in liczba:
                self.enqueue(i)
        else:
            self.wartosc += [liczba]

    def dequeue(self):
        if(not self.isEmpty()):
            del self.wartosc[0]
           
    def size(self):
        print("Rozmiar kolejki", len(self.wartosc))
        self.isEmpty()
        return len(self.wartosc)
  
kolejka = Kolejka()
kolejka.enqueue([2,6,10])
print(kolejka.wartosc)
kolejka.head()
kolejka.dequeue()
print(kolejka.wartosc)
kolejka.head()

