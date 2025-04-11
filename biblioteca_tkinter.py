import pymongo
from tkinter import *

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



schermo =Tk()
schermo.geometry("700x600")
schermo.title("Database_Biblioteca")



entry1=Entry(schermo,width=20, font =("Arial", 14))
entry2=Entry(schermo,width=20,font =("Arial", 14))
entry3=Entry(schermo,width=20,font =("Arial", 14))
entry4=Entry(schermo,width=20,font =("Arial", 14))

entry1.grid(row=2,column=0,sticky="w")
entry2.grid(row=4,column=0,sticky="w")
entry3.grid(row=6,column=0,sticky="w")
entry4.grid(row=8,column=0,sticky="w")

label1=Label(schermo,text="Titolo",width=20,font =("Arial", 14))
label2=Label(schermo,text="Autore",width=20,font =("Arial", 14))
label3=Label(schermo,text="Codice ISBN",width=20,font =("Arial", 14))
label4=Label(schermo,text="Anno di pubbicazione",width=20,font =("Arial", 14))

label1.grid(row=1,column=0,sticky="w")
label2.grid(row=3,column=0,sticky="w")
label3.grid(row=5,column=0,sticky="w")
label4.grid(row=7,column=0,sticky="w")



def inserisci_libro():
    """Permette all'utente di inserire i dati di un nuovo libro."""
    print("\nInserisci i dati del libro:")
    titolo = entry1.get()
    autore = entry2.get()
    isbn = entry3.get()
    anno_pubblicazione = entry4.get()
    #genere = input("Genere: ")
    #editore = input("Editore: ")
    #prezzo = float(input("Prezzo: "))

    libro = {
        "titolo": titolo,
        "autore": autore,
        "isbn": isbn,
        "anno_pubblicazione": anno_pubblicazione
        #"genere": genere,
        #"editore": editore,
        #"prezzo": prezzo
    }

    try:
        result = libri_collection.insert_one(libro)
        print(f"Libro inserito con successo con ID: {result.inserted_id}")
    except Exception as e:
        print(f"Errore durante l'inserimento del libro: {e}")

def chiudi_connessione():
    client.close()
    print("Connessione al database chiusa.")



btn1=Button(schermo,text="Inserisci",width=10,height=3,command=inserisci_libro,font =("Arial", 12))
btn2=Button(schermo,text="Chiudi_connessione",height=3,command=chiudi_connessione,font =("Arial", 12))
#btn3=Button(schermo,text="cerca",width=10,height=3,command=cerca)

btn1.grid(row=9,column=0, sticky="w")
btn2.grid(row=10,column=0, sticky="w")
#btn3.grid(row=7,column=0, sticky="w")



