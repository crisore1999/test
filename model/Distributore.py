from model.Bibita import Bibita
from model.Tessera import Tessera
from model.Colonna import Colonna

class Distributore:
    def __init__(self, bibita):
        self.bibita = bibita
        self.bevande = []
        self.tessere = []
        self.colonne = []

    def aggiungiBevanda(self, codice, nome, prezzo):
        bevanda = Bibita(codice, nome, prezzo)
        self.bevande.append(bevanda)
        print("bevanda aggiunta")
        print("codice: {}, nome: {}, prezzo: {}\n".format(codice, nome, prezzo))

    def getPrice(self, codiceBibita):
        trovato = False
        for x in self.bevande:
            if x.codice == codiceBibita:
                print("codice: {}, nome: {}, prezzo: {}\n".format(x.codice, x.nome, x.prezzo))
                trovato = True
                break
        if trovato != True:
            raise Exception("BevandaNonValida")

    def getNome(self, codiceBibita):
        trovato = False
        for x in self.bevande:
            if x.codice == codiceBibita:
                print("codice: {}, nome: {}, prezzo: {}\n".format(x.codice, x.nome, x.prezzo))
                trovato = True
                break
        if trovato != True:
            raise Exception("BevandaNonValida")


    def caricaTessera(self, codiceTessera, credito):
        tessera = Tessera(codiceTessera, credito)
        self.tessere.append(tessera)
        print("Tessera aggiunta")
        print("Codice: {}, Credito: {}\n".format(codiceTessera, credito))

    def leggiCredito(self, codice_Tessera):
        trovato = False
        for x in self.bevande:
            if x.codiceTessera == codice_Tessera:
                print("Codice: {}, Credito: {}\n".format(x.codiceTessera, x.credito))
                trovato = False
                break
        if trovato != False:
            raise Exception("TesseraNonValida ")

    def aggiornaColonna(self, nomeBibita, numeroLattine):
        colonna = Colonna(nomeBibita, numeroLattine)
        self.colonne.append(colonna);
        print("Numero Colonna: {}, Numero Colonna: {}, Numero Lattine: {}\n".format(len(self.colonne), nomeBibita,
                                                                                    numeroLattine))

    def erogaBibita(self, codiceBibita, codiceTessera):
        codice_bibita = None
        codice_tessera = None
        cred = None
        prez = None
        for x in self.bevande:
            if codiceBibita in x.codice:
                print("codiceBibita trovata!")
                prez = x.prezzo
                codice_bibita = "Found"

        for y in self.tessere:
            if str(codiceTessera) in str(y.codiceTessera):
                print("codiceTessera trovata!")
                cred = y.credito
                codice_tessera = "Found"

        if codice_bibita == "Found" and codice_tessera == "Found":
            if cred >= prez:
                canFlag = self.check_if()
                for z in self.colonne:
                    if z.nomeBibita[0] == codiceBibita and z.numeroLattine >= 1:
                        print("Before--> Nome Bibita:{} Numero Lattine: {}".format(z.nomeBibita, z.numeroLattine))
                        z.numeroLattine = z.numeroLattine - 1
                        print("After--> Nome Bibita:{} Numero Lattine: {}".format(z.nomeBibita, z.numeroLattine))
                        for y in self.tessere:
                            if str(codiceTessera) in str(y.codiceTessera):
                                print("Before--> Codice Tessera:{} Credito: {}".format(y.codiceTessera, y.credito))
                                cred = y.credito
                                y.credito = y.credito - prez
                                print("After--> Codice Tessera:{} Credito: {}".format(y.codiceTessera, y.credito))
            else:
                raise Exception("CreditoInsufficiente")

    def check_if(self):
        zero = 0
        for x in self.colonne:
            if str(x.numeroLattine) == str(0):
                zero = zero + 1
                if str(len(self.colonne)) == str(0):
                    print("throw exception zero value")
                    raise Exception("BevandaEsaurita")

