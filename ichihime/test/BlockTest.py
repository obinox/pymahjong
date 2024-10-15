from enum import Enum
from typing import Self

from ..enums import shortTile


class Test(str, Enum):
    W21 = "m1m1m1m2m3m4m6z1z1z1z2z2z2"
    W22 = "p1p1p1p2p3p4p5p6p7p9z2z2z2"
    W31 = "s1s1s1s3s4s5s6z1z1z1z2z2z2"
    W32 = "m1m1m1m2m3m4m6m7m8m9z1z1z1"
    W33 = "p1p1p1p2p3p3p3p4p5p5z1z1z1"
    W34 = "s1s1s2s2s2s3s3z1z1z1z2z2z2"
    W35 = "m1m1m2m2m3m3m4m4z1z1z2z2z2"
    W36 = "p1p1p2p2p2p2p3z1z1z1z2z2z2"
    W37 = "s1s1s2s3s3s3s3z1z1z1z2z2z2"
    W38 = "m1m1m1m3m3m4m5z1z1z1z2z2z2"
    W39 = "p1p1p1p2p3p4p4p5p6p6z1z1z1"
    W3A = "s1s1s1s2s3s3s4z1z1z1z2z2z2"
    W3B = "m1m1m2m3m3m4m4m4m5m5z1z1z1"
    W41 = "p1p1p2p2p3p3p4p4p5p5z1z1z1"
    W42 = "m1m1m1m2m3s1s1s1s2s3z1z1z1"
    W43 = "p1p1p1p2p3p4p5p5p6p6z1z1z1"
    W44 = "m1m1m1m2m3s1s1s2s2s3s3s4s4"
    W45 = "p1p1p1p2p2p3p3z1z1z1z2z2z2"
    W46 = "s1s1s1s2s2s2s3z1z1z1z2z2z2"
    W47 = "m1m1m1m2m3m4m5m6z1z1z2z2z2"
    W48 = "p2p3p3p3p4p5p6z1z1z1z2z2z2"
    W49 = "s1s1s1s3s4s5s6s7s8s9z1z1z1"
    W4A = "m1m1m1m3m4m5m6m8m8m8z1z1z1"
    W4B = "p2p2p3p3p3p3p4z1z1z1z2z2z2"
    W4C = "s2s2s2s3s3s4s5z1z1z1z2z2z2"
    W51 = "m1m2m3m4m4m4m5m5m6m6z1z1z1"
    W52 = "p2p2p2p3p4p5p6z1z1z1z2z2z2"
    W53 = "s1s1s1s2s3s3s4s5s5s5z1z1z1"
    W61 = "m1m1m1m2m3m4m5m6m7m8z1z1z1"
    W62 = "p2p2p2p3p4p5p6p6p7p8z1z1z1"
    W63 = "s1s2s3s3s3s3s4s5s6s7z1z1z1"
    W64 = "m1m1m1m2m2m2m3m3m3m4m4m5m5"
    W65 = "p2p2p2p3p3p3p4p4p4p5p5p5p6"
    W66 = "s1s1s2s2s3s3s4s4s4s5s5s5s6"
    W67 = "m2m2m2m3m4m4m4m4m5m6z1z1z1"
    W68 = "p1p1p1p2p2p2p3p4p5p6z1z1z1"
    W69 = "s1s1s1s2s2s2s3s3s4s5s6s7s8"
    W71 = "m2m3m3m3m3m4m5m6m7m7m7m7m8"
    W72 = "p2p3p4p4p4p4p5p6p6p6p6p7p8"
    W73 = "s2s2s2s3s3s3s4s4s4s5s6s6s6"
    W74 = "m1m1m1m2m2m3m3m4m4m5m5m6m6"
    W75 = "p2p3p4p4p4p5p5p5p6p6p6p7p8"
    W76 = "s2s2s2s3s4s5s6s6s6s7s7s8s8"
    W81 = "m2m2m2m3m4m5m6m6m7m7m7m7m8"
    W82 = "p1p1p1p2p3p4p5p6p6p6p6p7p8"
    W83 = "s2s2s2s3s4s5s6s7s7s7z1z1z1"
    W90 = "m1m1m1m2m3m4m5m6m7m8m9m9m9"
    W91 = "m1m1m1m2m3m4m5m6m7m8m8m9m9"

    def __new__(cls, value: str) -> Self:
        value = tuple(map(lambda x: shortTile["".join(x)].value, zip(value[::2], value[1::2])))
        obj = str.__new__(cls, value)
        obj._value_ = value
        return obj

    def __init__(self, value: str):
        value = tuple(map(lambda x: shortTile["".join(x)].value, zip(value[::2], value[1::2])))
        self._value_ = value

    @staticmethod
    def toTile(string: str):
        if type(string) == str:
            return tuple(
                map(
                    lambda x: shortTile["".join(x)].value,
                    zip(string[::2], string[1::2]),
                )
            )
        else:
            return string
