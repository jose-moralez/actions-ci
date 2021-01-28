import numpy as np
from numba import njit

@njit
def frecuencia(arr: np.ndarray, valor: int) -> int:
    freq = 0
    for elem in arr:
        if elem == valor:
            freq += 1
    return freq
