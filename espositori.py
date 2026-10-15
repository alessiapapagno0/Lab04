#creo una classe per gli espositori
class Espositori:
    def __init__(self,codice,nome,cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
    def __str__(self):
        return f"{self.codice} {self.nome} {self.cognome}"
