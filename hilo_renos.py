import threading
import time
import random

from hilo_santa import Elf, SantaClaus

class Reindeer(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        while True:
            # Simulando el tiempo que un reno tarda en necesitar a Santa
            time.sleep(random.randint(10, 20))
            print(f"{self.name}: ¡Necesito ayuda de Santa!")

            # Despierta a Santa
            reindeer_wake_event.set()

# Creamos el evento para despertar a Santa por los renos
reindeer_wake_event = threading.Event()

# Creamos una instancia de Santa
santa = SantaClaus("Santa Claus")

# Creamos varias instancias de elfos
elf1 = Elf("Elfo 1")
elf2 = Elf("Elfo 2")
elf3 = Elf("Elfo 3")

# Creamos varias instancias de renos
reindeer1 = Reindeer("Reno 1")
reindeer2 = Reindeer("Reno 2")
reindeer3 = Reindeer("Reno 3")

# Iniciamos los hilos
santa.start()
elf1.start()
elf2.start()
elf3.start()
reindeer1.start()
reindeer2.start()
reindeer3.start()
