from enum import Enum
from typing import Iterator, List, Self, Tuple

from ichihime.enums import group as _GR
from ichihime.enums import tile as _TL


class cat(tuple, Enum):
    """🀫🀫🀫"""

    MANZU = (_TL.MAN1, _TL.MAN2, _TL.MAN3, _TL.MAN4, _TL.MAN5, _TL.MAN6, _TL.MAN7, _TL.MAN8, _TL.MAN9)
    """**Characters** 🀇🀈🀉🀊🀋🀌🀍🀎🀏"""
    PINZU = (_TL.PIN1, _TL.PIN2, _TL.PIN3, _TL.PIN4, _TL.PIN5, _TL.PIN6, _TL.PIN7, _TL.PIN8, _TL.PIN9)
    """**Circles** 🀙🀚🀛🀜🀝🀞🀟🀠🀡"""
    SOUZU = (_TL.SOU1, _TL.SOU2, _TL.SOU3, _TL.SOU4, _TL.SOU5, _TL.SOU6, _TL.SOU7, _TL.SOU8, _TL.SOU9)
    """**Bamboos** 🀐🀑🀒🀓🀔🀕🀖🀗🀘"""
    MANZU0 = (_TL.MAN1, _TL.MAN2, _TL.MAN3, _TL.MAN4, _TL.MAN0, _TL.MAN6, _TL.MAN7, _TL.MAN8, _TL.MAN9)
    PINZU0 = (_TL.PIN1, _TL.PIN2, _TL.PIN3, _TL.PIN4, _TL.PIN0, _TL.PIN6, _TL.PIN7, _TL.PIN8, _TL.PIN9)
    SOUZU0 = (_TL.SOU1, _TL.SOU2, _TL.SOU3, _TL.SOU4, _TL.SOU0, _TL.SOU6, _TL.SOU7, _TL.SOU8, _TL.SOU9)

    MANZUA = (_TL.MAN1, _TL.MAN2, _TL.MAN3, _TL.MAN4, _TL.MAN5, _TL.MAN0, _TL.MAN6, _TL.MAN7, _TL.MAN8, _TL.MAN9)
    PINZUA = (_TL.PIN1, _TL.PIN2, _TL.PIN3, _TL.PIN4, _TL.PIN5, _TL.PIN0, _TL.PIN6, _TL.PIN7, _TL.PIN8, _TL.PIN9)
    SOUZUA = (_TL.SOU1, _TL.SOU2, _TL.SOU3, _TL.SOU4, _TL.SOU5, _TL.SOU0, _TL.SOU6, _TL.SOU7, _TL.SOU8, _TL.SOU9)

    AKAPAI = (_TL.MAN0, _TL.PIN0, _TL.SOU0)

    """**Reds** 🀋 🀝 🀔"""
    KAZEHAI = (_TL.TONN, _TL.NANN, _TL.SHAA, _TL.PEII)
    """**Winds** 🀀🀁🀂🀃"""
    SANGENPAI = (_TL.HAKU, _TL.HTSU, _TL.CHUN)
    """**Dragons** 🀆🀅🀄"""

    SHUUPAI = (*MANZU, *PINZU, *SOUZU)
    SHUUPAI0 = (*MANZU0, *PINZU0, *SOUZU0)
    SHUUPAIA = (*MANZU, *PINZU, *SOUZU, *AKAPAI)
    """**Numbers** 🀇🀈🀉🀊🀋🀌🀍🀎🀏 🀙🀚🀛🀜🀝🀞🀟🀠🀡 🀐🀑🀒🀓🀔🀕🀖🀗🀘"""

    MANZUCHUNCHAN = (_TL.MAN2, _TL.MAN3, _TL.MAN4, _TL.MAN5, _TL.MAN6, _TL.MAN7, _TL.MAN8, _TL.MAN0)
    PINZUCHUNCHAN = (_TL.PIN2, _TL.PIN3, _TL.PIN4, _TL.PIN5, _TL.PIN6, _TL.PIN7, _TL.PIN8, _TL.PIN0)
    SOUZUCHUNCHAN = (_TL.SOU2, _TL.SOU3, _TL.SOU4, _TL.SOU5, _TL.SOU6, _TL.SOU7, _TL.SOU8, _TL.SOU0)
    CHUNCHANHAI = (*MANZUCHUNCHAN, *PINZUCHUNCHAN, *SOUZUCHUNCHAN)
    """**Simples** 🀈🀉🀊🀋🀌🀍🀎 🀚🀛🀜🀝🀞🀟🀠 🀑🀒🀓🀔🀕🀖🀗"""

    JIHAI = (*KAZEHAI, *SANGENPAI)
    """**Words** 🀀🀁🀂🀃 🀆🀅🀄"""
    ROUTOUHAI = (_TL.MAN1, _TL.MAN9, _TL.PIN1, _TL.PIN9, _TL.SOU1, _TL.SOU9)
    """**Ends** 🀇🀏 🀙🀡 🀐🀘"""

    YAOCHUUHAI = (*ROUTOUHAI, *JIHAI)
    """**Terminals** 🀇🀏 🀙🀡 🀐🀘 🀀🀁🀂🀃 🀆🀅🀄"""

    MIDORIPAI = (_TL.SOU2, _TL.SOU3, _TL.SOU4, _TL.SOU6, _TL.SOU8, _TL.HTSU)
    """**Greens** 🀑🀒🀓🀕🀗 🀅"""
    KUROPAI = (_TL.PIN2, _TL.PIN4, _TL.PIN8, *KAZEHAI)
    """**Blacks** 🀚🀜🀠 🀀🀁🀂🀃"""
    JAKUPAI = (_TL.SOU1, _TL.SOU5, _TL.SOU0, _TL.SOU7, _TL.SOU9, _TL.CHUN)
    """**Peacocks** 🀐🀔🀖🀘 🀄"""

    def __new__(cls, value: Tuple[_TL]) -> Self:
        obj = tuple.__new__(cls, value)
        obj._value_ = value
        return obj

    @staticmethod
    def allIn(arr: Iterator[_TL], category: Tuple[_TL] | Self) -> bool:
        return all(map(lambda x: x in category, arr))

    @staticmethod
    def anyIn(arr: Iterator[_TL], category: Tuple[_TL] | Self) -> bool:
        return any(map(lambda x: x in category, arr))

    @staticmethod
    def getCat(tile: _TL) -> Self:
        match tile.group:
            case _GR.MAN:
                return cat.MANZU, cat.MANZU0, cat.MANZUA
            case _GR.PIN:
                return cat.PINZU, cat.PINZU0, cat.PINZUA
            case _GR.SOU:
                return cat.SOUZU, cat.SOUZU0, cat.SOUZUA
            case _GR.KZE:
                return cat.KAZEHAI, cat.KAZEHAI, cat.JIHAI
            case _GR.SGN:
                return cat.SANGENPAI, cat.SANGENPAI, cat.JIHAI
