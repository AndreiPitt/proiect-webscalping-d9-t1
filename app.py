import time

import schedule
from web import web
from produse import produse

"""
Pagini predefinite

     flag = 1 --> Drmax
     flag = 2 --> Napofarm
     flag = 3 --> Helpnet
"""

pagina1 = web("https://www.drmax.ro/medicamente-fara-reteta/vitamine-si-minerale")
pagina1.creazaPagina(flag=1)
# pagina1.afiseazaProduse()

pagina2 = web("https://www.farmaciilenapofarm.ro/minerale-vitamine")
pagina2.creazaPagina(flag=2)

pagina3 = web("https://www.helpnet.ro/uz-general")
pagina3.creazaPagina(flag=3)


def start():
    def pornesteAutomat():
        produse.scrieinfisier(a=pagina1, b=pagina2, c=pagina3)
        print(f"Produsele au fost adaugate in lista!")

    print("Aplicatia ruleaza....")
    schedule.every().day.at("00:15").do(pornesteAutomat)

    while True:
        schedule.run_pending()
        time.sleep(1)
