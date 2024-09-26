from enum import IntEnum
from typing import Literal


class Agaru(IntEnum):
    TSUMO = 0x00, "tsumo"
    RON = 0x04, "ron"

    DABURI = 0x20, "double riichi"
    RIICHI = 0x10, "riichi"
    IPPATSU = 0x08, "ippatsu"

    HAITEI = 0x02, "haitei"
    HOUTEI = 0x06, "houtei"
    CHANKAN = 0x05, "chankan"
    RINSHAN = 0x01, "rinshan"

    def __new__(cls, value: int, string: str):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.string = string
        return obj

    def __init__(self, value: int, string: str) -> None:
        self._value_ = value
        self.string: str
