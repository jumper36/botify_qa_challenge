from operator import truediv, add, mul, sub


def division(a, b):
    """
        returns division of 2 numbers
        >>> division(4, 2)
        2
    """
    return a / b


def addition(a, b):
    """
        returns addition of 2 numbers
        >>> addition(3, 5)
        8
    """
    return a + b


def subtraction(a, b):
    """
         returns subtraction of 2 numbers
         >>> subtraction(7, 5)
         2
    """
    return a - b


def multiplication(a, b):
    """
         returns the multiplication of 2 numbers
         >>> multiplication (4, 6)
         24
    """
    return a * b


def percentage(a, b):
    """
          returns the percentage of the division of 2 numbers
          >>> percentage(1, 1)
          100%
    """
    return (a / b) * 100


if __name__ == "__main__":
    import doctest
    doctest.testmod()

