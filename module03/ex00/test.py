import numpy as np
from NumPyCreator import NumPyCreator


def main():
    npc = NumPyCreator()
    print(f"{npc.from_list([[1, 2, 3], [6, 3, 4]], dtype=object)=}\n")

    print(f"{npc.from_list([[1, 2, 3], [6, 4]], dtype=object)=}\n")

    print(f"{npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]], dtype=object)=}\n")

    print(f"{npc.from_list(((1, 2), (3, 4)))=}\n")

    print(f"{npc.from_tuple(('a', 'b', 'c'))=}\n")

    print(f"{npc.from_tuple(['a', 'b', 'c'])=}\n")

    print(f"{npc.from_iterable(range(5))=}\n")

    shape = (3, 5)
    print(f"{npc.from_shape(shape)=}\n")

    print(f"{npc.random(shape)=}\n")

    print(f"{npc.identity(4)=}")


if __name__ == '__main__':
    main()
