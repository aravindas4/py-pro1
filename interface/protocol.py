from typing import Protocol


class Flyer(Protocol):

    def fly(self) -> None:
        """A flyer can fly"""


class Board:

    def make_fly(self, obj: Flyer):
        return obj.fly()
