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
schermo.geometry("700x700")
schermo.title("Database_Biblioteca")

frame1 = Frame(schermo, background="red", width= 400, height= 600, padx=10,pady=10)
frame1.grid(row=0,column=0,sticky="w")

frame2 = Frame(schermo, background="green", width= 400, height= 500, padx=10,pady=10)
frame2.grid(row=0,column=0,sticky="ne")

entry1=Entry(frame1,width=20, font =("Arial", 14))
entry2=Entry(frame1,width=20,font =("Arial", 14))
entry3=Entry(frame1,width=20,font =("Arial", 14))
entry4=Entry(frame1,width=20,font =("Arial", 14))
entry5=Entry(frame1,width=20,font =("Arial", 14))
entry6=Entry(frame1,width=20,font =("Arial", 14))
entry7=Entry(frame1,width=20,font =("Arial", 14))
entry8=Entry(frame1,width=20,font =("Arial", 14))

entry1.grid(row=1,column=0,sticky="w")
entry2.grid(row=3,column=0,sticky="w")
entry3.grid(row=5,column=0,sticky="w")
entry4.grid(row=7,column=0,sticky="w")
entry5.grid(row=9,column=0,sticky="w")
entry6.grid(row=11,column=0,sticky="w")
entry7.grid(row=13,column=0,sticky="w")
entry8.grid(row=15,column=0,sticky="w")

label1=Label(frame1,text="Titolo",width=20,font =("Arial", 14))
label2=Label(frame1,text="Autore",width=20,font =("Arial", 14))
label3=Label(frame1,text="Codice ISBN",width=20,font =("Arial", 14))
label4=Label(frame1,text="Anno di pubbicazione",width=20,font =("Arial", 14))
label5=Label(frame1,text="Genere",width=20,font =("Arial", 14))
label6=Label(frame1,text="Editore",width=20,font =("Arial", 14))
label7=Label(frame1,text="Prezzo",width=20,font =("Arial", 14))
label8=Label(frame1,text="Ubicazione",width=20,font =("Arial", 14))

label1.grid(row=0,column=0,sticky="w")
label2.grid(row=2,column=0,sticky="w")
label3.grid(row=4,column=0,sticky="w")
label4.grid(row=6,column=0,sticky="w")
label5.grid(row=8,column=0,sticky="w")
label6.grid(row=10,column=0,sticky="w")
label7.grid(row=12,column=0,sticky="w")
label8.grid(row=14,column=0,sticky="w")

def inserisci_libro():
    """Permette all'utente di inserire i dati di un nuovo libro."""
    print("\nInserisci i dati del libro:")
    titolo = entry1.get()
    autore = entry2.get()
    isbn = entry3.get()
    anno_pubblicazione = entry4.get()
    genere = entry5.get()
    editore = entry6.get()
    prezzo = float(entry7.get())
    ubicazione = entry8.get()

    libro = {
        "titolo": titolo,
        "autore": autore,
        "isbn": isbn,
        "anno_pubblicazione": anno_pubblicazione,
        "genere": genere,
        "editore": editore,
        "prezzo": prezzo,
        "ubicazione": ubicazione
    }

    try:
        result = libri_collection.insert_one(libro)
        print(f"Libro inserito con successo con ID: {result.inserted_id}")
        txt1.delete( 1.0, END)
        txt1.insert(1.0, f"Libro ' {titolo} ' inserito nel database\n")
        
    except Exception as e:
        print(f"Errore durante l'inserimento del libro: {e}")

def chiudi_connessione():
    client.close()
    print("Connessione al database chiusa.")
    txt1.delete( 1.0, END)
    txt1.insert(1.0, "Connessione al database chiusa.")

def cerca():
    txt1.delete( 1.0, END)
    print("\nInserisci i dati del libro:")
    titolo = entry1.get()
    print(libri_collection.find_one({"titolo" : titolo}))
    
    query = {"titolo" : titolo}
    risultato = libri_collection.find_one(query)
    i = 0.0
    #stringa =""
    #print(risultato)
    for chiave, valore in risultato.items():
        i += 1
        #print(chiave, ":", valore, "\n")
        txt1.insert(i, f"{chiave} : {valore}\n")
def cancella():
    txt1.delete( 1.0, END)
    print("\nInserisci i dati del libro:")
    titolo = entry1.get()
    print(libri_collection.delete_one({"titolo" : titolo}))
    txt1.insert(1.0, f"Libro ' {titolo} ' eliminato dal database\n")

def aggiorna():
    titolo = entry1.get()
    autore = entry2.get()
    isbn = entry3.get()
    anno_pubblicazione = entry4.get()
    genere = entry5.get()
    editore = entry6.get()
    prezzo = float(entry7.get())
    ubicazione = entry8.get()
    
    libro_dict = {
                 "titolo":titolo,
                 "autore":autore,
                 "isbn":isbn,
                 "anno_pubblicazione":anno_pubblicazione,
                 "genere":genere,
                 "editore":editore,
                 "prezzo":prezzo,
                 "ubicazione":ubicazione}
    query = { "titolo": titolo }
    for chiave,valore in libro_dict.items():
        nuovo_valore = { "$set": { chiave: valore } }
        libri_collection.update_one(query, nuovo_valore)
    txt1.delete( 1.0, END)
    cerca()
    #newvalues = { "$set": { "prezzo": 50.0 } }
    #libri_collection.update_one(query, newvalues)
    
    """
    myquery = { "address": "Valley 345" }
    newvalues = { "$set": { "address": "Canyon 123" } }
    mycol.update_one(myquery, newvalues)
    """
    pass

def pulisci():
    txt1.delete( 1.0, END)
    entry1.delete(first=0, last="end")
    entry2.delete(first=0, last="end")
    entry3.delete(first=0, last="end")
    entry4.delete(first=0, last="end")
    entry5.delete(first=0, last="end")
    entry6.delete(first=0, last="end")
    entry7.delete(first=0, last="end")
    entry8.delete(first=0, last="end")
    entry1.focus()


btn1=Button(frame2,text="Inserisci",width=10,height=3,command=inserisci_libro,font =("Arial", 12))
btn2=Button(frame2,text="Cerca",width=10,height=3,command=cerca,font =("Arial", 12))
btn3=Button(frame2,text="Cancella",width=10,height=3,command=cancella,font =("Arial", 12))
btn4=Button(frame2,text="Aggiorna",width=10,height=3,command=aggiorna,font =("Arial", 12))
btn5=Button(frame2,text="Chiudi_conn.",width=10,height=3,command=chiudi_connessione,font =("Arial", 12))
btn6=Button(frame2,text="Pulisci",width=10,height=3,command=pulisci,font =("Arial", 12))

btn1.grid(row=0,column=0, sticky="w")
btn2.grid(row=1,column=0, sticky="w")
btn3.grid(row=2,column=0, sticky="w")
btn4.grid(row=3,column=0, sticky="w")
btn5.grid(row=4,column=0, sticky="w")
btn6.grid(row=5,column=0, sticky="w")

txt1 = Text(schermo,width=40, height= 10, font=("Cambria",15), padx=10,pady=10)
txt1.grid(row=12,column=0, sticky = "nw")

