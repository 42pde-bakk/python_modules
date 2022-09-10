def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if function_to_apply is None or iterable is None:
        return None
    for item in iterable:
        if function_to_apply(item):
            yield item


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    result = ft_filter(lambda dum: not (dum % 2), x)
    # Output:
    print(result)
    result = list(ft_filter(lambda dum: not (dum % 2), x))
    print(result)
    assert result == [2, 4]
