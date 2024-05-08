import time

from pagini import *
from produse import produse

def start():
    @schedule.repeat(schedule.every().minute.at(":00"))
    def pornesteAutomat():
        produse.scrieinfisier(a=pagina1, b=pagina2, c=pagina3)
        print(f"Produsele au fost adaugate in lista!")

    print("Aplicatia ruleaza....")

    while True:
        schedule.run_pending()
        time.sleep(1)