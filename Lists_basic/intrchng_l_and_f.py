def intrchng(lst: list) -> list:
    """Given a list, write a Python program to swap first
     and last element of the list.
    """
    # swapping last and first element using indexing
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(intrchng([1, 3, 5, 6, 7]))
