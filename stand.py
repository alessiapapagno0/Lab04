class Stand:
    def __init__(self,codice,metratura,padiglione,prezzo): #creo la classe stand con le informazioni presenti nel file
        self.codice = codice
        self.metratura = metratura
        self.padiglione = padiglione
        self.prezzo = float(prezzo) #converto in float il prezzo per poterci lavorare su
        self.disponibile=True #aggiungo le informazioni sulla disponibilità
        self.espositore=None #inizializzo l'espositore come nullo, cosi da poterlo aggiornare
    def __str__(self):
        if self.disponibile:
            disponibilita="Disponibile"
        else:
            disponibilita="Non disponibile"

        return f"{self.codice}: {self.metratura}mq - Padiglione {self.padiglione} - Prezzo: {self.prezzo} - {disponibilita}"

#creo delle classi figlie per poter distinguere i vari tipi di stand
class StandConPrese(Stand):
    def __init__(self,codice,metratura,padiglione,prezzo,n_prese):
        super().__init__(codice,metratura,padiglione,prezzo) #metto tra parentesi gli attributi della classe padre
        self.n_prese = int(n_prese) #tengo conto del numero di prese

#creo una funzione che stabilisce il sovrapprezzo in base al numero di prese
    def sovrapprezzo(self):
        self.prezzo=self.prezzo*(1+0.07*self.n_prese)
        return self.prezzo #restituisco il nuovo prezzo


#in questo caso non è necessario definire una funzione per il sovrapprezzo, dato che è fisso
class StandPremium(Stand):
    def __init__(self,codice,metratura,padiglione,prezzo,posizione):
        super().__init__(codice,metratura,padiglione,prezzo)
        self.posizione = posizione #aggiungo l'informazione sulla posizione dello stand
        self.prezzo=self.prezzo*1.30 #modifico il prezzo iniziale della classe padre



