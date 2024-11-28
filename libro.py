libriinprestito = {}
libridisponibili = {}



def AggiuntaLibro(titolo):
    if titolo in libridisponibili :
        libridisponibili [titolo]["quantita"] +=1

    else:
        print(f"libro {'titolo'} aggiunto!")


def PrestitoLibro(titolo):
   
    if titolo in libridisponibili and libridisponibili[titolo]["quantita"] > 0:
        libridisponibili[titolo]["quantita"] -= 1
        if titolo not in libriinprestito:
            libriinprestito[titolo] = []
        libriinprestito[titolo].append(titolo)
        print(f"Libro '{titolo}' prestato a {utente}.")
    else:
        print(f"Il libro '{titolo}' non è disponibile.")



def Riportalibro(titolo, utente):
    
    if titolo in libriinprestito and utente in libriinprestito[titolo]:
        libriinprestito[titolo].remove(utente)
        if not libriinprestito[titolo]:
            del libriinprestito[titolo]
        libridisponibili[titolo]["quantita"] += 1
        print(f"Libro '{titolo}' riportato da {utente}.")
    else:
        print(f"Errore: Il libro '{titolo}' non risulta in prestito a {utente}.")



def Disponibilitalibro(titolo):
    
    if titolo in libridisponibili:
        quantita = libridisponibili[titolo]["quantita"]
        print(f"Il libro '{titolo}' è disponibile in {quantita} copie.")
    else:
        print(f"Il libro '{titolo}' non è presente nella libreria.")

def Libridisponibili():
    
    print("Libri disponibili:")

    for titolo, info in libridisponibili.items():
        print(f"- {titolo} (Autore: {info['autore']}, Quantità: {info['quantita']})")

def LibriinPrestito():
    
    print("Libri in prestito:")
    for titolo, utenti in libriinprestito.items():
        print(f"- {titolo}: prestato a {', '.join(utenti)}")








    

