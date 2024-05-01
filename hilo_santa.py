import threading
import time
import random

class SantaClaus(threading.Thread):
    #Contadores de los renos y duendes para las condiciones para despertar a santa
    reindeer_count = 0
    elf_help_count = 0
    
    wake_lock = threading.Lock() #se utiliza para sincronizar el acceso a un recurso compartido, en este caso, el despertar de Santa Claus. 
    print_lock = threading.Lock() #se utiliza para sincronizar las operaciones de impresión a la consola.

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name}: Ho, ho, ho! Estoy listo para repartir regalos.")

        while True:
            # Simulando el tiempo que Santa pasa durmiendo hasta que es despertado
            time.sleep(random.randint(1, 5))

            print(f"{self.name}: Zzz...")

            # Espera a ser despertado por un elfo o todos los renos
            with SantaClaus.print_lock, SantaClaus.wake_lock:
                if SantaClaus.reindeer_count == 9 or SantaClaus.elf_help_count > 0:
                    print(f"{self.name}: ¡Me han despertado! Es hora de repartir regalos.")
                    # Resetear los contadores
                    SantaClaus.reindeer_count = 0
                    SantaClaus.elf_help_count = 0

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
            with SantaClaus.print_lock:
                print(f"{self.name}: ¡Necesito ayuda de Santa!")

            # Incrementa el contador de elfos
            SantaClaus.elf_help_count += 1

            # Despierta a Santa si algún elfo necesita ayuda
            if SantaClaus.elf_help_count > 0:
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