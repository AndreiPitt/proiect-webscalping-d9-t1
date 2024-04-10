from datetime import datetime

now = datetime.now()


class produse:
    @classmethod
    def citesteFisierul(cls):
        with open("produse.csv", "r") as f:
            if len(f.read(1)) == 0:
                print("Fisier gol")
            else:
                for rand in f.readlines():
                    if rand.endswith("\n"):
                        temp = rand.find("\n")
                        rand = rand[0:temp]
                    if rand[0].isdigit():
                        rand = str(rand)
                        print(rand)  # printeaza data citita
                    else:
                        print(rand)

    @classmethod
    def scrieinfisier(cls, a: object, b: object, c: object):
        with open("produse.csv", "a") as f:
            f.write(now.strftime("%d/%m/%Y %H:%M:%S\n"))

            for produs in a.listadrmax:
                """
                Caracterul μ provoaca eroare la adaugarea produsului in fisier
                """
                produs = list(produs)
                produs[0] = produs[0].replace("μ", "u")
                f.write(f"({produs[0]},{produs[1]})\n")

            for produs in b.listanapofarm:
                if produs[0].endswith('\u03bc'):
                    temp = produs[0].find('\u03bc')
                    produs[0] = produs[0][0:temp]
                f.write(f"({produs[0]},{produs[1]})\n")

            for produs in c.listahelpnet:
                if produs[0].endswith('\u03bc'):
                    temp = produs[0].find('\u03bc')
                    produs[0] = produs[0][0:temp]
                f.write(f"({produs[0]},{produs[1]})\n")
