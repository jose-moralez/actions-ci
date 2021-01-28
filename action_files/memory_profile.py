import numpy as np

from mimodulo.frecuencia import frecuencia


if __name__ == '__main__':
    arreglo_grande = np.random.randint(0, 1_000, size=100_000_000) # ~ 760MB
    for i in range(10):
        frecuencia(arreglo_grande, i)
