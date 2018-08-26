import random

def _get_random_char():
    c = random.randint(0, 36)
    if c < 10:
        return str(c)
    return chr(65 + c - 10)


def cratesession():
    res = ''
    for _ in range(4):
        res += _get_random_char()
    return res