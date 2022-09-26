from typing import Iterable
import numpy as np


class NumPyCreator:
    def __init__(self):
        pass

    def from_list(self, lst: list, dtype=None) -> np.ndarray | None:
        if not isinstance(lst, list) or not lst or any(len(x) != len(lst[0]) for x in lst):
            return None
        return np.asarray(lst, dtype=dtype)

    def from_tuple(self, tpl: tuple, dtype=None) -> np.ndarray | None:
        if not isinstance(tpl, tuple) or not tpl or any(len(x) != len(tpl[0]) for x in tpl):
            return None
        return np.asarray(tpl, dtype=dtype)

    def from_iterable(self, itr: Iterable, dtype=None) -> np.ndarray | None:
        if not isinstance(itr, Iterable):
            return None
        return np.fromiter(itr, dtype=dtype)

    def from_shape(self, shape: tuple, value: int = 0, dtype=None) -> np.ndarray | None:
        if not isinstance(shape, tuple) or not isinstance(value, int) or any(x < 0 for x in shape):
            return None
        return np.full(shape=shape, fill_value=value, dtype=dtype)

    def random(self, shape: tuple, dtype=None) -> np.ndarray | None:
        if not isinstance(shape, tuple):
            return None
        # On my laptop it outputs an array of zeroes
        # but this is the function to use for an unitialized array:
        # https://numpy.org/doc/stable/reference/generated/numpy.empty.html
        return np.empty(shape=shape, dtype=dtype)

    def identity(self, n: int, dtype=None) -> np.ndarray | None:
        if not isinstance(n, int) or n < 0:
            return None
        return np.identity(n, dtype=dtype)
