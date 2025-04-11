import pymongo

# Connessione al server MongoDB (assicurati che MongoDB sia in esecuzione)
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    print("connessione al server Mongodb riuscita")
except Exception as e:
    print(f"Errore connessione al server Mongodb non riuscita : {e}")

# Nome del database
db_name = "biblioteca"

# Creazione o accesso al database
db = client[db_name]

# Nome della collezione per i libri
collection_name = "libri"

# Creazione o accesso alla collezione
libri_collection = db[collection_name]

def inserisci_libro():
    """Permette all'utente di inserire i dati di un nuovo libro."""
    print("\nInserisci i dati del libro:")
    titolo = input("Titolo: ")
    autore = input("Autore: ")
    isbn = input("ISBN: ")
    anno_pubblicazione = input("Anno di Pubblicazione: ")
    genere = input("Genere: ")
    editore = input("Editore: ")
    prezzo = float(input("Prezzo: "))

    libro = {
        "titolo": titolo,
        "autore": autore,
        "isbn": isbn,
        "anno_pubblicazione": anno_pubblicazione,
        "genere": genere,
        "editore": editore,
        "prezzo": prezzo
    }

    try:
        result = libri_collection.insert_one(libro)
        print(f"Libro inserito con successo con ID: {result.inserted_id}")
    except Exception as e:
        print(f"Errore durante l'inserimento del libro: {e}")

if __name__ == "__main__":
    print(f"Connesso al database MongoDB: {db_name}")
    inserisci_libro()

    # Puoi aggiungere qui altre funzionalità, come la visualizzazione dei libri, la ricerca, ecc.

    # Chiudi la connessione al database quando hai finito (opzionale in script semplici)
    client.close()
    print("Connessione al database chiusa.")