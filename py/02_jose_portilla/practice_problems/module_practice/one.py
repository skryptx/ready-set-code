from functools import reduce


def add(*args) -> int:
    print(f"__name__ of one.py: {__name__}")
    return reduce(lambda a, b: a+b, list(args), 0)
