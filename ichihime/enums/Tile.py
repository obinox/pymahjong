from enum import Enum, IntEnum
from typing import Self

from ichihime.enums import group as _GR


class tile(IntEnum):
    """🀫"""

    MAN1 = 0x01, 1, _GR.MAN
    """🀇"""
    MAN2 = 0x02, 2, _GR.MAN
    """🀈"""
    MAN3 = 0x03, 3, _GR.MAN
    """🀉"""
    MAN4 = 0x04, 4, _GR.MAN
    """🀊"""
    MAN5 = 0x05, 5, _GR.MAN
    """🀋"""
    MAN6 = 0x06, 6, _GR.MAN
    """🀌"""
    MAN7 = 0x07, 7, _GR.MAN
    """🀍"""
    MAN8 = 0x08, 8, _GR.MAN
    """🀎"""
    MAN9 = 0x09, 9, _GR.MAN
    """🀏"""
    MAN0 = 0x0D, 5, _GR.MAN
    """🀋"""
    PIN1 = 0x11, 1, _GR.PIN
    """🀙"""
    PIN2 = 0x12, 2, _GR.PIN
    """🀚"""
    PIN3 = 0x13, 3, _GR.PIN
    """🀛"""
    PIN4 = 0x14, 4, _GR.PIN
    """🀜"""
    PIN5 = 0x15, 5, _GR.PIN
    """🀝"""
    PIN6 = 0x16, 6, _GR.PIN
    """🀞"""
    PIN7 = 0x17, 7, _GR.PIN
    """🀟"""
    PIN8 = 0x18, 8, _GR.PIN
    """🀠"""
    PIN9 = 0x19, 9, _GR.PIN
    """🀡"""
    PIN0 = 0x1D, 5, _GR.PIN
    """🀝"""
    SOU1 = 0x21, 1, _GR.SOU
    """🀐"""
    SOU2 = 0x22, 2, _GR.SOU
    """🀑"""
    SOU3 = 0x23, 3, _GR.SOU
    """🀒"""
    SOU4 = 0x24, 4, _GR.SOU
    """🀓"""
    SOU5 = 0x25, 5, _GR.SOU
    """🀔"""
    SOU6 = 0x26, 6, _GR.SOU
    """🀕"""
    SOU7 = 0x27, 7, _GR.SOU
    """🀖"""
    SOU8 = 0x28, 8, _GR.SOU
    """🀗"""
    SOU9 = 0x29, 9, _GR.SOU
    """🀘"""
    SOU0 = 0x2D, 5, _GR.SOU
    """🀔"""
    TONN = 0x31, 0, _GR.KZE
    """🀀"""
    NANN = 0x32, 0, _GR.KZE
    """🀁"""
    SHAA = 0x33, 0, _GR.KZE
    """🀂"""
    PEII = 0x34, 0, _GR.KZE
    """🀃"""
    HAKU = 0x35, 0, _GR.SGN
    """🀆"""
    HTSU = 0x36, 0, _GR.SGN
    """🀅"""
    CHUN = 0x37, 0, _GR.SGN
    """🀄"""

    def __new__(cls, value: int, actual: int, group: _GR) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.group = group
        obj.actual = actual
        return obj

    def __init__(self, value: int, a: int, g: _GR) -> None:
        self._value_ = value
        self.actual: int
        self.group: _GR

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name  # f"{self.__class__.__name__}(0x{self.__hash__():0>2x})"


class shortTile(Enum):
    m1, m2, m3, m4, m5, m6, m7, m8, m9 = tile.MAN1, tile.MAN2, tile.MAN3, tile.MAN4, tile.MAN5, tile.MAN6, tile.MAN7, tile.MAN8, tile.MAN9
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = tile.PIN1, tile.PIN2, tile.PIN3, tile.PIN4, tile.PIN5, tile.PIN6, tile.PIN7, tile.PIN8, tile.PIN9
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = tile.SOU1, tile.SOU2, tile.SOU3, tile.SOU4, tile.SOU5, tile.SOU6, tile.SOU7, tile.SOU8, tile.SOU9
    z1, z2, z3, z4, z5, z6, z7 = tile.TONN, tile.NANN, tile.SHAA, tile.PEII, tile.HAKU, tile.HTSU, tile.CHUN
    m0, p0, s0 = tile.MAN0, tile.PIN0, tile.SOU0
