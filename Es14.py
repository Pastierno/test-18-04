# Cos'è l'astrazione? Spiegala teoricamente e con esempi pratici, puoi includere codice

# l'astrazione è quel concetto che permette ad un elemento di dividere corpo e azione.
# Possiamo separare nel codice i dettagli di implementazione da quelli di utilizzo.
# Nel pratico lo vediamo con le classi astratte, che non possono essere istanziate e servono per definire un'interfaccia comune per le classi derivate.

from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def verso(self):
        pass
    
class Cane(Animale):
    def verso(self):
        print("Bau")
        
class Gatto(Animale):
    def verso(self):
        print("Miao")
    