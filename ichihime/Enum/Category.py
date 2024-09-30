from enum import Enum
from typing import List, Self

from ichihime.Enum.Tile import Tile


class Category(tuple, Enum):
    """🀫🀫🀫"""

    MANZU = (Tile.MAN1, Tile.MAN2, Tile.MAN3, Tile.MAN4, Tile.MAN5, Tile.MAN6, Tile.MAN7, Tile.MAN8, Tile.MAN9)
    """**Characters** 🀇🀈🀉🀊🀋🀌🀍🀎🀏"""
    PINZU = (Tile.PIN1, Tile.PIN2, Tile.PIN3, Tile.PIN4, Tile.PIN5, Tile.PIN6, Tile.PIN7, Tile.PIN8, Tile.PIN9)
    """**Circles** 🀙🀚🀛🀜🀝🀞🀟🀠🀡"""
    SOUZU = (Tile.SOU1, Tile.SOU2, Tile.SOU3, Tile.SOU4, Tile.SOU5, Tile.SOU6, Tile.SOU7, Tile.SOU8, Tile.SOU9)
    """**Bamboos** 🀐🀑🀒🀓🀔🀕🀖🀗🀘"""

    KAZEHAI = (Tile.TON, Tile.NAN, Tile.SHA, Tile.PEI)
    """**Winds** 🀀🀁🀂🀃"""
    SANGENPAI = (Tile.HAKU, Tile.HATSU, Tile.CHUN)
    """**Dragons** 🀆🀅🀄"""

    SHUUPAI = (*MANZU, *PINZU, *SOUZU)
    """**Numbers** 🀇🀈🀉🀊🀋🀌🀍🀎🀏 🀙🀚🀛🀜🀝🀞🀟🀠🀡 🀐🀑🀒🀓🀔🀕🀖🀗🀘"""

    MANZUCHUNCHAN = (Tile.MAN2, Tile.MAN3, Tile.MAN4, Tile.MAN5, Tile.MAN6, Tile.MAN7, Tile.MAN8)
    PINZUCHUNCHAN = (Tile.PIN2, Tile.PIN3, Tile.PIN4, Tile.PIN5, Tile.PIN6, Tile.PIN7, Tile.PIN8)
    SOUZUCHUNCHAN = (Tile.SOU2, Tile.SOU3, Tile.SOU4, Tile.SOU5, Tile.SOU6, Tile.SOU7, Tile.SOU8)
    CHUNCHANHAI = (*MANZUCHUNCHAN, *PINZUCHUNCHAN, *SOUZUCHUNCHAN)
    """**Simples** 🀈🀉🀊🀋🀌🀍🀎 🀚🀛🀜🀝🀞🀟🀠 🀑🀒🀓🀔🀕🀖🀗"""

    JIHAI = (*KAZEHAI, *SANGENPAI)
    """**Words** 🀀🀁🀂🀃 🀆🀅🀄"""
    ROUTOUHAI = (Tile.MAN1, Tile.MAN9, Tile.PIN1, Tile.PIN9, Tile.SOU1, Tile.SOU9)
    """**Ends** 🀇🀏 🀙🀡 🀐🀘"""

    YAOCHUUHAI = (*ROUTOUHAI, *JIHAI)
    """**Terminals** 🀇🀏 🀙🀡 🀐🀘 🀀🀁🀂🀃 🀆🀅🀄"""

    MIDORIPAI = (Tile.SOU2, Tile.SOU3, Tile.SOU4, Tile.SOU6, Tile.SOU8, Tile.HATSU)
    """**Greens** 🀑🀒🀓🀕🀗 🀅"""
    KUROPAI = (Tile.PIN2, Tile.PIN4, Tile.PIN8, *KAZEHAI)
    """**Blacks** 🀚🀜🀠 🀀🀁🀂🀃"""
    JAKUPAI = (Tile.SOU1, Tile.SOU5, Tile.SOU7, Tile.SOU9, Tile.CHUN)
    """**Peacocks** 🀐🀔🀖🀘 🀄"""

    # AKAPAI = (Tile.MAN0, Tile.PIN0, Tile.SOU0)
    # """**Reds** 🀋 🀝 🀔"""

    def __new__(cls, value: List[Tile]):
        obj = tuple.__new__(cls, value)
        obj._value_ = value
        return obj

    def __init__(self, value: List[Tile]) -> None:
        self._value_ = value

    @classmethod
    def allIn(cls, arr: List[Tile], category: tuple[Tile] | Self) -> bool:
        return all([x in category for x in arr])

    @classmethod
    def anyIn(cls, arr: List[Tile], category: tuple[Tile] | Self) -> bool:
        return any([x in category for x in arr])
