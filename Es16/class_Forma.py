# Costruisci un sistema per gestire forme geometriche usando classi astratte

# Definire una classe astratta Forma con metodi astratti area() e perimetro(). 
# Creare classi concrete (Cerchio, Rettangolo, Triangolo) che implementino i metodi.
# Fornire un menu per scegliere il tipo di forma, richiedere i parametri e stampare area/perimetro.
# Salva almeno 4 forme geometriche in lista di oggetti. 
# Creare un metodo poliformico che si occupi di paragonare la lista di forme geometriche e rispondere quale ha l'area maggiore e/o il perimetro.
from abc import ABC, abstractmethod

class Forma:
    @abstractmethod # Definizione della classe astratta Forma
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Cerchio(Forma): # Definizione della classe Cerchio
    # Inizializzazione del raggio del cerchio
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return 3.14 * self.raggio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.raggio
    
class Rettangolo(Forma): # Definizione della classe Rettangolo
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)
    
class Triangolo(Forma): # Definizione della classe Triangolo
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return (self.base * self.altezza) / 2

    def perimetro(self):
        return self.base + 2 * ((self.base ** 2 + self.altezza ** 2) ** 0.5)