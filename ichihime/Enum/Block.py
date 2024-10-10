from collections.abc import Iterator
from enum import IntEnum
from typing import List, Self

from ichihime.Enum.Mentsu import Mentsu
from ichihime.Enum.Tile import Tile


class SubBlock(IntEnum):
    def __new__(cls, value: int, fu: int) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.fu = fu
        return obj

    def __init__(self, value: int, fu: int) -> None:
        self._value_ = value
        self.fu = fu


class Block(IntEnum):
    # Manzu shuntsu
    M123S = Mentsu.SHUNTSH + Tile.MAN1, (Tile.MAN1, Tile.MAN2, Tile.MAN3)
    M234S = Mentsu.SHUNTSH + Tile.MAN2, (Tile.MAN2, Tile.MAN3, Tile.MAN4)
    M345S = Mentsu.SHUNTSH + Tile.MAN3, (Tile.MAN3, Tile.MAN4, Tile.MAN5)
    M456S = Mentsu.SHUNTSH + Tile.MAN4, (Tile.MAN4, Tile.MAN5, Tile.MAN6)
    M567S = Mentsu.SHUNTSH + Tile.MAN5, (Tile.MAN5, Tile.MAN6, Tile.MAN7)
    M678S = Mentsu.SHUNTSH + Tile.MAN6, (Tile.MAN6, Tile.MAN7, Tile.MAN8)
    M789S = Mentsu.SHUNTSH + Tile.MAN7, (Tile.MAN7, Tile.MAN8, Tile.MAN9)
    M340S = Mentsu.SHUNTSH + Tile.MAN3 + Mentsu.AKA, (Tile.MAN3, Tile.MAN4, Tile.MAN0)
    M406S = Mentsu.SHUNTSH + Tile.MAN4 + Mentsu.AKA, (Tile.MAN4, Tile.MAN0, Tile.MAN6)
    M067S = Mentsu.SHUNTSH + Tile.MAN5 + Mentsu.AKA, (Tile.MAN0, Tile.MAN6, Tile.MAN7)
    # Pinzu shuntsu
    P123S = Mentsu.SHUNTSH + Tile.PIN1, (Tile.PIN1, Tile.PIN2, Tile.PIN3)
    P234S = Mentsu.SHUNTSH + Tile.PIN2, (Tile.PIN2, Tile.PIN3, Tile.PIN4)
    P345S = Mentsu.SHUNTSH + Tile.PIN3, (Tile.PIN3, Tile.PIN4, Tile.PIN5)
    P456S = Mentsu.SHUNTSH + Tile.PIN4, (Tile.PIN4, Tile.PIN5, Tile.PIN6)
    P567S = Mentsu.SHUNTSH + Tile.PIN5, (Tile.PIN5, Tile.PIN6, Tile.PIN7)
    P678S = Mentsu.SHUNTSH + Tile.PIN6, (Tile.PIN6, Tile.PIN7, Tile.PIN8)
    P789S = Mentsu.SHUNTSH + Tile.PIN7, (Tile.PIN7, Tile.PIN8, Tile.PIN9)
    P340S = Mentsu.SHUNTSH + Tile.PIN3 + Mentsu.AKA, (Tile.PIN3, Tile.PIN4, Tile.PIN0)
    P406S = Mentsu.SHUNTSH + Tile.PIN4 + Mentsu.AKA, (Tile.PIN4, Tile.PIN0, Tile.PIN6)
    P067S = Mentsu.SHUNTSH + Tile.PIN5 + Mentsu.AKA, (Tile.PIN0, Tile.PIN6, Tile.PIN7)
    # Souzu shuntsu
    S123S = Mentsu.SHUNTSH + Tile.SOU1, (Tile.SOU1, Tile.SOU2, Tile.SOU3)
    S234S = Mentsu.SHUNTSH + Tile.SOU2, (Tile.SOU2, Tile.SOU3, Tile.SOU4)
    S345S = Mentsu.SHUNTSH + Tile.SOU3, (Tile.SOU3, Tile.SOU4, Tile.SOU5)
    S456S = Mentsu.SHUNTSH + Tile.SOU4, (Tile.SOU4, Tile.SOU5, Tile.SOU6)
    S567S = Mentsu.SHUNTSH + Tile.SOU5, (Tile.SOU5, Tile.SOU6, Tile.SOU7)
    S678S = Mentsu.SHUNTSH + Tile.SOU6, (Tile.SOU6, Tile.SOU7, Tile.SOU8)
    S789S = Mentsu.SHUNTSH + Tile.SOU7, (Tile.SOU7, Tile.SOU8, Tile.SOU9)
    S340S = Mentsu.SHUNTSH + Tile.SOU3 + Mentsu.AKA, (Tile.SOU3, Tile.SOU4, Tile.SOU0)
    S406S = Mentsu.SHUNTSH + Tile.SOU4 + Mentsu.AKA, (Tile.SOU4, Tile.SOU0, Tile.SOU6)
    S067S = Mentsu.SHUNTSH + Tile.SOU5 + Mentsu.AKA, (Tile.SOU0, Tile.SOU6, Tile.SOU7)

    # Manzu koutsu
    M1KOU = Mentsu.KOUTSU + Tile.MAN1, (Tile.MAN1, Tile.MAN1, Tile.MAN1)
    M2KOU = Mentsu.KOUTSU + Tile.MAN2, (Tile.MAN2, Tile.MAN2, Tile.MAN2)
    M3KOU = Mentsu.KOUTSU + Tile.MAN3, (Tile.MAN3, Tile.MAN3, Tile.MAN3)
    M4KOU = Mentsu.KOUTSU + Tile.MAN4, (Tile.MAN4, Tile.MAN4, Tile.MAN4)
    M5KOU = Mentsu.KOUTSU + Tile.MAN5, (Tile.MAN5, Tile.MAN5, Tile.MAN5)
    M6KOU = Mentsu.KOUTSU + Tile.MAN6, (Tile.MAN6, Tile.MAN6, Tile.MAN6)
    M7KOU = Mentsu.KOUTSU + Tile.MAN7, (Tile.MAN7, Tile.MAN7, Tile.MAN7)
    M8KOU = Mentsu.KOUTSU + Tile.MAN8, (Tile.MAN8, Tile.MAN8, Tile.MAN8)
    M9KOU = Mentsu.KOUTSU + Tile.MAN9, (Tile.MAN9, Tile.MAN9, Tile.MAN9)
    M0KOU = Mentsu.KOUTSU + Tile.MAN5 + Mentsu.AKA, (Tile.MAN5, Tile.MAN5, Tile.MAN0)
    # Pinzu koutsu
    P1KOU = Mentsu.KOUTSU + Tile.PIN1, (Tile.PIN1, Tile.PIN1, Tile.PIN1)
    P2KOU = Mentsu.KOUTSU + Tile.PIN2, (Tile.PIN2, Tile.PIN2, Tile.PIN2)
    P3KOU = Mentsu.KOUTSU + Tile.PIN3, (Tile.PIN3, Tile.PIN3, Tile.PIN3)
    P4KOU = Mentsu.KOUTSU + Tile.PIN4, (Tile.PIN4, Tile.PIN4, Tile.PIN4)
    P5KOU = Mentsu.KOUTSU + Tile.PIN5, (Tile.PIN5, Tile.PIN5, Tile.PIN5)
    P6KOU = Mentsu.KOUTSU + Tile.PIN6, (Tile.PIN6, Tile.PIN6, Tile.PIN6)
    P7KOU = Mentsu.KOUTSU + Tile.PIN7, (Tile.PIN7, Tile.PIN7, Tile.PIN7)
    P8KOU = Mentsu.KOUTSU + Tile.PIN8, (Tile.PIN8, Tile.PIN8, Tile.PIN8)
    P9KOU = Mentsu.KOUTSU + Tile.PIN9, (Tile.PIN9, Tile.PIN9, Tile.PIN9)
    P0KOU = Mentsu.KOUTSU + Tile.PIN5 + Mentsu.AKA, (Tile.PIN5, Tile.PIN5, Tile.PIN0)
    # Souzu koutsu
    S1KOU = Mentsu.KOUTSU + Tile.SOU1, (Tile.SOU1, Tile.SOU1, Tile.SOU1)
    S2KOU = Mentsu.KOUTSU + Tile.SOU2, (Tile.SOU2, Tile.SOU2, Tile.SOU2)
    S3KOU = Mentsu.KOUTSU + Tile.SOU3, (Tile.SOU3, Tile.SOU3, Tile.SOU3)
    S4KOU = Mentsu.KOUTSU + Tile.SOU4, (Tile.SOU4, Tile.SOU4, Tile.SOU4)
    S5KOU = Mentsu.KOUTSU + Tile.SOU5, (Tile.SOU5, Tile.SOU5, Tile.SOU5)
    S6KOU = Mentsu.KOUTSU + Tile.SOU6, (Tile.SOU6, Tile.SOU6, Tile.SOU6)
    S7KOU = Mentsu.KOUTSU + Tile.SOU7, (Tile.SOU7, Tile.SOU7, Tile.SOU7)
    S8KOU = Mentsu.KOUTSU + Tile.SOU8, (Tile.SOU8, Tile.SOU8, Tile.SOU8)
    S9KOU = Mentsu.KOUTSU + Tile.SOU9, (Tile.SOU9, Tile.SOU9, Tile.SOU9)
    S0KOU = Mentsu.KOUTSU + Tile.SOU5 + Mentsu.AKA, (Tile.SOU5, Tile.SOU5, Tile.SOU0)
    # Jihai koutsu
    Z1KOU = Mentsu.KOUTSU + Tile.TONN, (Tile.TONN, Tile.TONN, Tile.TONN)
    Z2KOU = Mentsu.KOUTSU + Tile.NANN, (Tile.NANN, Tile.NANN, Tile.NANN)
    Z3KOU = Mentsu.KOUTSU + Tile.SHAA, (Tile.SHAA, Tile.SHAA, Tile.SHAA)
    Z4KOU = Mentsu.KOUTSU + Tile.PEII, (Tile.PEII, Tile.PEII, Tile.PEII)
    Z5KOU = Mentsu.KOUTSU + Tile.HAKU, (Tile.HAKU, Tile.HAKU, Tile.HAKU)
    Z6KOU = Mentsu.KOUTSU + Tile.HATS, (Tile.HATS, Tile.HATS, Tile.HATS)
    Z7KOU = Mentsu.KOUTSU + Tile.CHUN, (Tile.CHUN, Tile.CHUN, Tile.CHUN)

    # Manzu kantsu
    M1KAN = Mentsu.KANTSU + Tile.MAN1, (Tile.MAN1, Tile.MAN1, Tile.MAN1, Tile.MAN1)
    M2KAN = Mentsu.KANTSU + Tile.MAN2, (Tile.MAN2, Tile.MAN2, Tile.MAN2, Tile.MAN2)
    M3KAN = Mentsu.KANTSU + Tile.MAN3, (Tile.MAN3, Tile.MAN3, Tile.MAN3, Tile.MAN3)
    M4KAN = Mentsu.KANTSU + Tile.MAN4, (Tile.MAN4, Tile.MAN4, Tile.MAN4, Tile.MAN4)
    M5KAN = Mentsu.KANTSU + Tile.MAN5, (Tile.MAN5, Tile.MAN5, Tile.MAN5, Tile.MAN0)
    M6KAN = Mentsu.KANTSU + Tile.MAN6, (Tile.MAN6, Tile.MAN6, Tile.MAN6, Tile.MAN6)
    M7KAN = Mentsu.KANTSU + Tile.MAN7, (Tile.MAN7, Tile.MAN7, Tile.MAN7, Tile.MAN7)
    M8KAN = Mentsu.KANTSU + Tile.MAN8, (Tile.MAN8, Tile.MAN8, Tile.MAN8, Tile.MAN8)
    M9KAN = Mentsu.KANTSU + Tile.MAN9, (Tile.MAN9, Tile.MAN9, Tile.MAN9, Tile.MAN9)
    # Pinzu kantsu
    P1KAN = Mentsu.KANTSU + Tile.PIN1, (Tile.PIN1, Tile.PIN1, Tile.PIN1, Tile.PIN1)
    P2KAN = Mentsu.KANTSU + Tile.PIN2, (Tile.PIN2, Tile.PIN2, Tile.PIN2, Tile.PIN2)
    P3KAN = Mentsu.KANTSU + Tile.PIN3, (Tile.PIN3, Tile.PIN3, Tile.PIN3, Tile.PIN3)
    P4KAN = Mentsu.KANTSU + Tile.PIN4, (Tile.PIN4, Tile.PIN4, Tile.PIN4, Tile.PIN4)
    P5KAN = Mentsu.KANTSU + Tile.PIN5, (Tile.PIN5, Tile.PIN5, Tile.PIN5, Tile.PIN0)
    P6KAN = Mentsu.KANTSU + Tile.PIN6, (Tile.PIN6, Tile.PIN6, Tile.PIN6, Tile.PIN6)
    P7KAN = Mentsu.KANTSU + Tile.PIN7, (Tile.PIN7, Tile.PIN7, Tile.PIN7, Tile.PIN7)
    P8KAN = Mentsu.KANTSU + Tile.PIN8, (Tile.PIN8, Tile.PIN8, Tile.PIN8, Tile.PIN8)
    P9KAN = Mentsu.KANTSU + Tile.PIN9, (Tile.PIN9, Tile.PIN9, Tile.PIN9, Tile.PIN9)
    # Souzu kantsu
    S1KAN = Mentsu.KANTSU + Tile.SOU1, (Tile.SOU1, Tile.SOU1, Tile.SOU1, Tile.SOU1)
    S2KAN = Mentsu.KANTSU + Tile.SOU2, (Tile.SOU2, Tile.SOU2, Tile.SOU2, Tile.SOU2)
    S3KAN = Mentsu.KANTSU + Tile.SOU3, (Tile.SOU3, Tile.SOU3, Tile.SOU3, Tile.SOU3)
    S4KAN = Mentsu.KANTSU + Tile.SOU4, (Tile.SOU4, Tile.SOU4, Tile.SOU4, Tile.SOU4)
    S5KAN = Mentsu.KANTSU + Tile.SOU5, (Tile.SOU5, Tile.SOU5, Tile.SOU5, Tile.SOU0)
    S6KAN = Mentsu.KANTSU + Tile.SOU6, (Tile.SOU6, Tile.SOU6, Tile.SOU6, Tile.SOU6)
    S7KAN = Mentsu.KANTSU + Tile.SOU7, (Tile.SOU7, Tile.SOU7, Tile.SOU7, Tile.SOU7)
    S8KAN = Mentsu.KANTSU + Tile.SOU8, (Tile.SOU8, Tile.SOU8, Tile.SOU8, Tile.SOU8)
    S9KAN = Mentsu.KANTSU + Tile.SOU9, (Tile.SOU9, Tile.SOU9, Tile.SOU9, Tile.SOU9)
    # Jihai kantsu
    Z1KAN = Mentsu.KANTSU + Tile.TONN, (Tile.TONN, Tile.TONN, Tile.TONN, Tile.TONN)
    Z2KAN = Mentsu.KANTSU + Tile.NANN, (Tile.NANN, Tile.NANN, Tile.NANN, Tile.NANN)
    Z3KAN = Mentsu.KANTSU + Tile.SHAA, (Tile.SHAA, Tile.SHAA, Tile.SHAA, Tile.SHAA)
    Z4KAN = Mentsu.KANTSU + Tile.PEII, (Tile.PEII, Tile.PEII, Tile.PEII, Tile.PEII)
    Z5KAN = Mentsu.KANTSU + Tile.HAKU, (Tile.HAKU, Tile.HAKU, Tile.HAKU, Tile.HAKU)
    Z6KAN = Mentsu.KANTSU + Tile.HATS, (Tile.HATS, Tile.HATS, Tile.HATS, Tile.HATS)
    Z7KAN = Mentsu.KANTSU + Tile.CHUN, (Tile.CHUN, Tile.CHUN, Tile.CHUN, Tile.CHUN)

    # Manzu toitsu
    M1TOI = Mentsu.TOITSU + Tile.MAN1, (Tile.MAN1, Tile.MAN1)
    M2TOI = Mentsu.TOITSU + Tile.MAN2, (Tile.MAN2, Tile.MAN2)
    M3TOI = Mentsu.TOITSU + Tile.MAN3, (Tile.MAN3, Tile.MAN3)
    M4TOI = Mentsu.TOITSU + Tile.MAN4, (Tile.MAN4, Tile.MAN4)
    M5TOI = Mentsu.TOITSU + Tile.MAN5, (Tile.MAN5, Tile.MAN5)
    M6TOI = Mentsu.TOITSU + Tile.MAN6, (Tile.MAN6, Tile.MAN6)
    M7TOI = Mentsu.TOITSU + Tile.MAN7, (Tile.MAN7, Tile.MAN7)
    M8TOI = Mentsu.TOITSU + Tile.MAN8, (Tile.MAN8, Tile.MAN8)
    M9TOI = Mentsu.TOITSU + Tile.MAN9, (Tile.MAN9, Tile.MAN9)
    M0TOI = Mentsu.TOITSU + Tile.MAN5 + Mentsu.AKA, (Tile.MAN5, Tile.MAN0)
    # Pinzu koutsu
    P1TOI = Mentsu.TOITSU + Tile.PIN1, (Tile.PIN1, Tile.PIN1)
    P2TOI = Mentsu.TOITSU + Tile.PIN2, (Tile.PIN2, Tile.PIN2)
    P3TOI = Mentsu.TOITSU + Tile.PIN3, (Tile.PIN3, Tile.PIN3)
    P4TOI = Mentsu.TOITSU + Tile.PIN4, (Tile.PIN4, Tile.PIN4)
    P5TOI = Mentsu.TOITSU + Tile.PIN5, (Tile.PIN5, Tile.PIN5)
    P6TOI = Mentsu.TOITSU + Tile.PIN6, (Tile.PIN6, Tile.PIN6)
    P7TOI = Mentsu.TOITSU + Tile.PIN7, (Tile.PIN7, Tile.PIN7)
    P8TOI = Mentsu.TOITSU + Tile.PIN8, (Tile.PIN8, Tile.PIN8)
    P9TOI = Mentsu.TOITSU + Tile.PIN9, (Tile.PIN9, Tile.PIN9)
    P0TOI = Mentsu.TOITSU + Tile.PIN5 + Mentsu.AKA, (Tile.PIN5, Tile.PIN0)
    # Souzu koutsu
    S1TOI = Mentsu.TOITSU + Tile.SOU1, (Tile.SOU1, Tile.SOU1)
    S2TOI = Mentsu.TOITSU + Tile.SOU2, (Tile.SOU2, Tile.SOU2)
    S3TOI = Mentsu.TOITSU + Tile.SOU3, (Tile.SOU3, Tile.SOU3)
    S4TOI = Mentsu.TOITSU + Tile.SOU4, (Tile.SOU4, Tile.SOU4)
    S5TOI = Mentsu.TOITSU + Tile.SOU5, (Tile.SOU5, Tile.SOU5)
    S6TOI = Mentsu.TOITSU + Tile.SOU6, (Tile.SOU6, Tile.SOU6)
    S7TOI = Mentsu.TOITSU + Tile.SOU7, (Tile.SOU7, Tile.SOU7)
    S8TOI = Mentsu.TOITSU + Tile.SOU8, (Tile.SOU8, Tile.SOU8)
    S9TOI = Mentsu.TOITSU + Tile.SOU9, (Tile.SOU9, Tile.SOU9)
    S0TOI = Mentsu.TOITSU + Tile.SOU5 + Mentsu.AKA, (Tile.SOU5, Tile.SOU0)
    # Jihai koutsu
    Z1TOI = Mentsu.TOITSU + Tile.TONN, (Tile.TONN, Tile.TONN)
    Z2TOI = Mentsu.TOITSU + Tile.NANN, (Tile.NANN, Tile.NANN)
    Z3TOI = Mentsu.TOITSU + Tile.SHAA, (Tile.SHAA, Tile.SHAA)
    Z4TOI = Mentsu.TOITSU + Tile.PEII, (Tile.PEII, Tile.PEII)
    Z5TOI = Mentsu.TOITSU + Tile.HAKU, (Tile.HAKU, Tile.HAKU)
    Z6TOI = Mentsu.TOITSU + Tile.HATS, (Tile.HATS, Tile.HATS)
    Z7TOI = Mentsu.TOITSU + Tile.CHUN, (Tile.CHUN, Tile.CHUN)

    # Koukushi tiles
    KKSM1 = Mentsu.KOKUSHI + Tile.MAN1, (Tile.MAN1,)
    KKSM9 = Mentsu.KOKUSHI + Tile.MAN9, (Tile.MAN9,)
    KKSP1 = Mentsu.KOKUSHI + Tile.PIN1, (Tile.PIN1,)
    KKSP9 = Mentsu.KOKUSHI + Tile.PIN9, (Tile.PIN9,)
    KKSS1 = Mentsu.KOKUSHI + Tile.SOU1, (Tile.SOU1,)
    KKSS9 = Mentsu.KOKUSHI + Tile.SOU9, (Tile.SOU9,)
    KKSZ1 = Mentsu.KOKUSHI + Tile.TONN, (Tile.TONN,)
    KKSZ2 = Mentsu.KOKUSHI + Tile.NANN, (Tile.NANN,)
    KKSZ3 = Mentsu.KOKUSHI + Tile.SHAA, (Tile.SHAA,)
    KKSZ4 = Mentsu.KOKUSHI + Tile.PEII, (Tile.PEII,)
    KKSZ5 = Mentsu.KOKUSHI + Tile.HAKU, (Tile.HAKU,)
    KKSZ6 = Mentsu.KOKUSHI + Tile.HATS, (Tile.HATS,)
    KKSZ7 = Mentsu.KOKUSHI + Tile.CHUN, (Tile.CHUN,)

    def __new__(cls, value: int, tiles: List[Tile]) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.tiles = tiles
        return obj

    def __init__(self, value: int, tiles: List[Tile]) -> None:
        self._value_ = value
        self.tiles = tiles

    def __iter__(self) -> Iterator[Tile]:
        for t in self.tiles:
            yield t

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
