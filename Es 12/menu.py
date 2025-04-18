import db
import class_Contatti as cc
import class_Utente as cu

def menu():
    db_conn = db.connessione("rubrica") # connessione al DB
    cursor = db_conn.cursor() # crea un cursore per eseguire le query
    db.crea_tabella() # crea il database e le tabelle se non esistono
    utente = None # inizializza l'oggetto utente a None
    while True:
        print("1. Login")
        print("2. Registrati")
        print("3. Aggiungi contatto (solo dopo il login)")
        print("4. Visualizza contatti (solo dopo il login)")
        print("5. Modifica contatto (solo dopo il login)")
        print("6. Elimina contatto (solo dopo il login)")
        print("7. Esci")
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            nome = input("Inserisci la tua email: ")
            password = input("Inserisci la tua password: ")
            db.autenticazione(nome, password) # verifica se l'utente esiste nel DB
            if db.autenticazione(nome, password) is not None: # se l'utente esiste
                print("Login avvenuto con successo.")
                utente = cu.Utente(nome, password, email)
               
        elif scelta == "2":
            nome = input("Inserisci il tuo nome: ")
            password = input("Inserisci la tua password: ")
            email = input("Inserisci la tua email: ")
            utente = cu.Utente(nome, password, email)
            db.registrazione(utente, db_conn) # registra l'utente nel DB
            db_conn.commit()
            print("Registrazione avvenuta con successo.")
        elif scelta == "3":
            if utente is None:
                print("Devi effettuare il login per aggiungere un contatto.")
                continue
            nome = input("Inserisci il nome del contatto: ")
            cognome = input("Inserisci il cognome del contatto: ")
            telefono = input("Inserisci il telefono del contatto: ")
            email = input("Inserisci l'email del contatto: ")
            contatto = cc.Contatto(nome, cognome, telefono, email)
            db.aggiungi_contatto(contatto, utente, db_conn)
            db_conn.commit()
            print("Contatto aggiunto con successo.")
        elif scelta == "4":
            if utente is None:
                print("Devi effettuare il login per visualizzare i contatti.")
                continue
            contatti = db.visualizza_contatti(utente, db_conn)
            # stampa i contatti
            if contatti:
                print("Contatti:")
                for contatto in contatti:
                    print(contatto)
            else:
                print("Nessun contatto trovato.")
        elif scelta == "5":
            if utente is None:
                print("Devi effettuare il login per modificare un contatto.")
                continue
            id = input("Inserisci l'ID del contatto da modificare: ")
            nome = input("Inserisci il nuovo nome del contatto: ")
            cognome = input("Inserisci il nuovo cognome del contatto: ")
            telefono = input("Inserisci il nuovo telefono del contatto: ")
            email = input("Inserisci la nuova email del contatto: ")
            db.modifica_contatto(id, nome, cognome, telefono, email, db_conn)
            db_conn.commit()
            print("Contatto modificato con successo.")
        elif scelta == "6":
            if utente is None:
                print("Devi effettuare il login per eliminare un contatto.")
                continue
            id = input("Inserisci l'ID del contatto da eliminare: ")
            db.elimina_contatto(id, utente, db_conn)
            db_conn.commit()
            print("Contatto eliminato con successo.")
        elif scelta == "7":
            db.chiudi_connessione(db_conn)
            utente = None
            print("Logout avvenuto con successo.")
            print("Ciao!")
            break
            
            
        else:
            print("Opzione non valida. Riprova.")


menu()