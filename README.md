# Problema de Santa Claus en Python

Este repositorio contiene una implementación del problema de Santa Claus utilizando hilos en Python.

## Descripción

El problema de Santa Claus es un problema clásico de concurrencia y sincronización. En este problema, Santa Claus duerme hasta que es despertado por un elfo que necesita ayuda para fabricar un juguete, o hasta que todos los renos han vuelto de vacaciones.

En esta implementación, Santa Claus y los elfos son representados por hilos. Utilizamos un objeto `threading.Event` para simular el despertar de Santa Claus.

## Código

El código consta de dos clases principales: `SantaClaus` y `Elf`.

- `SantaClaus`: Esta clase representa a Santa Claus. Santa duerme hasta que es despertado por un elfo. Una vez despertado, reparte regalos y luego vuelve a dormir.
- `Elf`: Esta clase representa a un elfo. Los elfos trabajan fabricando juguetes. Cuando un elfo necesita ayuda, despierta a Santa Claus.

## Ejecución

Para ejecutar el programa, simplemente ejecuta el script de Python en tu terminal:

```bash
python santa_claus_problem.py
