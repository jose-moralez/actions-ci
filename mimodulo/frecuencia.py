import numpy as np

def frecuencia(arr: np.ndarray, valor: int) -> int:
    mascara = arr == valor
    return np.sum(mascara)
