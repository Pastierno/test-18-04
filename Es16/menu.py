# Fornire un menu per scegliere il tipo di forma, richiedere i parametri e stampare area/perimetro.
# Salva almeno 4 forme geometriche in lista di oggetti. 
# Creare un metodo poliformico che si occupi di paragonare la lista di forme geometriche e rispondere quale ha l'area maggiore e/o il perimetro.

import class_Forma as cf

def menu():
    lista_forme = []  # Lista per memorizzare le forme geometriche
    while True:
        print("1. Cerchio")
        print("2. Rettangolo")
        print("3. Triangolo")
        print("4. Mostra forme")
        print("5. Uscire")
        scelta = int(input("Scegli una forma (1-4): "))
        
        if scelta == 1:
            raggio = float(input("Inserisci il raggio del cerchio: "))
            forma = cf.Cerchio(raggio)
            lista_forme.append(forma)
            print(f"Area del cerchio: {forma.area()}")
            print(f"Perimetro del cerchio: {forma.perimetro()}")
        elif scelta == 2:
            base = float(input("Inserisci la base del rettangolo: "))
            altezza = float(input("Inserisci l'altezza del rettangolo: "))
            forma = cf.Rettangolo(base, altezza)
            lista_forme.append(forma)
            print(f"Area del rettangolo: {forma.area()}")
            print(f"Perimetro del rettangolo: {forma.perimetro()}")
        elif scelta == 3:
            base = float(input("Inserisci la base del triangolo: "))
            altezza = float(input("Inserisci l'altezza del triangolo: "))
            forma = cf.Triangolo(base, altezza)
            lista_forme.append(forma)
            print(f"Area del triangolo: {forma.area()}")
            print(f"Perimetro del triangolo: {forma.perimetro()}")
        elif scelta == 4:
            if not lista_forme:
                print("Nessuna forma salvata.")
            else:
                for i, forma in enumerate(lista_forme):
                    print(f"Forma {i+1}: Area = {forma.area()}, Perimetro = {forma.perimetro()}") # Mostra tutte le forme
        elif scelta == 5:
            print("Ciao!.")
            break
        else:
            print("Scelta non valida. Riprova.")
            
menu()