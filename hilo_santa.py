import threading
import time
import random

class SantaClaus(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name}: Ho, ho, ho! Estoy listo para repartir regalos.")

        while True:
            # Simulando el tiempo que Santa pasa durmiendo hasta que es despertado
            time.sleep(random.randint(1, 5))

            print(f"{self.name}: Zzz...")

            # Espera a ser despertado por un elfo
            print(f"{self.name}: Esperando a que un elfo me despierte...")
            elf_wake_event.wait()

            print(f"{self.name}: ¡Me han despertado! Es hora de repartir regalos.")

            # Simulando la entrega de regalos
            time.sleep(random.randint(2, 5))
            print(f"{self.name}: Regalos entregados. Ahora vuelvo a dormir.")
            elf_wake_event.clear()

class Elf(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        while True:
            # Simulando el tiempo que un elfo tarda en necesitar a Santa
            time.sleep(random.randint(3, 8))
            print(f"{self.name}: ¡Necesito ayuda de Santa!")

            # Despierta a Santa
            elf_wake_event.set()

# Creamos el evento para despertar a Santa
elf_wake_event = threading.Event()

# Creamos una instancia de Santa
santa = SantaClaus("Santa Claus")

# Creamos varias instancias de elfos
elf1 = Elf("Elfo 1")
elf2 = Elf("Elfo 2")
elf3 = Elf("Elfo 3")

# Iniciamos los hilos
santa.start()
elf1.start()
elf2.start()
elf3.start()