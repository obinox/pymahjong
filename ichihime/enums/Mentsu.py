from enum import IntEnum
from typing import Self


class mentsu(IntEnum):
    SHUNTSU = 0x00, 0  # Anjun
    KOUTSU = 0x40, 4  # Ankou
    TOITSU = 0x80, 0
    KANTSU = 0xC0, 16  # Ankan

    KOKUSHI = 0x800, 0

    AKA = 0x0D - 0x05, 0

    def __new__(cls, value: int, fu: int) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.fu = fu
        return obj

    def __init__(self, value: int, fu: int) -> None:
        self._value_ = value
        self.fu = fu


class fuuro(IntEnum):
    KAMI = 0x100  # left pon, kan and chii first tile
    TOI = 0x200  # across pon, kan and chii second tile
    SHIMO = 0x300  # right pon, kan and chii third tile

    JI = 0x400  # ankan and kakan(pon+kan)
