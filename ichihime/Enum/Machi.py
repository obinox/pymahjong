from enum import IntEnum
from typing import Self


class Machi(IntEnum):
    TAN = 0x00, 2
    KAN = 0x01, 2
    SHP = 0x02, 1
    PN3 = 0x03, 2
    PN7 = 0x07, 2
    RML = 0x0A, 1
    RMR = 0x0B, 1
    CHI = 0x0C, 25
    KMU = 0x0D, 0
    K13 = 0x0E, 0

    def __new__(cls, value: int, fu: int) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.fu = fu
        return obj

    def __init__(self, value: int, fu: int) -> None:
        self._value_ = value
        self.fu = fu

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
