import csv
#importo le nuove classi create per poterci lavorare su
from stand import *
from espositori import Espositori
class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.stand=[] #creo lista stand ed espositori in cui inserirò le informazioni
        self.espositori=[]

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try: #gestisco le eccezioni in caso di file non trovato
            with open(file_path, "r",encoding="utf-8") as f:
                reader=csv.reader(f) #leggo il file con reader, che restituisce una lista
                for row in reader:
                    codice=row[0]
                    iniziale=codice[0] #prendo l'iniziale della prima parola
                    if iniziale=="S": #distinguo gli stand dagli espositori
                        if len(row)==5: #se la lunghezza è 5, si tratta di uno stand speciale
                            if row[-1].isdigit(): #controllo sia un numero
                                s_prese=StandConPrese(row[0],row[1],row[2],row[3],row[4])
                                self.stand.append(s_prese)
                            elif row[-1].isalpha(): #controllo sia un carattere
                                s_premium=StandPremium(row[0],row[1],row[2],row[3],row[4])
                                self.stand.append(s_premium)
                        else: #altrimenti, è uno stand standard
                            s_standard=Stand(row[0],row[1],row[2],row[3])
                            self.stand.append(s_standard)
                    else: #aggiungo le informazioni sugli espositori alla lista
                        espositore=Espositori(row[0],row[1],row[2])
                        self.espositori.append(espositore)
        except FileNotFoundError:
            raise FileNotFoundError

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_trovato = None #creo due nuove variabili, associate allo stand ed espositori cercati
        espositore_trovato = None

        #controllo che lo stand esista
        for s in self.stand:
            if s.codice==codice_stand: #se esiste, lo definisco come quello cercato
                stand_trovato=s
        if stand_trovato is None: #altrimenti, scateno un'eccezione
            raise Exception("Stand inesistente")

        #controllo che l'espositore esista
        for e in self.espositori: #faccio lo stesso procedimento con l'espositore
            if e.codice==codice_espositore:
                espositore_trovato=e
        if espositore_trovato is None:
            raise Exception("Espositore inesistente")

        #controllo che lo stand sia disponibile
        if not stand_trovato.disponibile:
            raise Exception("Stand non disponibile")

        #controllo che l'espositore non abbia già uno stand
        for s in self.stand:
            if s.espositore==espositore_trovato:
                raise Exception("Espositore già assegnato")

        #registro l'associazione e aggiorno la disponibilità
        stand_trovato.espositore=espositore_trovato
        stand_trovato.disponibile=False

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for e in self.espositori: #per ogni espositore, lo stampo
            print(e)
            for s in self.stand:
                if s.espositore==e: #cerco lo stand assegnato all'espositore
                    print(s)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        #ordino gli stand in base al prezzo con la funzione sorted, mettendo come parametro il prezzo
        stand_ordinati=sorted(self.stand, key=lambda s: s.prezzo)
        return stand_ordinati
