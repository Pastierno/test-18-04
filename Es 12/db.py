import mysql.connector as sq

#  Realizza un’app console Python con menu che si connetta a un database MySQL per gestire una rubrica contatti.

# Stabilire la connessione al DB e creare, se non esiste, la tabella contatti (nome, telefono, email). 
#Implementare le operazioni CRUD: inserimento, lettura, aggiornamento, cancellazione.
# Creare una classe Utente e una tabella Utenti con ID auto aumentato, nome e passw
#Creare una gestione di login rispetto agli utenti che verifichi se l'utente e presente nella tabella utenti
#Presentare un menu per selezionare ciascuna operazione e permettere dopo il login di registrare contatti collegando il contattato creato all'ID della classe utente che l'ha creato.

def crea_tabella():
    # Stabilire la connessione al DB e creare, se non esiste, la tabella contatti (nome, telefono, email).
    db = sq.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = db.cursor()
    # crea DATABASE
    cursor.execute("""
            CREATE DATABASE IF NOT EXISTS rubrica
        """)
    cursor.execute("""
            USE rubrica
        """)

    # crea tabella utenti
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS utenti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            )
        """)
    # crea tabella contatti
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS contatti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                cognome VARCHAR(255) NOT NULL,
                telefono INT NOT NULL,
                email VARCHAR(255) NOT NULL,
                utente_id INT NOT NULL,
                FOREIGN KEY (utente_id) REFERENCES utenti(id) ON DELETE CASCADE
                )""")
    db.commit()
    cursor.close()
    db.close()
    
def connessione(datab):
    return sq.connect(
        host="localhost",
        user="root",
        password="",
        database= datab
    ) 

def chiudi_connessione(db):
    db.close() # chiude la connessione al DB

def autenticazione(nome, password):
    db = connessione()
    cursor = db.cursor()
    # verifica se l'utente è presente nella tabella utenti
    cursor.execute("SELECT * FROM utenti WHERE nome = %s AND password = %s", (nome, password))
    utente = cursor.fetchone()
    cursor.close()
    chiudi_connessione(db)
    return utente

def registrazione(nome, password, email):
    db = connessione()
    cursor = db.cursor()
    # inserisce un utente nella tabella utenti
    cursor.execute("INSERT INTO utenti (nome, password, email) VALUES (%s, %s, %s)", (nome, password, email))
    db.commit()
    cursor.close()
    chiudi_connessione(db)
    

def inserisci_contatto(Contatto, utente_id):
    db = connessione()
    cursor = db.cursor()
    # inserisce un contatto nella tabella contatti
    cursor.execute("INSERT INTO contatti (nome, cognome, telefono, email, utente_id) VALUES (%s, %s, %s, %s, %s)", (Contatto.nome, Contatto.cognome, Contatto.telefono, Contatto.email, utente_id))
    
    db.commit()
    cursor.close()
    chiudi_connessione(db)

def leggi_contatti(utente_id):
    db = connessione()
    cursor = db.cursor()
    # legge i contatti della tabella contatti
    cursor.execute("SELECT * FROM contatti WHERE utente_id = %s", (utente_id,))
    contatti = cursor.fetchall()
    cursor.close()
    chiudi_connessione(db)
    return contatti

def aggiorna_contatto(id, nome, cognome, telefono, email):
    db = connessione()
    cursor = db.cursor()
    # aggiorna un contatto nella tabella contatti
    cursor.execute("UPDATE contatti SET nome = %s, cognome = %s, telefono = %s, email = %s WHERE id = %s", (nome, cognome, telefono, email, id))
    db.commit()
    cursor.close()
    chiudi_connessione(db)
    
def cancella_contatto(id, utente_id):
    db = connessione()
    cursor = db.cursor()
    # cancella un contatto dalla tabella contatti
    cursor.execute("DELETE FROM contatti WHERE id = %s AND utente_id = %s", (id, utente_id))
    db.commit()
    cursor.close()
    chiudi_connessione(db)
    