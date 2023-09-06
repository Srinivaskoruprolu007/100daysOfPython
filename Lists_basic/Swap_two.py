def swap_two(lst: list, pos1: int, pos2: int) -> list:
    """Given a list in Python and provided the positions of the elements,
    swap the two elements in the list."""
    lst[pos1 - 1], lst[pos2 - 1] = lst[pos2 - 1], lst[pos1 - 1]
    return lst


input_list = [23, 65, 19, 90]
print(swap_two(input_list, 1, 3))



