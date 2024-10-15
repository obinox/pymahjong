from typing import Self

from ichihime.enums import player as _PL


class score(int):
    def __init__(self, han: int, fu: int) -> None:
        self.han = han
        if fu != 25:
            fu = (fu // 10 + bool(fu % 10)) * 10
        self.fu = fu

        # under mangan (<3h70f|4h40f|5h)
        # F * (2 ** (2 + H))

    def __new__(cls, han: int, fu: int) -> Self:
        if fu != 25:
            fu = (fu // 10 + bool(fu % 10)) * 10
        return super().__new__(cls, fu * pow(2, 2 + han))

    def __str__(self) -> str:
        return f"{self.han}han {self.fu}fu"

    def __repr__(self) -> str:
        return f"{self.han}h{self.fu}f"

    def __matmul__(self, value: int) -> int:
        k = 0
        match value:
            case _PL.KOOYA:
                k = 2
            case _PL.OYAKO:
                k = 2
            case _PL.KOKO:
                k = 1
            case _PL.OYA:
                k = 6
            case _PL.KO:
                k = 4
            case _:
                raise ValueError

        if self > 2000:
            if self.han in {3, 4, 5}:
                return 2000 * k
            elif self.han in {6, 7}:
                return 3000 * k
            elif self.han in {8, 9, 10}:
                return 4000 * k
            elif self.han in {11, 12}:
                return 6000 * k
            elif self.han >= 13:
                return 8000 * (self.han // 13) * k
        else:
            return ((self * k) // 100 + bool(self % 100)) * 100

    def scores(self):
        return (self @ _PL.KO, self @ _PL.OYA, self @ _PL.KOKO, self @ _PL.OYAKO, self @ _PL.KOOYA)
