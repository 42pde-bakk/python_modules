from vector import Vector

if __name__ == '__main__':
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    assert v1.shape == (4, 1)
    assert v1.values == [[0.0], [1.0], [2.0], [3.0]]
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    assert v2.shape == (1, 4)
    assert v2.values == [[0.0, 1.0, 2.0, 3.0]]

    v1_transposed = v1.T()
    v2_transposed = v2.T()
    assert v1_transposed.shape == (1, 4)
    assert v1.shape == (4, 1)
    assert v1_transposed.values == [[0.0, 1.0, 2.0, 3.0]]
    assert v2_transposed.shape == (4, 1)
    assert v2_transposed.values == [[0.0], [1.0], [2.0], [3.0]]
    assert v1.values == [[0.0], [1.0], [2.0], [3.0]]
    assert v2.values == [[0.0, 1.0, 2.0, 3.0]]

    v2_multiplied = v2 * 5
    assert v2_multiplied.shape == v2.shape
    print(f'{v2_multiplied.values=}')
    assert v2_multiplied.values == [[0.0, 5.0, 10.0, 15.0]]

    v2_divided = v2 / 2
    assert v2_divided.shape == v2.shape
    assert v2_divided.values == [[0.0, 0.5, 1.0, 1.5]]

    print(v1)
    print(f'{v1!r}')

    # Example 1:
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print(v1.dot(v2))
    # Expected output:
    # 18.0
    assert v1.dot(v2) == 18.0

    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print(v3.dot(v4))
    # Expected output:
    # 13.0
    assert v3.dot(v4) == 14.0
    # subject is wrong.

    Vector(range(4))
