from datetime import datetime

class produse:
    @classmethod
    def citesteFisierul(cls):
        with open("produse.csv", "r",encoding="UTF-8") as f:
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
        """
        Aceasta este o metoda de clasa.
        Functia scrieinfisier adauga in fisierul de tip csv date de pe o anume pagina a fiecarei tip de site.
        Fiecare site (drmax,napofarm,helpnet) au structura diferita.
        Se pot introduce orice pagina web de pe site-urile respective cu conditia de pasa functiei cate o pagina de pe
        fiecare site pentru comparatie. (Cerinta proiect)
        """
        now = datetime.now()
        with open("produse.csv", "a", encoding="UTF-8") as f:
            f.write(now.strftime("%d/%m/%Y %H:%M:%S\n"))
            for produs in a.listadrmax:
                f.write(f"({produs[0]},{produs[1]})\n")

            for produs in b.listanapofarm:
                f.write(f"({produs[0]},{produs[1]})\n")

            for produs in c.listahelpnet:
                f.write(f"({produs[0]},{produs[1]})\n")
