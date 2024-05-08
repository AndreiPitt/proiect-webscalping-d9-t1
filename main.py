import time

from web import web
from produse import produse
import schedule

if __name__ == '__main__':

    """"
     Creare obiect de tip web care primeste ca parametrul url.


     Metode principale:
     obiect.creazaPagina(flag=)
     obiect.afiseazaPagina(flag=)
     produse.citesteFisierul()
     produse.scrieinfisier(a=pagina1,b=pagina2,c=pagina3)

     flag = 1 --> Drmax
     flag = 2 --> Napofarm
     flag = 3 --> Helpnet

    """

    pagina1 = web("https://www.drmax.ro/medicamente-fara-reteta/vitamine-si-minerale")
    pagina1.creazaPagina(flag=1)
    # pagina1.afiseazaProduse(flag=1)
    # print()
    pagina2 = web("https://www.farmaciilenapofarm.ro/minerale-vitamine")
    pagina2.creazaPagina(flag=2)
    # pagina2.afiseazaProduse(flag=2)
    # print()
    pagina3 = web("https://www.helpnet.ro/uz-general")
    pagina3.creazaPagina(flag=3)


    # pagina3.afiseazaProduse(flag = 3)
    #
    # print()

    # print(pagina1.listadrmax)
    # print(pagina2.listanapofarm)
    # print(pagina3.listahelpnet)

    # produse.citesteFisierul()

    @schedule.repeat(schedule.every().minute.at(":23"))
    # @schedule.repeat(schedule.every().day.at("12:00"))
    def pornesteAutomat():
        produse.scrieinfisier(a=pagina1, b=pagina2, c=pagina3)
        print(f"Produsele au fost adaugate in lista!")


    print("Aplicatia ruleaza....")
    while True:
        schedule.run_pending()
        time.sleep(1)
