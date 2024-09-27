from enum import Enum, IntEnum
from typing import Literal


class Group(IntEnum):
    MAN = 0, 0x00, "m"
    PIN = 1, 0x10, "p"
    SOU = 2, 0x20, "s"
    KAZE = 3, 0x30, "z"
    SANGEN = 4, 0x33, "z"

    def __new__(cls, value: int, index: int, string: str):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.string = string
        obj.index = index
        return obj

    def __init__(self, value: int, index: int, string: str) -> None:
        self._value_ = value
        self.index: int
        self.string: str
