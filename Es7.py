# 7.Quali sono le tre regole fondamentali dell'OOP? Spiegale teoricamente e con esempi pratici,
# puoi includere codice


# Ereditarietà:
# L'ereditarietà è un principio fondamentale della programmazione orientata agli oggetti (OOP) 
# è quel legame gerarchico che permette ad una classe di ereditare le proprietà e i metodi
# di un'altra classe.

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, sono {self.nome} e ho {self.eta} anni.")

class Studente(Persona):
    def __init__(self, nome, eta, matricola):
        super().__init__(nome, eta)  # Chiama il costruttore della classe base
        self.matricola = matricola

    def saluta(self):
        super().saluta()  # Chiama il metodo saluta della classe base
        print(f"La mia matricola è {self.matricola}.")
        
# Incapsulamento:
# È la capacità di un elemento di nascondere i propri dettagli all'esterno o al codice stesso.
# i metodi che abbiamo sono attributi privati, protetti e getter/setter.

class ContoBanca:
    def __init__(self, saldo_iniziale):
        self.__saldo = saldo_iniziale  # Attributo privato

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo} effettuato.")
        else:
            print("Importo non valido.")

    def preleva(self, importo):
        if 0 < importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Prelievo di {importo} effettuato.")
        else:
            print("Importo non valido o saldo insufficiente.")

    def mostra_saldo(self):
        print(f"Saldo attuale: {self.__saldo}")
        
# Polimorfismo:
# È la capacità di un elemento di assumere forma diversa in base al contesto.
# Si manifesta ad esempio con l'overriding dei metodi

class Animale:
    def fai_suono(self):
        print("L'animale fa un suono.")

class Cane(Animale):
    def fai_suono(self):
        print("Il cane abbaia.")