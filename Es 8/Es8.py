# Implementa in Python un piccolo sistema di gestione di veicoli che dimostri incapsulamento, ereditarietà e polimorfismo.

# Definire una classe base Veicolo con attributi protetti(Marca[Str], Anno di immatricolazione[Int], Targa [Str] e Revisione[Bool]  ) e metodi getter/setter.
# Creare tre sottoclassi (Auto, Moto, Camion) che ereditano da Veicolo e sovrascrivono un metodo comune (descrivi())che riporti tutti i dati dell'oggetto reale, ogni classe figlia deve avere un attributo unico . 
# Nel menu, permettere all’utente di creare istanze diverse specifiche dei veicoli e previo controllo di tutti gli inserimenti chiamare descrivi() in un metodo polimorfico polimorfo. 

class Veicolo:
    def __init__(self, marca, anno_immatricolazione, targa, revisione):
        self._marca = marca  # Attributo protetto
        self._anno_immatricolazione = anno_immatricolazione  # Attributo protetto
        self._targa = targa  # Attributo protetto
        self._revisione = revisione  # Attributo protetto

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_anno_immatricolazione(self):
        return self._anno_immatricolazione

    def set_anno_immatricolazione(self, anno_immatricolazione):
        self._anno_immatricolazione = anno_immatricolazione

    def get_targa(self):
        return self._targa

    def set_targa(self, targa):
        self._targa = targa

    def get_revisione(self):
        return self._revisione

    def set_revisione(self, revisione):
        self._revisione = revisione
        
    def descrivi(self):
        return f"Marca: {self._marca}, Anno di immatricolazione: {self._anno_immatricolazione}, Targa: {self._targa}, Revisione: {self._revisione}"
    
class Auto(Veicolo):
    def __init__(self, marca, anno_immatricolazione, targa, revisione, numero_portiere):
        super().__init__(marca, anno_immatricolazione, targa, revisione)
        self._numero_portiere = numero_portiere  # Attributo unico per Auto

    def descrivi(self):
        return f"{super().descrivi()}, Numero portiere: {self._numero_portiere}"

# Auto1 = Auto("Fiat", 2020, "BB232CC", True, 4)
# print(Auto1.descrivi())
    
class Moto(Veicolo):
    def __init__(self, marca, anno_immatricolazione, targa, revisione, cilindrata):
        super().__init__(marca, anno_immatricolazione, targa, revisione)
        self._cilindrata = cilindrata  # Attributo unico per Moto

    def descrivi(self):
        return f"{super().descrivi()}, Cilindrata: {self._cilindrata}" 

# Moto1 = Moto("Yamaha", 2019, "XY456ZT", True, 600)
# print(Moto1.descrivi())

class Camion(Veicolo):
    def __init__(self, marca, anno_immatricolazione, targa, revisione, portata_massima):
        super().__init__(marca, anno_immatricolazione, targa, revisione)
        self._portata_massima = portata_massima  # Attributo unico per Camion

    def descrivi(self):
        return f"{super().descrivi()}, Portata massima: {self._portata_massima}"
    
# Camion1 = Camion("Mercedes", 2018, "ZZ789AA", True, 12000)
# print(Camion1.descrivi())