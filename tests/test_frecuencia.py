import numpy as np
import pytest

from mimodulo.frecuencia import frecuencia

@pytest.mark.parametrize('veces,valor', [(0, 1), (10, 2), (20, 3)])
def test_frecuencia(veces: int, valor: int):
    otros_valores = np.random.randint(low=1, high=5, size=100) + valor
    arr = np.asarray([valor]*veces + otros_valores.tolist())
    assert frecuencia(arr, valor) == veces
