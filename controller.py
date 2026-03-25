import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view
        self._flagLingua = False
        self._flagModalita = False
        self._lingua = None
        self._modalita = None

    def handleSentence(self, txtIn, e):
        if self._flagLingua == False or self._flagModalita==False or txtIn == "":
            self._view._comunicazioni.controls.append(ft.Text("Non hai completato tutti i campi", color="red"))
            self._view.update()
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "
        if txtIn !="":
            match self._modalita:
                case "Default":
                    t1 = time.time()
                    parole = self._multiDic.searchWord(words, self._lingua)
                    for parola in parole:
                        if not parola.corretta:
                            paroleErrate = paroleErrate + str(parola) + " - "
                    t2 = time.time()
                    self._view._comunicazioni.controls.append(ft.Text(f"Frase inserita: {txtIn}"))
                    self._view._comunicazioni.controls.append(ft.Text(f"Parole errate: {paroleErrate}"))
                    self._view._comunicazioni.controls.append(ft.Text(f"Ci hai impiegato: {t2-t1} secondi"))
                    self._view.update()

                case "Lineare":
                    t1 = time.time()
                    parole = self._multiDic.searchWordLinear(words, self._lingua)
                    for parola in parole:
                        if not parola.corretta:
                            paroleErrate = paroleErrate + str(parola) + " "
                    t2 = time.time()
                    self._view._comunicazioni.controls.append(ft.Text(f"Frase inserita: {txtIn}"))
                    self._view._comunicazioni.controls.append(ft.Text(f"Parole errate: {paroleErrate}"))
                    self._view._comunicazioni.controls.append(ft.Text(f"Ci hai impiegato: {t2 - t1} secondi"))
                    self._view.update()

                case "Dicotomica":
                    t1 = time.time()
                    parole = self._multiDic.searchWordDichotomic(words, self._lingua)
                    for parola in parole:
                        if not parola.corretta:
                            paroleErrate = paroleErrate + str(parola) + " - "
                    t2 = time.time()
                    self._view._comunicazioni.controls.append(ft.Text(f"Frase inserita: {txtIn}"))
                    self._view._comunicazioni.controls.append(ft.Text(f"Parole errate: {paroleErrate}"))
                    self._view._comunicazioni.controls.append(ft.Text(f"Ci hai impiegato: {t2 - t1} secondi"))
                    self._view.update()
                case _:
                    return None
            self.pulisci()

    def printaLingua(self, x, e):
        self._flagLingua = False
        if x=="italian":
            d = self._multiDic._italian
        if x == "english":
            d = self._multiDic._english
        if x == "spanish" :
            d = self._multiDic._spanish
        if d!=None:
            self._view._comunicazioni.controls.append(ft.Text(f"La lingua scelta è {x}"))
            self._flagLingua = True
        else:
            self._view._comunicazioni.controls.append(ft.Text(f"La lingua scelta {x} non esiste"))
        self._lingua = x
        self._view.update()

    def printaModalita(self, x, e):
        self._flagModalita = False
        if self._lingua == None:
            self.lingua="Italian"
        try:
            if x == "Default":
                d = self._multiDic.searchWord("prova", self._lingua)
            if x == "Lineare":
                d = self._multiDic.searchWordLinear("prova", self._lingua)
            if x == "Dicotomica":
                d = self._multiDic.searchWordDichotomic("prova", self._lingua)
        except:
            self._view._comunicazioni.controls.append(ft.Text(f"LLa modalità {x} non è disponibile"))
        else:
            self._view._comunicazioni.controls.append(ft.Text(f"La modalità scelta è {x}"))
            self._flagModalita = True
            self._modalita = x
        self._view.update()


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def pulisci(self):
        self._view._inserisci.value = None
        self._view.update()


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text