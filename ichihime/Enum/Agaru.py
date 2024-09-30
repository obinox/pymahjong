from enum import IntEnum
from typing import Literal


class Agaru(IntEnum):
    TSUMO = 0x00, "tsumo"
    RON = 0x08, "ron"

    RIICHI = 0x10, "riichi"
    DABURI = 0x20, "double riichi"
    OPENRI = 0x40, "open riichi"
    OPENDABURI = 0x60, "double open riichi"

    IPPATSU = 0x80, "ippatsu"

    HAITEI = 0x02, "haitei"
    HOUTEI = 0x0A, "houtei"
    CHANKAN = 0x09, "chankan"
    RINSHAN = 0x01, "rinshan"

    TSUBAME = 0x0C, "tsubamegaeshi"
    KANFURI = 0x0C, "kanfuri"
    RENKAIHOU = 0x04, "renkaihou"

    def __new__(cls, value: int, string: str):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.string = string
        return obj

    def __init__(self, value: int, string: str) -> None:
        self._value_ = value
        self.string: str

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(0x{self.__hash__():0>2x})"
