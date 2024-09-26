from enum import Enum, IntEnum
from typing import Self

from ichihime.Group import Group


class Tile(IntEnum):
    """🀫"""

    MAN1 = 0x01, 1, Group.MAN
    """🀇"""
    MAN2 = 0x02, 2, Group.MAN
    """🀈"""
    MAN3 = 0x03, 3, Group.MAN
    """🀉"""
    MAN4 = 0x04, 4, Group.MAN
    """🀊"""
    MAN5 = 0x05, 5, Group.MAN
    """🀋"""
    MAN6 = 0x06, 6, Group.MAN
    """🀌"""
    MAN7 = 0x07, 7, Group.MAN
    """🀍"""
    MAN8 = 0x08, 8, Group.MAN
    """🀎"""
    MAN9 = 0x09, 9, Group.MAN
    """🀏"""
    # MAN0 = 0x0D, 5, Group.MAN
    """🀋"""
    PIN1 = 0x11, 1, Group.PIN
    """🀙"""
    PIN2 = 0x12, 2, Group.PIN
    """🀚"""
    PIN3 = 0x13, 3, Group.PIN
    """🀛"""
    PIN4 = 0x14, 4, Group.PIN
    """🀜"""
    PIN5 = 0x15, 5, Group.PIN
    """🀝"""
    PIN6 = 0x16, 6, Group.PIN
    """🀞"""
    PIN7 = 0x17, 7, Group.PIN
    """🀟"""
    PIN8 = 0x18, 8, Group.PIN
    """🀠"""
    PIN9 = 0x19, 9, Group.PIN
    """🀡"""
    # PIN0 = 0x1D, 5, Group.PIN
    """🀝"""
    SOU1 = 0x21, 1, Group.SOU
    """🀐"""
    SOU2 = 0x22, 2, Group.SOU
    """🀑"""
    SOU3 = 0x23, 3, Group.SOU
    """🀒"""
    SOU4 = 0x24, 4, Group.SOU
    """🀓"""
    SOU5 = 0x25, 5, Group.SOU
    """🀔"""
    SOU6 = 0x26, 6, Group.SOU
    """🀕"""
    SOU7 = 0x27, 7, Group.SOU
    """🀖"""
    SOU8 = 0x28, 8, Group.SOU
    """🀗"""
    SOU9 = 0x29, 9, Group.SOU
    """🀘"""
    # SOU0 = 0x2D, 5, Group.SOU
    """🀔"""
    TON = 0x31, 0, Group.KAZE
    """🀀"""
    NAN = 0x32, 0, Group.KAZE
    """🀁"""
    SHAA = 0x33, 0, Group.KAZE
    """🀂"""
    PEI = 0x34, 0, Group.KAZE
    """🀃"""
    HAKU = 0x35, 0, Group.SANGEN
    """🀆"""
    HATSU = 0x36, 0, Group.SANGEN
    """🀅"""
    CHUN = 0x37, 0, Group.SANGEN
    """🀄"""

    def __new__(cls, value: int, actual: int, group: Group) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.group = group
        obj.actual = actual
        return obj

    def __init__(self, value: int, actual: int, group: Group) -> None:
        self._value_ = value
        self.actual: int
        self.group: Group


class ShortTile(Enum):
    m1, m2, m3, m4, m5, m6, m7, m8, m9 = Tile.MAN1, Tile.MAN2, Tile.MAN3, Tile.MAN4, Tile.MAN5, Tile.MAN6, Tile.MAN7, Tile.MAN8, Tile.MAN9
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = Tile.PIN1, Tile.PIN2, Tile.PIN3, Tile.PIN4, Tile.PIN5, Tile.PIN6, Tile.PIN7, Tile.PIN8, Tile.PIN9
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = Tile.SOU1, Tile.SOU2, Tile.SOU3, Tile.SOU4, Tile.SOU5, Tile.SOU6, Tile.SOU7, Tile.SOU8, Tile.SOU9
    z1, z2, z3, z4, z5, z6, z7 = Tile.TON, Tile.NAN, Tile.SHAA, Tile.PEI, Tile.HAKU, Tile.HATSU, Tile.CHUN
