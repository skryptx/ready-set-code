"""Dog class with breed and spots properties"""
from typing import override

class Dog:
    """
    name: string
    breed: string
    spots: boolean
    """

    species = "mammal"

    def __init__(self, name: str, breed: str, spots: bool):
        self.name = name
        self.breed = breed
        self.spots = spots

    @override
    def __str__(self) -> str:
        return (
            f"{self.name} is a {self.species}, a {self.breed} and "
            f"{"do" if self.spots else "does not"} have spots"
        )


jack = Dog("Jack", "pomerion", True)
softy = Dog("Softy", "golden retriever", False)

print(str(jack))
print(str(softy))

jack.species = "reptile"


print(str(jack))
print(str(softy))
