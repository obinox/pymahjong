from enum import IntEnum


class group(IntEnum):
    MAN = 0, 0x00, "m", 9
    PIN = 1, 0x10, "p", 9
    SOU = 2, 0x20, "s", 9
    KZE = 3, 0x30, "z", 4
    SGN = 4, 0x34, "z", 3

    def __new__(cls, value: int, index: int, string: str, count: int):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.string = string
        obj.index = index
        obj.count = count
        return obj

    def __init__(self, value: int, index: int, string: str, count: int) -> None:
        self._value_ = value
        self.index: int
        self.string: str
        self.count: int
