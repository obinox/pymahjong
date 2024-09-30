from enum import IntEnum
from typing import Self

from ichihime.Enum.Tile import Tile


class Mentsu(IntEnum):
    SHUNTSH = 0x00, 0  # Anjun
    KOUTSU = 0x40, 4  # Ankou
    TOITSU = 0x80, 0
    KANTSU = 0xC0, 16  # Ankan

    MINJUN = 0x100, 0
    MINKOU = 0x140, 2
    KAKAN = 0x180, 8
    DAIMINKAN = 0x1C0, 8

    KOKUSHI = 0x400, 8

    AKA = 0x200, 0

    def __new__(cls, value: int, fu: int) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.fu = fu
        return obj

    def __init__(self, value: int, fu: int) -> None:
        self._value_ = value
        self.fu = fu
