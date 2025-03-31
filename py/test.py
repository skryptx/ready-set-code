from enum import auto, Enum


class PowersOfThree(Enum):

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return 3 ** (count + 1)
    FIRST = auto()
    SECOND = auto()


print(PowersOfThree.SECOND.value)
