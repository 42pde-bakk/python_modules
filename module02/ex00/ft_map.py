def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if not function_to_apply or not iterable:
        return None
    for item in iterable:
        yield function_to_apply(item)


if __name__ == '__main__':
    # Example 1:
    x = [1, 2, 3, 4, 5]
    result = ft_map(lambda dum: dum + 1, x)
    # Output:
    print(result)
    # The adress will be different
    result = list(ft_map(lambda t: t + 1, x))
    # Output:
    assert result == [2, 3, 4, 5, 6]
