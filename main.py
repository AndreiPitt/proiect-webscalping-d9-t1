import interfata_grafica
import app
import threading
if __name__ == "__main__":
    fir1 = threading.Thread(target=interfata_grafica.start)
    fir1.start()
    fir2 = threading.Thread(target=app.start)
    fir2.start()