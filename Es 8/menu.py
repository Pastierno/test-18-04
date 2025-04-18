from Es8 import Auto, Moto, Camion

def menu():
    veicoli = [] # Lista per memorizzare i veicoli
    while True:
        print("Menu:")
        print("1. Aggiungi veicolo")
        print("2. Visualizza veicoli")
        print("3. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1': # Aggiungi veicolo
            scelta_veicolo = input("Scegli il tipo di veicolo (auto/moto/camion): ").lower()
            
            if scelta_veicolo == 'auto':
                marca = input("Marca: ")
                anno_immatricolazione = int(input("Anno di immatricolazione: "))
                targa = input("Targa: ")
                revisione = input("Revisione (True/False): ").lower() == 'true'
                numero_portiere = int(input("Numero di portiere: "))
                veicolo = Auto(marca, anno_immatricolazione, targa, revisione, numero_portiere)
                veicoli.append(veicolo)
                
            elif scelta_veicolo == 'moto':
                marca = input("Marca: ")
                anno_immatricolazione = int(input("Anno di immatricolazione: "))
                targa = input("Targa: ")
                revisione = input("Revisione (True/False): ").lower() == 'true'
                cilindrata = int(input("Cilindrata: "))
                veicolo = Moto(marca, anno_immatricolazione, targa, revisione, cilindrata)
                veicoli.append(veicolo)
                
            elif scelta_veicolo == 'camion':
                marca = input("Marca: ")
                anno_immatricolazione = int(input("Anno di immatricolazione: "))
                targa = input("Targa: ")
                revisione = input("Revisione (True/False): ").lower() == 'true'
                portata_massima = int(input("Portata massima: "))
                veicolo = Camion(marca, anno_immatricolazione, targa, revisione, portata_massima)
                veicoli.append(veicolo)
                
        elif scelta == '2': # Visualizza veicoli
            if not veicoli:
                print("Nessun veicolo registrato.")
                continue
            print("Veicoli registrati:")
            for veicolo in veicoli:
                print(veicolo.descrivi())
        elif scelta == '3':
            print("Ciao!")
            break
        else:
            print("Opzione non valida")
            
menu()