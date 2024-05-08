import requests
from bs4 import BeautifulSoup
from medicamente import medicamente


class web:
    """Extragere date"""

    numardepaginiweb = 0
    adresaweb = ""

    def __init__(self, adresaweb):
        web.numardepaginiweb += 1
        self.adresaweb = adresaweb
        self.nume = requests.get(self.adresaweb).text
        self.soup = BeautifulSoup(self.nume, "lxml")

        self.listanapofarm = None
        self.napofarm = None
        self.listadrmax = None
        self.drmax = None
        self.helpnet = None
        self.listahelpnet = None

    def creazaPagina(self, flag=1):
        if flag == 1:
            self.drmax = medicamente(self, "li", "tile tile--catalog")
            self.drmax.actualizareMedicamentDrmax("h3", "tile__title")
            self.drmax.actualizarePretDrmax(self, "div", "tile__price")
            self.listadrmax = self.drmax.listaProduse()
        elif flag == 2:
            self.napofarm = medicamente(self, "a", "product__name")
            self.napofarm.actualizareMedicamentNapofarm()
            self.napofarm.actualizarePretNapofarm(self, "div",
                                                  "product__info product__info--price-row "
                                                  "product__info--price-gross-row")
            self.listanapofarm = self.napofarm.listaProduse()
        elif flag == 3:
            self.helpnet = medicamente(self, "a", "product-box__link complex-link--hover-underline u-d-f u-fxd-c "
                                                  "u-fxg-1 u-ai-fs u-ord-2")
            self.helpnet.actualizareMedicamentHelpNet()

            self.helpnet.actualizarePretHelpNet(self, "p", "product-box__price u-d-f u-gap-2 u-jc-c u-fxw-w u-mb-3 "
                                                           "u-mt-auto u-lh-n")
            self.listahelpnet = self.helpnet.listaProduse()

    def afiseazaProduse(self, flag=1):
        if flag == 1:
            for pereche in self.listadrmax:
                print(pereche)
        elif flag == 2:
            for pereche in self.listanapofarm:
                print(pereche)
        elif flag == 3:
            for pereche in self.listahelpnet:
                print(pereche)



