import random
import string
from sys import maxsize


def random_int(*args) -> int:
    """Returns a random int ranging [minsize - maxsize] by default, [args[0] - maxsize], or [args[0] - args[1]]."""
    if len(args) is 0:
        return random.randint(((maxsize * -1) + 1), maxsize)
    elif len(args) is 1:
        return random.randint(args[0], maxsize)
    elif len(args) is 2:
        return random.randint(args[0], args[1])
    else:
        raise ValueError("Invalid Arguments: Only " +
                         "random_int()[minsize - maxsize], " +
                         "random_int(minimum: int)[minimum - maxsize], " +
                         "random_int(minimum: int, maximum: int)[minimum - maximum] " +
                         "available.")
def random_str(*args) -> str:
    """Returns a concatenated string of random characters with size 10 by default, or size args[0]."""
    if len(args) is 0:
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    elif len(args) is 1:
        return ''.join(random.choice(string.ascii_lowercase) for i in range(args[0]))
    else:
        raise ValueError("Invalid Arguments: Only " +
                         "random_str(), " +
                         "random_str(char_len), " +
                         "available.")

def random_chr() -> chr:
    """Returns a random character."""
    return random_str(1)

def random_float(*args) -> float:
    """"""
    return 00.00

def random_list(*args) -> list:
    """"""
    return []
def random_obj(*args) -> object:
    """"""
    return None

