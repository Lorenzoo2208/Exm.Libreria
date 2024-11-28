from libro import (AggiuntaLibro, PrestitoLibro, Riportalibro, Disponibilitalibro , Libridisponibili , LibriinPrestito)

while True:

    print("1. Aggiungi libro")
    print("2. Presta il libro")
    print("3. Riporta il libro")
    print("4. Disponibilità libri")
    print("5. Libri disponibili")
    print("6. Libri in prestito")

    scelta = input("scegli un'opzione:")

    if scelta == ("1"):

        titolo = input("inserisci il titolo del libro:")
        AggiuntaLibro (titolo)

    elif scelta == ("2"):

         titolo = input("inserisci il titolo del libro da prestare:")
         PrestitoLibro (titolo)

    elif scelta == ("3"):

         titolo = input("inserisci il titolo del libro da riportare:")
         Riportalibro (titolo)

    elif scelta == ("4"):

         titolo = input("inserisci il titolo del libro:")
         Disponibilitalibro (titolo)

    elif scelta == ("5"):

         Libridisponibili ()

    elif scelta == ("6"):
    
         LibriinPrestito ()



