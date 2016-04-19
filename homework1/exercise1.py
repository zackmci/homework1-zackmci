# the documenation has been written for you in this exercise

def collatz_step(n):
    """Returns the result of the Collatz function.

    The Collatz function C : N -> N is used in `collatz` to generate collatz
    sequences. Raises an error if n < 1.

    Parameters
    ----------
    n : int

    Returns
    -------
    int
        The result of C(n).

    """
    try:
        while n >= 1:
            if n == 1:
                n = 1
            elif n %2 == 0:
                n = n / 2
            elif n % 2 != 0:
                n = 3 * n + 1
            return n
    except ValueError:
        raise ValueError
         

    

def collatz(n):
    """Returns the Collatz sequence beginning with `n`.

    It is conjectured that Collatz sequences all end with `1`. Calls
    `collatz_step` at each iteration.

    Parameters
    ----------
    n : int

    Returns
    -------
    sequence : list
        A Collatz sequence.

    """
    sequence = []

    while n != 1:
        if n > 1:
            sequence = sequence + [n]
            n = collatz_step(n)
        elif n < 1:
            n = collatz_step(n)
            sequence = sequence + [n]
            break
    if n == 1:
        sequence = sequence + [n]
        return sequence
    print sequence
