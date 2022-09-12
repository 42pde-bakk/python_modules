from typing import Iterable
import numpy as np


class NumPyCreator:
    def __init__(self):
        pass

    def from_list(self, lst: list, dtype=None) -> np.ndarray:
        return np.asarray(lst, dtype=dtype)

    def from_tuple(self, tpl: tuple, dtype=None) -> np.ndarray:
        return np.asarray(tpl, dtype=dtype)

    def from_iterable(self, itr: Iterable, dtype=None) -> np.ndarray:
        return np.fromiter(itr, dtype=dtype)

    def from_shape(self, shape: tuple, value: int = 0, dtype=None) -> np.ndarray:
        return np.full(shape=shape, fill_value=value, dtype=dtype)

    def random(self, shape: tuple, dtype=None) -> np.ndarray:
        return np.empty(shape=shape, dtype=dtype)

    def identity(self, n: int, dtype=None) -> np.ndarray:
        return np.identity(n, dtype=dtype)
