def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    # TODO
    dizionario = {}
    with open(file_path, "r", encoding='utf-8') as file:
        file.readline()
        for riga in file:
            if riga!='':
                lista_foto=riga.strip().split(',')

                codice=lista_foto[0]
                titolo = lista_foto[1]
                autore = lista_foto[2]
                mese = lista_foto[3]
                anno = lista_foto[4]

                if anno not in dizionario:
                    dizionario[anno] = lista_foto
                    pass
                else:
                    dizionario[anno].append(lista_foto)

    return dizionario

def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    # TODO
    lista_foto=[]
    codice=input(str('inserire il codice della foto: '))
    titolo = input(str('inserire il titolo della foto: '))
    autore = input(str('inserire il autore della foto: '))
    mese = input(int('inserire il mese della foto: '))
    anno = input(int('inserire il anno della foto: '))
    lista_foto.append(codice)
    lista_foto.append(titolo)
    lista_foto.append(autore)
    lista_foto.append(mese)
    lista_foto.append(anno)


    if anno in album:
        album[anno]=lista_foto

    return album

def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    # TODO
    for anno in album:
        # Scorriamo ogni foto dentro la lista di quell'anno
        for foto in album[anno]:
            # Se il codice della foto (indice 0) corrisponde, la restituiamo
            if foto[0] == codice:
                return foto
    return False

def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    # TODO
    anno=str(anno)
    titoli_foto=[]

    if anno in album:
        for foto in album[anno]:
            titoli_foto.append(foto[1])

    titoli_foto.sort()
    return titoli_foto


def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()