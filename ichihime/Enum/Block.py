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
    MAN123 = Mentsu.SHUNTSH + Tile.MAN1, (Tile.MAN1, Tile.MAN2, Tile.MAN3)
    MAN234 = Mentsu.SHUNTSH + Tile.MAN2, (Tile.MAN2, Tile.MAN3, Tile.MAN4)
    MAN345 = Mentsu.SHUNTSH + Tile.MAN3, (Tile.MAN3, Tile.MAN4, Tile.MAN5)
    MAN456 = Mentsu.SHUNTSH + Tile.MAN4, (Tile.MAN4, Tile.MAN5, Tile.MAN6)
    MAN567 = Mentsu.SHUNTSH + Tile.MAN5, (Tile.MAN5, Tile.MAN6, Tile.MAN7)
    MAN678 = Mentsu.SHUNTSH + Tile.MAN6, (Tile.MAN6, Tile.MAN7, Tile.MAN8)
    MAN789 = Mentsu.SHUNTSH + Tile.MAN7, (Tile.MAN7, Tile.MAN8, Tile.MAN9)
    MAN340 = Mentsu.SHUNTSH + Tile.MAN3 + Mentsu.AKA, (Tile.MAN3, Tile.MAN4, Tile.MAN0)
    MAN406 = Mentsu.SHUNTSH + Tile.MAN4 + Mentsu.AKA, (Tile.MAN4, Tile.MAN0, Tile.MAN6)
    MAN067 = Mentsu.SHUNTSH + Tile.MAN5 + Mentsu.AKA, (Tile.MAN0, Tile.MAN6, Tile.MAN7)
    # Pinzu shuntsu
    PIN123 = Mentsu.SHUNTSH + Tile.PIN1, (Tile.PIN1, Tile.PIN2, Tile.PIN3)
    PIN234 = Mentsu.SHUNTSH + Tile.PIN2, (Tile.PIN2, Tile.PIN3, Tile.PIN4)
    PIN345 = Mentsu.SHUNTSH + Tile.PIN3, (Tile.PIN3, Tile.PIN4, Tile.PIN5)
    PIN456 = Mentsu.SHUNTSH + Tile.PIN4, (Tile.PIN4, Tile.PIN5, Tile.PIN6)
    PIN567 = Mentsu.SHUNTSH + Tile.PIN5, (Tile.PIN5, Tile.PIN6, Tile.PIN7)
    PIN678 = Mentsu.SHUNTSH + Tile.PIN6, (Tile.PIN6, Tile.PIN7, Tile.PIN8)
    PIN789 = Mentsu.SHUNTSH + Tile.PIN7, (Tile.PIN7, Tile.PIN8, Tile.PIN9)
    PIN340 = Mentsu.SHUNTSH + Tile.PIN3 + Mentsu.AKA, (Tile.PIN3, Tile.PIN4, Tile.PIN0)
    PIN406 = Mentsu.SHUNTSH + Tile.PIN4 + Mentsu.AKA, (Tile.PIN4, Tile.PIN0, Tile.PIN6)
    PIN067 = Mentsu.SHUNTSH + Tile.PIN5 + Mentsu.AKA, (Tile.PIN0, Tile.PIN6, Tile.PIN7)
    # Souzu shuntsu
    SOU123 = Mentsu.SHUNTSH + Tile.SOU1, (Tile.SOU1, Tile.SOU2, Tile.SOU3)
    SOU234 = Mentsu.SHUNTSH + Tile.SOU2, (Tile.SOU2, Tile.SOU3, Tile.SOU4)
    SOU345 = Mentsu.SHUNTSH + Tile.SOU3, (Tile.SOU3, Tile.SOU4, Tile.SOU5)
    SOU456 = Mentsu.SHUNTSH + Tile.SOU4, (Tile.SOU4, Tile.SOU5, Tile.SOU6)
    SOU567 = Mentsu.SHUNTSH + Tile.SOU5, (Tile.SOU5, Tile.SOU6, Tile.SOU7)
    SOU678 = Mentsu.SHUNTSH + Tile.SOU6, (Tile.SOU6, Tile.SOU7, Tile.SOU8)
    SOU789 = Mentsu.SHUNTSH + Tile.SOU7, (Tile.SOU7, Tile.SOU8, Tile.SOU9)
    SOU340 = Mentsu.SHUNTSH + Tile.SOU3 + Mentsu.AKA, (Tile.SOU3, Tile.SOU4, Tile.SOU0)
    SOU406 = Mentsu.SHUNTSH + Tile.SOU4 + Mentsu.AKA, (Tile.SOU4, Tile.SOU0, Tile.SOU6)
    SOU067 = Mentsu.SHUNTSH + Tile.SOU5 + Mentsu.AKA, (Tile.SOU0, Tile.SOU6, Tile.SOU7)

    # Manzu koutsu
    MAN111 = Mentsu.KOUTSU + Tile.MAN1, (Tile.MAN1, Tile.MAN1, Tile.MAN1)
    MAN222 = Mentsu.KOUTSU + Tile.MAN2, (Tile.MAN2, Tile.MAN2, Tile.MAN2)
    MAN333 = Mentsu.KOUTSU + Tile.MAN3, (Tile.MAN3, Tile.MAN3, Tile.MAN3)
    MAN444 = Mentsu.KOUTSU + Tile.MAN4, (Tile.MAN4, Tile.MAN4, Tile.MAN4)
    MAN555 = Mentsu.KOUTSU + Tile.MAN5, (Tile.MAN5, Tile.MAN5, Tile.MAN5)
    MAN666 = Mentsu.KOUTSU + Tile.MAN6, (Tile.MAN6, Tile.MAN6, Tile.MAN6)
    MAN777 = Mentsu.KOUTSU + Tile.MAN7, (Tile.MAN7, Tile.MAN7, Tile.MAN7)
    MAN888 = Mentsu.KOUTSU + Tile.MAN8, (Tile.MAN8, Tile.MAN8, Tile.MAN8)
    MAN999 = Mentsu.KOUTSU + Tile.MAN9, (Tile.MAN9, Tile.MAN9, Tile.MAN9)
    MAN550 = Mentsu.KOUTSU + Tile.MAN5 + Mentsu.AKA, (Tile.MAN5, Tile.MAN5, Tile.MAN0)
    # Pinzu koutsu
    PIN111 = Mentsu.KOUTSU + Tile.PIN1, (Tile.PIN1, Tile.PIN1, Tile.PIN1)
    PIN222 = Mentsu.KOUTSU + Tile.PIN2, (Tile.PIN2, Tile.PIN2, Tile.PIN2)
    PIN333 = Mentsu.KOUTSU + Tile.PIN3, (Tile.PIN3, Tile.PIN3, Tile.PIN3)
    PIN444 = Mentsu.KOUTSU + Tile.PIN4, (Tile.PIN4, Tile.PIN4, Tile.PIN4)
    PIN555 = Mentsu.KOUTSU + Tile.PIN5, (Tile.PIN5, Tile.PIN5, Tile.PIN5)
    PIN666 = Mentsu.KOUTSU + Tile.PIN6, (Tile.PIN6, Tile.PIN6, Tile.PIN6)
    PIN777 = Mentsu.KOUTSU + Tile.PIN7, (Tile.PIN7, Tile.PIN7, Tile.PIN7)
    PIN888 = Mentsu.KOUTSU + Tile.PIN8, (Tile.PIN8, Tile.PIN8, Tile.PIN8)
    PIN999 = Mentsu.KOUTSU + Tile.PIN9, (Tile.PIN9, Tile.PIN9, Tile.PIN9)
    PIN550 = Mentsu.KOUTSU + Tile.PIN5 + Mentsu.AKA, (Tile.PIN5, Tile.PIN5, Tile.PIN0)
    # Souzu koutsu
    SOU111 = Mentsu.KOUTSU + Tile.SOU1, (Tile.SOU1, Tile.SOU1, Tile.SOU1)
    SOU222 = Mentsu.KOUTSU + Tile.SOU2, (Tile.SOU2, Tile.SOU2, Tile.SOU2)
    SOU333 = Mentsu.KOUTSU + Tile.SOU3, (Tile.SOU3, Tile.SOU3, Tile.SOU3)
    SOU444 = Mentsu.KOUTSU + Tile.SOU4, (Tile.SOU4, Tile.SOU4, Tile.SOU4)
    SOU555 = Mentsu.KOUTSU + Tile.SOU5, (Tile.SOU5, Tile.SOU5, Tile.SOU5)
    SOU666 = Mentsu.KOUTSU + Tile.SOU6, (Tile.SOU6, Tile.SOU6, Tile.SOU6)
    SOU777 = Mentsu.KOUTSU + Tile.SOU7, (Tile.SOU7, Tile.SOU7, Tile.SOU7)
    SOU888 = Mentsu.KOUTSU + Tile.SOU8, (Tile.SOU8, Tile.SOU8, Tile.SOU8)
    SOU999 = Mentsu.KOUTSU + Tile.SOU9, (Tile.SOU9, Tile.SOU9, Tile.SOU9)
    SOU550 = Mentsu.KOUTSU + Tile.SOU5 + Mentsu.AKA, (Tile.SOU5, Tile.SOU5, Tile.SOU0)
    # Jihai koutsu
    JIH111 = Mentsu.KOUTSU + Tile.TON, (Tile.TON, Tile.TON, Tile.TON)
    JIH222 = Mentsu.KOUTSU + Tile.NAN, (Tile.NAN, Tile.NAN, Tile.NAN)
    JIH333 = Mentsu.KOUTSU + Tile.SHA, (Tile.SHA, Tile.SHA, Tile.SHA)
    JIH444 = Mentsu.KOUTSU + Tile.PEI, (Tile.PEI, Tile.PEI, Tile.PEI)
    JIH555 = Mentsu.KOUTSU + Tile.HAKU, (Tile.HAKU, Tile.HAKU, Tile.HAKU)
    JIH666 = Mentsu.KOUTSU + Tile.HATSU, (Tile.HATSU, Tile.HATSU, Tile.HATSU)
    JIH777 = Mentsu.KOUTSU + Tile.CHUN, (Tile.CHUN, Tile.CHUN, Tile.CHUN)

    # Manzu kantsu
    MAN1111 = Mentsu.KANTSU + Tile.MAN1, (Tile.MAN1, Tile.MAN1, Tile.MAN1, Tile.MAN1)
    MAN2222 = Mentsu.KANTSU + Tile.MAN2, (Tile.MAN2, Tile.MAN2, Tile.MAN2, Tile.MAN2)
    MAN3333 = Mentsu.KANTSU + Tile.MAN3, (Tile.MAN3, Tile.MAN3, Tile.MAN3, Tile.MAN3)
    MAN4444 = Mentsu.KANTSU + Tile.MAN4, (Tile.MAN4, Tile.MAN4, Tile.MAN4, Tile.MAN4)
    MAN5555 = Mentsu.KANTSU + Tile.MAN5, (Tile.MAN5, Tile.MAN5, Tile.MAN5, Tile.MAN0)
    MAN6666 = Mentsu.KANTSU + Tile.MAN6, (Tile.MAN6, Tile.MAN6, Tile.MAN6, Tile.MAN6)
    MAN7777 = Mentsu.KANTSU + Tile.MAN7, (Tile.MAN7, Tile.MAN7, Tile.MAN7, Tile.MAN7)
    MAN8888 = Mentsu.KANTSU + Tile.MAN8, (Tile.MAN8, Tile.MAN8, Tile.MAN8, Tile.MAN8)
    MAN9999 = Mentsu.KANTSU + Tile.MAN9, (Tile.MAN9, Tile.MAN9, Tile.MAN9, Tile.MAN9)
    # Pinzu kantsu
    PIN1111 = Mentsu.KANTSU + Tile.PIN1, (Tile.PIN1, Tile.PIN1, Tile.PIN1, Tile.PIN1)
    PIN2222 = Mentsu.KANTSU + Tile.PIN2, (Tile.PIN2, Tile.PIN2, Tile.PIN2, Tile.PIN2)
    PIN3333 = Mentsu.KANTSU + Tile.PIN3, (Tile.PIN3, Tile.PIN3, Tile.PIN3, Tile.PIN3)
    PIN4444 = Mentsu.KANTSU + Tile.PIN4, (Tile.PIN4, Tile.PIN4, Tile.PIN4, Tile.PIN4)
    PIN5555 = Mentsu.KANTSU + Tile.PIN5, (Tile.PIN5, Tile.PIN5, Tile.PIN5, Tile.PIN0)
    PIN6666 = Mentsu.KANTSU + Tile.PIN6, (Tile.PIN6, Tile.PIN6, Tile.PIN6, Tile.PIN6)
    PIN7777 = Mentsu.KANTSU + Tile.PIN7, (Tile.PIN7, Tile.PIN7, Tile.PIN7, Tile.PIN7)
    PIN8888 = Mentsu.KANTSU + Tile.PIN8, (Tile.PIN8, Tile.PIN8, Tile.PIN8, Tile.PIN8)
    PIN9999 = Mentsu.KANTSU + Tile.PIN9, (Tile.PIN9, Tile.PIN9, Tile.PIN9, Tile.PIN9)
    # Souzu kantsu
    SOU1111 = Mentsu.KANTSU + Tile.SOU1, (Tile.SOU1, Tile.SOU1, Tile.SOU1, Tile.SOU1)
    SOU2222 = Mentsu.KANTSU + Tile.SOU2, (Tile.SOU2, Tile.SOU2, Tile.SOU2, Tile.SOU2)
    SOU3333 = Mentsu.KANTSU + Tile.SOU3, (Tile.SOU3, Tile.SOU3, Tile.SOU3, Tile.SOU3)
    SOU4444 = Mentsu.KANTSU + Tile.SOU4, (Tile.SOU4, Tile.SOU4, Tile.SOU4, Tile.SOU4)
    SOU5555 = Mentsu.KANTSU + Tile.SOU5, (Tile.SOU5, Tile.SOU5, Tile.SOU5, Tile.SOU0)
    SOU6666 = Mentsu.KANTSU + Tile.SOU6, (Tile.SOU6, Tile.SOU6, Tile.SOU6, Tile.SOU6)
    SOU7777 = Mentsu.KANTSU + Tile.SOU7, (Tile.SOU7, Tile.SOU7, Tile.SOU7, Tile.SOU7)
    SOU8888 = Mentsu.KANTSU + Tile.SOU8, (Tile.SOU8, Tile.SOU8, Tile.SOU8, Tile.SOU8)
    SOU9999 = Mentsu.KANTSU + Tile.SOU9, (Tile.SOU9, Tile.SOU9, Tile.SOU9, Tile.SOU9)
    # Jihai kantsu
    JIH1111 = Mentsu.KANTSU + Tile.TON, (Tile.TON, Tile.TON, Tile.TON, Tile.TON)
    JIH2222 = Mentsu.KANTSU + Tile.NAN, (Tile.NAN, Tile.NAN, Tile.NAN, Tile.NAN)
    JIH3333 = Mentsu.KANTSU + Tile.SHA, (Tile.SHA, Tile.SHA, Tile.SHA, Tile.SHA)
    JIH4444 = Mentsu.KANTSU + Tile.PEI, (Tile.PEI, Tile.PEI, Tile.PEI, Tile.PEI)
    JIH5555 = Mentsu.KANTSU + Tile.HAKU, (Tile.HAKU, Tile.HAKU, Tile.HAKU, Tile.HAKU)
    JIH6666 = Mentsu.KANTSU + Tile.HATSU, (Tile.HATSU, Tile.HATSU, Tile.HATSU, Tile.HATSU)
    JIH7777 = Mentsu.KANTSU + Tile.CHUN, (Tile.CHUN, Tile.CHUN, Tile.CHUN, Tile.CHUN)

    # Manzu toitsu
    MAN11 = Mentsu.TOITSU + Tile.MAN1, (Tile.MAN1, Tile.MAN1)
    MAN22 = Mentsu.TOITSU + Tile.MAN2, (Tile.MAN2, Tile.MAN2)
    MAN33 = Mentsu.TOITSU + Tile.MAN3, (Tile.MAN3, Tile.MAN3)
    MAN44 = Mentsu.TOITSU + Tile.MAN4, (Tile.MAN4, Tile.MAN4)
    MAN55 = Mentsu.TOITSU + Tile.MAN5, (Tile.MAN5, Tile.MAN5)
    MAN66 = Mentsu.TOITSU + Tile.MAN6, (Tile.MAN6, Tile.MAN6)
    MAN77 = Mentsu.TOITSU + Tile.MAN7, (Tile.MAN7, Tile.MAN7)
    MAN88 = Mentsu.TOITSU + Tile.MAN8, (Tile.MAN8, Tile.MAN8)
    MAN99 = Mentsu.TOITSU + Tile.MAN9, (Tile.MAN9, Tile.MAN9)
    MAN50 = Mentsu.TOITSU + Tile.MAN5 + Mentsu.AKA, (Tile.MAN5, Tile.MAN0)
    # Pinzu koutsu
    PIN11 = Mentsu.TOITSU + Tile.PIN1, (Tile.PIN1, Tile.PIN1)
    PIN22 = Mentsu.TOITSU + Tile.PIN2, (Tile.PIN2, Tile.PIN2)
    PIN33 = Mentsu.TOITSU + Tile.PIN3, (Tile.PIN3, Tile.PIN3)
    PIN44 = Mentsu.TOITSU + Tile.PIN4, (Tile.PIN4, Tile.PIN4)
    PIN55 = Mentsu.TOITSU + Tile.PIN5, (Tile.PIN5, Tile.PIN5)
    PIN66 = Mentsu.TOITSU + Tile.PIN6, (Tile.PIN6, Tile.PIN6)
    PIN77 = Mentsu.TOITSU + Tile.PIN7, (Tile.PIN7, Tile.PIN7)
    PIN88 = Mentsu.TOITSU + Tile.PIN8, (Tile.PIN8, Tile.PIN8)
    PIN99 = Mentsu.TOITSU + Tile.PIN9, (Tile.PIN9, Tile.PIN9)
    PIN50 = Mentsu.TOITSU + Tile.PIN5 + Mentsu.AKA, (Tile.PIN5, Tile.PIN0)
    # Souzu koutsu
    SOU11 = Mentsu.TOITSU + Tile.SOU1, (Tile.SOU1, Tile.SOU1)
    SOU22 = Mentsu.TOITSU + Tile.SOU2, (Tile.SOU2, Tile.SOU2)
    SOU33 = Mentsu.TOITSU + Tile.SOU3, (Tile.SOU3, Tile.SOU3)
    SOU44 = Mentsu.TOITSU + Tile.SOU4, (Tile.SOU4, Tile.SOU4)
    SOU55 = Mentsu.TOITSU + Tile.SOU5, (Tile.SOU5, Tile.SOU5)
    SOU66 = Mentsu.TOITSU + Tile.SOU6, (Tile.SOU6, Tile.SOU6)
    SOU77 = Mentsu.TOITSU + Tile.SOU7, (Tile.SOU7, Tile.SOU7)
    SOU88 = Mentsu.TOITSU + Tile.SOU8, (Tile.SOU8, Tile.SOU8)
    SOU99 = Mentsu.TOITSU + Tile.SOU9, (Tile.SOU9, Tile.SOU9)
    SOU50 = Mentsu.TOITSU + Tile.SOU5 + Mentsu.AKA, (Tile.SOU5, Tile.SOU0)
    # Jihai koutsu
    JIH11 = Mentsu.TOITSU + Tile.TON, (Tile.TON, Tile.TON)
    JIH22 = Mentsu.TOITSU + Tile.NAN, (Tile.NAN, Tile.NAN)
    JIH33 = Mentsu.TOITSU + Tile.SHA, (Tile.SHA, Tile.SHA)
    JIH44 = Mentsu.TOITSU + Tile.PEI, (Tile.PEI, Tile.PEI)
    JIH55 = Mentsu.TOITSU + Tile.HAKU, (Tile.HAKU, Tile.HAKU)
    JIH66 = Mentsu.TOITSU + Tile.HATSU, (Tile.HATSU, Tile.HATSU)
    JIH77 = Mentsu.TOITSU + Tile.CHUN, (Tile.CHUN, Tile.CHUN)

    # Koukushi tiles
    KOUM1 = Mentsu.KOKUSHI + Tile.MAN1, (Tile.MAN1,)
    KOUM9 = Mentsu.KOKUSHI + Tile.MAN9, (Tile.MAN9,)
    KOUP1 = Mentsu.KOKUSHI + Tile.PIN1, (Tile.PIN1,)
    KOUP9 = Mentsu.KOKUSHI + Tile.PIN9, (Tile.PIN9,)
    KOUS1 = Mentsu.KOKUSHI + Tile.SOU1, (Tile.SOU1,)
    KOUS9 = Mentsu.KOKUSHI + Tile.SOU9, (Tile.SOU9,)
    KOUZ1 = Mentsu.KOKUSHI + Tile.TON, (Tile.TON,)
    KOUZ2 = Mentsu.KOKUSHI + Tile.NAN, (Tile.NAN,)
    KOUZ3 = Mentsu.KOKUSHI + Tile.SHA, (Tile.SHA,)
    KOUZ4 = Mentsu.KOKUSHI + Tile.PEI, (Tile.PEI,)
    KOUZ5 = Mentsu.KOKUSHI + Tile.HAKU, (Tile.HAKU,)
    KOUZ6 = Mentsu.KOKUSHI + Tile.HATSU, (Tile.HATSU,)
    KOUZ7 = Mentsu.KOKUSHI + Tile.CHUN, (Tile.CHUN,)

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
