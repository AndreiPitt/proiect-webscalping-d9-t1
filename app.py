import time

from pagini import *
from produse import produse

def start():

    def pornesteAutomat():
        produse.scrieinfisier(a=pagina1, b=pagina2, c=pagina3)
        print(f"Produsele au fost adaugate in lista!")

    print("Aplicatia ruleaza....")
    schedule.every().day.at("00:15").do(pornesteAutomat)

    while True:
        schedule.run_pending()
        time.sleep(1)