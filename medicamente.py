class medicamente:
    def __init__(self, a: object, tipdedate, numeclasa):
        self.date = a.soup.findAll(tipdedate, numeclasa)
        self.listademedicamente = []
        self.listapreturi = []
        self.produse = []

    def actualizareMedicamentDrmax(self, tipdedate, numeclasa):
        for medicament in self.date:
            medicament = medicament.find(tipdedate, numeclasa).text
            self.listademedicamente.append(medicament.strip())

    def actualizareMedicamentNapofarm(self):
        for medicament in self.date:
            self.listademedicamente.append(medicament.text.strip())

    def actualizareMedicamentHelpNet(self):
        for medicament in self.date:
            self.listademedicamente.append(medicament.text.strip())
        self.listademedicamente[2] = self.listademedicamente[2][0:33]

    def actualizarePretDrmax(self, a: object, tipdedate, numeclasa):
        for pret in a.soup.findAll(tipdedate, numeclasa):
            self.listapreturi.append(pret.text.strip())
        del self.listapreturi[0]
        del self.listapreturi[1]
        del self.listapreturi[2]
        for i in range(0, len(self.listapreturi)):
            self.listapreturi[i] = self.listapreturi[i].strip("  Lei")
            self.listapreturi[i] = self.listapreturi[i].replace(",", ".")
            self.listapreturi[i] = float(self.listapreturi[i])

    def actualizarePretNapofarm(self, a: object, tipdedate, numeclasa):
        temporar = []
        for pret in a.soup.findAll(tipdedate, numeclasa):
            temporar.append(pret.text.strip())

        for pret in temporar:
            pret = pret.strip()
            pret = pret.strip(" RON")
            pret = pret[0:2] + "." + pret[2:4]
            self.listapreturi.append(pret)

    def actualizarePretHelpNet(self, a: object, tipdedate, numeclasa):
        preturi = []
        for p in a.soup.findAll(tipdedate, numeclasa):
            preturi.append(p)
        for pret in preturi:
            pret = pret.text.strip()
            pret = pret.replace(",", ".")
            pret = pret.strip("\xa0 RON")
            pret = float(pret)
            self.listapreturi.append(pret)

    def listaProduse(self):
        for i in range(0, len(self.listademedicamente)):
            self.produse.append((self.listademedicamente[i], self.listapreturi[i]))
        return self.produse

    def afiseazaProduse(self):
        for pereche in self.produse:
            print(pereche)
