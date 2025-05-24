nums = [1, 2, 3, 4, 5, 6]


def square(num: int):
    return num**2


def is_even(num: int):
    if num % 2 == 0:
        return True
    return False


print(list(map(square, nums)))
print(list(filter(is_even, nums)))
