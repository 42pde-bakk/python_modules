def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    # https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-python-variable-is-a-function
    if not callable(function_to_apply):
        raise RuntimeError("function not callable")
    out = iterable[0]
    for item in iterable[1:]:
        out = function_to_apply(out, item)
    return out


if __name__ == '__main__':
    # Example 3:
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    result = ft_reduce(lambda u, v: u + v, lst)
    # Output:
    print(result)
    assert result == 'Hello world'
