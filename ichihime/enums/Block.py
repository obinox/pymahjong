from enum import IntEnum
from typing import Iterator, List, Self

from ichihime.enums import fuuro as _FU
from ichihime.enums import mentsu as _MT
from ichihime.enums import tile as _TL


class subblock(IntEnum):
    def __new__(cls, value: int, fu: int) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.fu = fu
        return obj

    def __init__(self, value: int, fu: int) -> None:
        self._value_ = value
        self.fu = fu


class block(IntEnum):
    # Manzu shuntsu
    M123S = _MT.SHUNTSU + _TL.MAN1, (_TL.MAN1, _TL.MAN2, _TL.MAN3)
    M234S = _MT.SHUNTSU + _TL.MAN2, (_TL.MAN2, _TL.MAN3, _TL.MAN4)
    M345S = _MT.SHUNTSU + _TL.MAN3, (_TL.MAN3, _TL.MAN4, _TL.MAN5)
    M456S = _MT.SHUNTSU + _TL.MAN4, (_TL.MAN4, _TL.MAN5, _TL.MAN6)
    M567S = _MT.SHUNTSU + _TL.MAN5, (_TL.MAN5, _TL.MAN6, _TL.MAN7)
    M678S = _MT.SHUNTSU + _TL.MAN6, (_TL.MAN6, _TL.MAN7, _TL.MAN8)
    M789S = _MT.SHUNTSU + _TL.MAN7, (_TL.MAN7, _TL.MAN8, _TL.MAN9)
    M340S = _MT.SHUNTSU + _TL.MAN3 + _MT.AKA, (_TL.MAN3, _TL.MAN4, _TL.MAN0)
    M406S = _MT.SHUNTSU + _TL.MAN4 + _MT.AKA, (_TL.MAN4, _TL.MAN0, _TL.MAN6)
    M067S = _MT.SHUNTSU + _TL.MAN5 + _MT.AKA, (_TL.MAN0, _TL.MAN6, _TL.MAN7)
    # Pinzu shuntsu
    P123S = _MT.SHUNTSU + _TL.PIN1, (_TL.PIN1, _TL.PIN2, _TL.PIN3)
    P234S = _MT.SHUNTSU + _TL.PIN2, (_TL.PIN2, _TL.PIN3, _TL.PIN4)
    P345S = _MT.SHUNTSU + _TL.PIN3, (_TL.PIN3, _TL.PIN4, _TL.PIN5)
    P456S = _MT.SHUNTSU + _TL.PIN4, (_TL.PIN4, _TL.PIN5, _TL.PIN6)
    P567S = _MT.SHUNTSU + _TL.PIN5, (_TL.PIN5, _TL.PIN6, _TL.PIN7)
    P678S = _MT.SHUNTSU + _TL.PIN6, (_TL.PIN6, _TL.PIN7, _TL.PIN8)
    P789S = _MT.SHUNTSU + _TL.PIN7, (_TL.PIN7, _TL.PIN8, _TL.PIN9)
    P340S = _MT.SHUNTSU + _TL.PIN3 + _MT.AKA, (_TL.PIN3, _TL.PIN4, _TL.PIN0)
    P406S = _MT.SHUNTSU + _TL.PIN4 + _MT.AKA, (_TL.PIN4, _TL.PIN0, _TL.PIN6)
    P067S = _MT.SHUNTSU + _TL.PIN5 + _MT.AKA, (_TL.PIN0, _TL.PIN6, _TL.PIN7)
    # Souzu shuntsu
    S123S = _MT.SHUNTSU + _TL.SOU1, (_TL.SOU1, _TL.SOU2, _TL.SOU3)
    S234S = _MT.SHUNTSU + _TL.SOU2, (_TL.SOU2, _TL.SOU3, _TL.SOU4)
    S345S = _MT.SHUNTSU + _TL.SOU3, (_TL.SOU3, _TL.SOU4, _TL.SOU5)
    S456S = _MT.SHUNTSU + _TL.SOU4, (_TL.SOU4, _TL.SOU5, _TL.SOU6)
    S567S = _MT.SHUNTSU + _TL.SOU5, (_TL.SOU5, _TL.SOU6, _TL.SOU7)
    S678S = _MT.SHUNTSU + _TL.SOU6, (_TL.SOU6, _TL.SOU7, _TL.SOU8)
    S789S = _MT.SHUNTSU + _TL.SOU7, (_TL.SOU7, _TL.SOU8, _TL.SOU9)
    S340S = _MT.SHUNTSU + _TL.SOU3 + _MT.AKA, (_TL.SOU3, _TL.SOU4, _TL.SOU0)
    S406S = _MT.SHUNTSU + _TL.SOU4 + _MT.AKA, (_TL.SOU4, _TL.SOU0, _TL.SOU6)
    S067S = _MT.SHUNTSU + _TL.SOU5 + _MT.AKA, (_TL.SOU0, _TL.SOU6, _TL.SOU7)

    # Manzu koutsu
    M1KOU = _MT.KOUTSU + _TL.MAN1, (_TL.MAN1, _TL.MAN1, _TL.MAN1)
    M2KOU = _MT.KOUTSU + _TL.MAN2, (_TL.MAN2, _TL.MAN2, _TL.MAN2)
    M3KOU = _MT.KOUTSU + _TL.MAN3, (_TL.MAN3, _TL.MAN3, _TL.MAN3)
    M4KOU = _MT.KOUTSU + _TL.MAN4, (_TL.MAN4, _TL.MAN4, _TL.MAN4)
    M5KOU = _MT.KOUTSU + _TL.MAN5, (_TL.MAN5, _TL.MAN5, _TL.MAN5)
    M0KOU = _MT.KOUTSU + _TL.MAN5 + _MT.AKA, (_TL.MAN5, _TL.MAN5, _TL.MAN0)
    M6KOU = _MT.KOUTSU + _TL.MAN6, (_TL.MAN6, _TL.MAN6, _TL.MAN6)
    M7KOU = _MT.KOUTSU + _TL.MAN7, (_TL.MAN7, _TL.MAN7, _TL.MAN7)
    M8KOU = _MT.KOUTSU + _TL.MAN8, (_TL.MAN8, _TL.MAN8, _TL.MAN8)
    M9KOU = _MT.KOUTSU + _TL.MAN9, (_TL.MAN9, _TL.MAN9, _TL.MAN9)
    # Pinzu koutsu
    P1KOU = _MT.KOUTSU + _TL.PIN1, (_TL.PIN1, _TL.PIN1, _TL.PIN1)
    P2KOU = _MT.KOUTSU + _TL.PIN2, (_TL.PIN2, _TL.PIN2, _TL.PIN2)
    P3KOU = _MT.KOUTSU + _TL.PIN3, (_TL.PIN3, _TL.PIN3, _TL.PIN3)
    P4KOU = _MT.KOUTSU + _TL.PIN4, (_TL.PIN4, _TL.PIN4, _TL.PIN4)
    P5KOU = _MT.KOUTSU + _TL.PIN5, (_TL.PIN5, _TL.PIN5, _TL.PIN5)
    P0KOU = _MT.KOUTSU + _TL.PIN5 + _MT.AKA, (_TL.PIN5, _TL.PIN5, _TL.PIN0)
    P6KOU = _MT.KOUTSU + _TL.PIN6, (_TL.PIN6, _TL.PIN6, _TL.PIN6)
    P7KOU = _MT.KOUTSU + _TL.PIN7, (_TL.PIN7, _TL.PIN7, _TL.PIN7)
    P8KOU = _MT.KOUTSU + _TL.PIN8, (_TL.PIN8, _TL.PIN8, _TL.PIN8)
    P9KOU = _MT.KOUTSU + _TL.PIN9, (_TL.PIN9, _TL.PIN9, _TL.PIN9)
    # Souzu koutsu
    S1KOU = _MT.KOUTSU + _TL.SOU1, (_TL.SOU1, _TL.SOU1, _TL.SOU1)
    S2KOU = _MT.KOUTSU + _TL.SOU2, (_TL.SOU2, _TL.SOU2, _TL.SOU2)
    S3KOU = _MT.KOUTSU + _TL.SOU3, (_TL.SOU3, _TL.SOU3, _TL.SOU3)
    S4KOU = _MT.KOUTSU + _TL.SOU4, (_TL.SOU4, _TL.SOU4, _TL.SOU4)
    S5KOU = _MT.KOUTSU + _TL.SOU5, (_TL.SOU5, _TL.SOU5, _TL.SOU5)
    S0KOU = _MT.KOUTSU + _TL.SOU5 + _MT.AKA, (_TL.SOU5, _TL.SOU5, _TL.SOU0)
    S6KOU = _MT.KOUTSU + _TL.SOU6, (_TL.SOU6, _TL.SOU6, _TL.SOU6)
    S7KOU = _MT.KOUTSU + _TL.SOU7, (_TL.SOU7, _TL.SOU7, _TL.SOU7)
    S8KOU = _MT.KOUTSU + _TL.SOU8, (_TL.SOU8, _TL.SOU8, _TL.SOU8)
    S9KOU = _MT.KOUTSU + _TL.SOU9, (_TL.SOU9, _TL.SOU9, _TL.SOU9)
    # Jihai koutsu
    Z1KOU = _MT.KOUTSU + _TL.TONN, (_TL.TONN, _TL.TONN, _TL.TONN)
    Z2KOU = _MT.KOUTSU + _TL.NANN, (_TL.NANN, _TL.NANN, _TL.NANN)
    Z3KOU = _MT.KOUTSU + _TL.SHAA, (_TL.SHAA, _TL.SHAA, _TL.SHAA)
    Z4KOU = _MT.KOUTSU + _TL.PEII, (_TL.PEII, _TL.PEII, _TL.PEII)
    Z5KOU = _MT.KOUTSU + _TL.HAKU, (_TL.HAKU, _TL.HAKU, _TL.HAKU)
    Z6KOU = _MT.KOUTSU + _TL.HTSU, (_TL.HTSU, _TL.HTSU, _TL.HTSU)
    Z7KOU = _MT.KOUTSU + _TL.CHUN, (_TL.CHUN, _TL.CHUN, _TL.CHUN)

    # Manzu kantsu
    M1KAN = _MT.KANTSU + _TL.MAN1, (_TL.MAN1, _TL.MAN1, _TL.MAN1, _TL.MAN1)
    M2KAN = _MT.KANTSU + _TL.MAN2, (_TL.MAN2, _TL.MAN2, _TL.MAN2, _TL.MAN2)
    M3KAN = _MT.KANTSU + _TL.MAN3, (_TL.MAN3, _TL.MAN3, _TL.MAN3, _TL.MAN3)
    M4KAN = _MT.KANTSU + _TL.MAN4, (_TL.MAN4, _TL.MAN4, _TL.MAN4, _TL.MAN4)
    M5KAN = _MT.KANTSU + _TL.MAN5, (_TL.MAN5, _TL.MAN5, _TL.MAN5, _TL.MAN0)
    M6KAN = _MT.KANTSU + _TL.MAN6, (_TL.MAN6, _TL.MAN6, _TL.MAN6, _TL.MAN6)
    M7KAN = _MT.KANTSU + _TL.MAN7, (_TL.MAN7, _TL.MAN7, _TL.MAN7, _TL.MAN7)
    M8KAN = _MT.KANTSU + _TL.MAN8, (_TL.MAN8, _TL.MAN8, _TL.MAN8, _TL.MAN8)
    M9KAN = _MT.KANTSU + _TL.MAN9, (_TL.MAN9, _TL.MAN9, _TL.MAN9, _TL.MAN9)
    # Pinzu kantsu
    P1KAN = _MT.KANTSU + _TL.PIN1, (_TL.PIN1, _TL.PIN1, _TL.PIN1, _TL.PIN1)
    P2KAN = _MT.KANTSU + _TL.PIN2, (_TL.PIN2, _TL.PIN2, _TL.PIN2, _TL.PIN2)
    P3KAN = _MT.KANTSU + _TL.PIN3, (_TL.PIN3, _TL.PIN3, _TL.PIN3, _TL.PIN3)
    P4KAN = _MT.KANTSU + _TL.PIN4, (_TL.PIN4, _TL.PIN4, _TL.PIN4, _TL.PIN4)
    P5KAN = _MT.KANTSU + _TL.PIN5, (_TL.PIN5, _TL.PIN5, _TL.PIN5, _TL.PIN0)
    P6KAN = _MT.KANTSU + _TL.PIN6, (_TL.PIN6, _TL.PIN6, _TL.PIN6, _TL.PIN6)
    P7KAN = _MT.KANTSU + _TL.PIN7, (_TL.PIN7, _TL.PIN7, _TL.PIN7, _TL.PIN7)
    P8KAN = _MT.KANTSU + _TL.PIN8, (_TL.PIN8, _TL.PIN8, _TL.PIN8, _TL.PIN8)
    P9KAN = _MT.KANTSU + _TL.PIN9, (_TL.PIN9, _TL.PIN9, _TL.PIN9, _TL.PIN9)
    # Souzu kantsu
    S1KAN = _MT.KANTSU + _TL.SOU1, (_TL.SOU1, _TL.SOU1, _TL.SOU1, _TL.SOU1)
    S2KAN = _MT.KANTSU + _TL.SOU2, (_TL.SOU2, _TL.SOU2, _TL.SOU2, _TL.SOU2)
    S3KAN = _MT.KANTSU + _TL.SOU3, (_TL.SOU3, _TL.SOU3, _TL.SOU3, _TL.SOU3)
    S4KAN = _MT.KANTSU + _TL.SOU4, (_TL.SOU4, _TL.SOU4, _TL.SOU4, _TL.SOU4)
    S5KAN = _MT.KANTSU + _TL.SOU5, (_TL.SOU5, _TL.SOU5, _TL.SOU5, _TL.SOU0)
    S6KAN = _MT.KANTSU + _TL.SOU6, (_TL.SOU6, _TL.SOU6, _TL.SOU6, _TL.SOU6)
    S7KAN = _MT.KANTSU + _TL.SOU7, (_TL.SOU7, _TL.SOU7, _TL.SOU7, _TL.SOU7)
    S8KAN = _MT.KANTSU + _TL.SOU8, (_TL.SOU8, _TL.SOU8, _TL.SOU8, _TL.SOU8)
    S9KAN = _MT.KANTSU + _TL.SOU9, (_TL.SOU9, _TL.SOU9, _TL.SOU9, _TL.SOU9)
    # Jihai kantsu
    Z1KAN = _MT.KANTSU + _TL.TONN, (_TL.TONN, _TL.TONN, _TL.TONN, _TL.TONN)
    Z2KAN = _MT.KANTSU + _TL.NANN, (_TL.NANN, _TL.NANN, _TL.NANN, _TL.NANN)
    Z3KAN = _MT.KANTSU + _TL.SHAA, (_TL.SHAA, _TL.SHAA, _TL.SHAA, _TL.SHAA)
    Z4KAN = _MT.KANTSU + _TL.PEII, (_TL.PEII, _TL.PEII, _TL.PEII, _TL.PEII)
    Z5KAN = _MT.KANTSU + _TL.HAKU, (_TL.HAKU, _TL.HAKU, _TL.HAKU, _TL.HAKU)
    Z6KAN = _MT.KANTSU + _TL.HTSU, (_TL.HTSU, _TL.HTSU, _TL.HTSU, _TL.HTSU)
    Z7KAN = _MT.KANTSU + _TL.CHUN, (_TL.CHUN, _TL.CHUN, _TL.CHUN, _TL.CHUN)

    # Manzu toitsu
    M1TOI = _MT.TOITSU + _TL.MAN1, (_TL.MAN1, _TL.MAN1)
    M2TOI = _MT.TOITSU + _TL.MAN2, (_TL.MAN2, _TL.MAN2)
    M3TOI = _MT.TOITSU + _TL.MAN3, (_TL.MAN3, _TL.MAN3)
    M4TOI = _MT.TOITSU + _TL.MAN4, (_TL.MAN4, _TL.MAN4)
    M5TOI = _MT.TOITSU + _TL.MAN5, (_TL.MAN5, _TL.MAN5)
    M6TOI = _MT.TOITSU + _TL.MAN6, (_TL.MAN6, _TL.MAN6)
    M7TOI = _MT.TOITSU + _TL.MAN7, (_TL.MAN7, _TL.MAN7)
    M8TOI = _MT.TOITSU + _TL.MAN8, (_TL.MAN8, _TL.MAN8)
    M9TOI = _MT.TOITSU + _TL.MAN9, (_TL.MAN9, _TL.MAN9)
    M0TOI = _MT.TOITSU + _TL.MAN5 + _MT.AKA, (_TL.MAN5, _TL.MAN0)
    # Pinzu koutsu
    P1TOI = _MT.TOITSU + _TL.PIN1, (_TL.PIN1, _TL.PIN1)
    P2TOI = _MT.TOITSU + _TL.PIN2, (_TL.PIN2, _TL.PIN2)
    P3TOI = _MT.TOITSU + _TL.PIN3, (_TL.PIN3, _TL.PIN3)
    P4TOI = _MT.TOITSU + _TL.PIN4, (_TL.PIN4, _TL.PIN4)
    P5TOI = _MT.TOITSU + _TL.PIN5, (_TL.PIN5, _TL.PIN5)
    P6TOI = _MT.TOITSU + _TL.PIN6, (_TL.PIN6, _TL.PIN6)
    P7TOI = _MT.TOITSU + _TL.PIN7, (_TL.PIN7, _TL.PIN7)
    P8TOI = _MT.TOITSU + _TL.PIN8, (_TL.PIN8, _TL.PIN8)
    P9TOI = _MT.TOITSU + _TL.PIN9, (_TL.PIN9, _TL.PIN9)
    P0TOI = _MT.TOITSU + _TL.PIN5 + _MT.AKA, (_TL.PIN5, _TL.PIN0)
    # Souzu koutsu
    S1TOI = _MT.TOITSU + _TL.SOU1, (_TL.SOU1, _TL.SOU1)
    S2TOI = _MT.TOITSU + _TL.SOU2, (_TL.SOU2, _TL.SOU2)
    S3TOI = _MT.TOITSU + _TL.SOU3, (_TL.SOU3, _TL.SOU3)
    S4TOI = _MT.TOITSU + _TL.SOU4, (_TL.SOU4, _TL.SOU4)
    S5TOI = _MT.TOITSU + _TL.SOU5, (_TL.SOU5, _TL.SOU5)
    S6TOI = _MT.TOITSU + _TL.SOU6, (_TL.SOU6, _TL.SOU6)
    S7TOI = _MT.TOITSU + _TL.SOU7, (_TL.SOU7, _TL.SOU7)
    S8TOI = _MT.TOITSU + _TL.SOU8, (_TL.SOU8, _TL.SOU8)
    S9TOI = _MT.TOITSU + _TL.SOU9, (_TL.SOU9, _TL.SOU9)
    S0TOI = _MT.TOITSU + _TL.SOU5 + _MT.AKA, (_TL.SOU5, _TL.SOU0)
    # Jihai koutsu
    Z1TOI = _MT.TOITSU + _TL.TONN, (_TL.TONN, _TL.TONN)
    Z2TOI = _MT.TOITSU + _TL.NANN, (_TL.NANN, _TL.NANN)
    Z3TOI = _MT.TOITSU + _TL.SHAA, (_TL.SHAA, _TL.SHAA)
    Z4TOI = _MT.TOITSU + _TL.PEII, (_TL.PEII, _TL.PEII)
    Z5TOI = _MT.TOITSU + _TL.HAKU, (_TL.HAKU, _TL.HAKU)
    Z6TOI = _MT.TOITSU + _TL.HTSU, (_TL.HTSU, _TL.HTSU)
    Z7TOI = _MT.TOITSU + _TL.CHUN, (_TL.CHUN, _TL.CHUN)

    # Koukushi tiles
    KKSM1 = _MT.KOKUSHI + _TL.MAN1, (_TL.MAN1,)
    KKSM9 = _MT.KOKUSHI + _TL.MAN9, (_TL.MAN9,)
    KKSP1 = _MT.KOKUSHI + _TL.PIN1, (_TL.PIN1,)
    KKSP9 = _MT.KOKUSHI + _TL.PIN9, (_TL.PIN9,)
    KKSS1 = _MT.KOKUSHI + _TL.SOU1, (_TL.SOU1,)
    KKSS9 = _MT.KOKUSHI + _TL.SOU9, (_TL.SOU9,)
    KKSZ1 = _MT.KOKUSHI + _TL.TONN, (_TL.TONN,)
    KKSZ2 = _MT.KOKUSHI + _TL.NANN, (_TL.NANN,)
    KKSZ3 = _MT.KOKUSHI + _TL.SHAA, (_TL.SHAA,)
    KKSZ4 = _MT.KOKUSHI + _TL.PEII, (_TL.PEII,)
    KKSZ5 = _MT.KOKUSHI + _TL.HAKU, (_TL.HAKU,)
    KKSZ6 = _MT.KOKUSHI + _TL.HTSU, (_TL.HTSU,)
    KKSZ7 = _MT.KOKUSHI + _TL.CHUN, (_TL.CHUN,)

    def __new__(cls, value: int, tiles: List[_TL]) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.tiles = tiles
        return obj

    def __init__(self, value: int, tiles: List[_TL]) -> None:
        self._value_ = value
        self.tiles = tiles

    def __iter__(self) -> Iterator[_TL]:
        for t in self.tiles:
            yield t

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    @staticmethod
    def isShuntsu(b: Self) -> bool:
        return _MT.SHUNTSU < b % _FU.KAMI < _MT.KOUTSU

    @staticmethod
    def isKoutsu(b: Self) -> bool:
        return _MT.KOUTSU < b % _FU.KAMI < _MT.TOITSU

    @staticmethod
    def isToitsu(b: Self) -> bool:
        return _MT.TOITSU < b % _FU.KAMI < _MT.KANTSU

    @staticmethod
    def isKantsu(b: Self) -> bool:
        return _MT.KANTSU < b % _FU.KAMI < _FU.KAMI

    @staticmethod
    def isKokushi(b: Self) -> bool:
        return _MT.KOKUSHI < b

    @staticmethod
    def isAnkou(b: Self) -> bool:
        return block.isKoutsu(b) and b < _FU.KAMI

    @staticmethod
    def isAnkan(b: Self) -> bool:
        return block.isKantsu(b) and b < _FU.KAMI
