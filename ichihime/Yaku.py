from enum import Enum
from typing import Self, Tuple

from ichihime.Agari import Agari
from ichihime.Block import Block
from ichihime.Tenpai import Tenpai
from ichihime.Tile import Tile


class Yaku(Enum, str):
    RCH = "riichi", (1, 0)
    DRI = "double riichi", (2, 0)

    IPP = "ippatsu", (1, 0)

    RIN = "rinshan", (1, 1)
    CHK = "chankan", (1, 1)
    HAI = "haitei", (1, 1)
    HOU = "houtei", (1, 1)
    IPP = "ippatsu", (1, 0)

    SMO = "tsumo", (1, 0)

    YAK = "yakuhai", (1, 1)
    PFU = "pinfu", (1, 0)
    TAN = "tanyao", (1, 1)
    IPK = "iipeikou", (1, 0)
    ITT = "ittsu", (2, 1)
    SDJ = "sanshoku doujun", (2, 1)

    SDO = "sanshoku doukou", (2, 2)
    SNK = "sankantsu", (2, 2)
    TOI = "toitoi", (2, 2)
    SNA = "sanankou", (2, 2)
    SSG = "shousangen", (2, 2)
    HRO = "honroutou", (2, 2)
    HON = "honittsu", (3, 2)

    CHA = "chanta", (2, 1)
    JUN = "junchan", (3, 2)
    RPK = "ryanpaikou", (3, 0)
    CHN = "chinittsu", (6, 5)
    CHI = "chiitoi", (2, 0)

    DRA = "dora", (1, 1)
    AKA = "akadora", (1, 1)
    NUK = "nukidora", (1, 1)
    URA = "uradora", (1, 1)

    REN = "renhou", (0, 0)
    NAG = "nagashi mangan", (5, 5)

    # Yakuman
    KAZ = "kazoe", (13, 0)
    TEN = "tenhou", (13, 0)
    CHH = "chiihou", (13, 0)
    DSG = "daisangen", (13, 13)
    SUA = "suuankou", (13, 0)
    TSU = "tsuuiisou", (13, 13)
    CHR = "chinroutou", (13, 13)
    RYU = "ryuiisou", (13, 13)
    KMU = "kokushi musou", (13, 0)
    SSS = "shousuushii", (13, 13)
    SUK = "suukantsu", (13, 13)
    CHU = "chuuren poutou", (13, 0)
    CHU9 = "chuuren kyumen machi", (26, 0)
    SUA1 = "suuankou tanki", (26, 0)
    KMU13 = "kokushi juusanmen machi", (26, 0)
    DSS = "daisuushii", (26, 26)

    def __new__(cls, value: str, han: Tuple[int]) -> Self:
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.han = han
        return obj

    def __init__(self, value: str, han: int) -> None:
        self._value_ = value
        self.han: int

    @staticmethod
    def yaku(block: Block):
        block.tenpai
