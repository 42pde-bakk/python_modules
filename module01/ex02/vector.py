import copy


class Vector:
    def __init__(self, arg):
        if arg is None:
            self.values = []
            self.shape = 0, 0
        elif isinstance(arg, int):
            self.values = [[float(i)] for i in range(arg)]
            self.shape = arg, 1
        elif isinstance(arg, list):
            self.values = copy.deepcopy(arg)
            self.shape = len(arg), len(arg[0])
            assert all(len(elem) == len(arg[0]) for elem in arg)
        elif isinstance(arg, Vector):
            self.values = copy.deepcopy(arg.values)
            self.shape = copy.deepcopy(arg.shape)
        elif isinstance(arg, tuple):
            assert len(arg) == 2 and arg[0] < arg[1]
            print('tuple')
            self.values = [[float(i)] for i in range(arg[0], arg[1])]
            self.shape = len(self.values[0]), 1
        elif isinstance(arg, range):
            self.values = [[float(i)] for i in arg]
            self.shape = len(self.values[0]), 1
        else:
            print(f'{arg=}, type={type(arg)}')
            raise TypeError("What are you tryna give me?")

    def __yield_values(self):
        if self.shape[0] == 1:
            for elem in self.values[0]:
                yield elem
        elif self.shape[1] == 1:
            for elem in self.values:
                yield elem[0]
        else:
            return NotImplemented

    def dot(self, vec) -> float:
        if isinstance(vec, Vector) and self.shape == vec.shape:
            return sum([a * b for (a, b) in zip(self.__yield_values(), vec.__yield_values())])
        return NotImplemented

    def T(self):
        out = Vector(None)
        if self.shape[0] == 1:
            out.values = [[x] for x in self.values[0]]
        elif self.shape[1]:
            out.values = [[x[0] for x in self.values]]
        else:
            return NotImplemented
        out.shape = self.shape[::-1]
        return out

    def __mul__(self, mult):
        out = Vector(self)
        if self.shape[0] == 1:
            out.values = [[mult * x for x in self.values[0]]]
        elif self.shape[1] == 1:
            out.values = [[mult * x[0]] for x in self.values]
        else:
            return NotImplemented
        return out

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, div):
        out = Vector(self)
        if not isinstance(div, int) and not isinstance(div, float):
            return NotImplemented
        if self.shape[0] == 1:
            out.values = [[x / div for x in self.values[0]]]
        elif self.shape[1] == 1:
            out.values = [[x[0] / div] for x in self.values]
        else:
            return NotImplemented
        return out

    def __rtruediv__(self, other):
        return NotImplemented

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if self.shape != other.shape:
            raise ValueError
        if self.shape == (0, 0):
            return Vector(None)
        out = Vector(None)
        out.shape = self.shape
        if self.shape[0] == 1:
            out.values = [[a + b for (a, b) in zip(self.values[0], other.values[0])]]
        elif self.shape[1] == 1:
            out.values = [[a + b] for (a, b) in zip(self.values, other.values)]
        else:
            return NotImplemented
        return out

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(other * -1)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __str__(self):
        return f'{self.values}'

    def __repr__(self):
        return self.__str__()
