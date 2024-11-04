from enum import Enum
from typing import List, Self, Tuple

from ichihime.enums.Agaru import agaru
from ichihime.enums.Block import block
from ichihime.enums.Category import cat
from ichihime.enums.Mentsu import mentsu
from ichihime.enums.Tile import tile
from ichihime.src.Agari import agari
from ichihime.src.Blocks import blocks
from ichihime.src.Tenpai import tenpai


class Yaku(str, Enum):
    # RCH = "riichi", (1, 0)
    # DRI = "double riichi", (2, 0)

    # IPP = "ippatsu", (1, 0)

    # RIN = "rinshan", (1, 1)
    # CHK = "chankan", (1, 1)
    # HAI = "haitei", (1, 1)
    # HOU = "houtei", (1, 1)

    # SMO = "tsumo", (1, 0)

    # YAK = "yakuhai", (1, 1)
    # HKU = "yakuhai: haku", (1, 1)
    # HTS = "yakuhai: hatsu", (1, 1)
    # CUN = "yakuhai: chun", (1, 1)
    # BAK = "yakuhai: bakaze", (1, 1)
    # JIK = "yakuhai: jikaze", (1, 1)

    # PFU = "pinfu", (1, 0)
    # TAN = "tanyao", (1, 1)
    # IPK = "iipeikou", (1, 0)
    # ITT = "ittsu", (2, 1)
    # SDJ = "sanshoku doujun", (2, 1)

    # SDO = "sanshoku doukou", (2, 2)
    # SNK = "sankantsu", (2, 2)
    # TOI = "toitoi", (2, 2)
    # SNA = "sanankou", (2, 2)
    # SSG = "shousangen", (2, 2)
    # HRO = "honroutou", (2, 2)
    # HON = "honitsu", (3, 2)

    # CHA = "chanta", (2, 1)
    # JUN = "junchan", (3, 2)
    # RPK = "ryanpaikou", (3, 0)
    # CHN = "chinittsu", (6, 5)
    # CHI = "chiitoi", (2, 0)

    # DRA = "dora", (1, 1)
    # AKA = "akadora", (1, 1)
    # NUK = "nukidora", (1, 1)
    # URA = "uradora", (1, 1)

    # REN = "renhou", (0, 0)
    NAG = "nagashi mangan", (5, 5)

    # Yakuman
    # KAZ = "kazoe", (13, 0)
    # TEN = "tenhou", (13, 0)
    # CHH = "chiihou", (13, 0)
    # DSG = "daisangen", (13, 13)
    # SUA = "suuankou", (13, 0)
    # TSU = "tsuuiisou", (13, 13)
    # CHR = "chinroutou", (13, 13)
    # RYU = "ryuiisou", (13, 13)
    # KMU = "kokushi musou", (13, 0)
    # SSS = "shousuushii", (13, 13)
    # SUK = "suukantsu", (13, 13)
    # CHU = "chuuren poutou", (13, 0)
    # CHU9 = "chuuren kyumen machi", (26, 0)
    # SUA1 = "suuankou tanki", (26, 0)
    # KMU13 = "kokushi juusanmen machi", (26, 0)
    # DSS = "daisuushii", (26, 26)
    # daisharin
    # daichikurin
    # daisuurin
    # toukanhou
    #

    def __new__(cls, value: str, han: Tuple[int, int]) -> Self:
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.han = han
        obj.menzen, obj.fuuro = han
        return obj

    def __init__(self, value: str, han: Tuple[int, int]) -> None:
        self._value_ = value
        self.han: int
        self.menzen: int
        self.fuuro: int

    @staticmethod
    def yaku(block: blocks, aotenjou: bool = False):
        out: List[Yaku] = []
        yakuman: List[Yaku] = []
        tefuda = list(sum(map(lambda x: block(x).tiles, block.blocks), ()))
        menzen = all(map(lambda x: x <= mentsu.MINJUN, block.mentsu))
        print(menzen, tefuda)
        if menzen and block.agari.tsumo == agaru.TSUMO:
            out.append(Yaku.SMO)

        match block.agari.riichi:
            case agaru.RIICHI:
                out.append(Yaku.RCH)
            case agaru.DABURI:
                out.append(Yaku.DRI)

        match block.agari.aru:
            case agaru.RINSHAN:
                out.append(Yaku.RIN)
            case agaru.CHANKAN:
                out.append(Yaku.CHK)
            case agaru.HAITEI:
                out.append(Yaku.HAI)
            case agaru.HOUTEI:
                out.append(Yaku.HOU)

        match block.agari.ippatsu:
            case agaru.IPPATSU:
                out.append(Yaku.IPP)

        if cat.allIn(tefuda, cat.CHUNCHANHAI):
            out.append(Yaku.TAN)

        if block.bakaze + mentsu.KOUTSU in block.blocks:
            out.append(Yaku.BAK)
        if block.jikaze + mentsu.KOUTSU in block.blocks:
            out.append(Yaku.JIK)
        if tile.HAKU + mentsu.KOUTSU in block.blocks:
            out.append(Yaku.HKU)
        if tile.HTSU + mentsu.KOUTSU in block.blocks:
            out.append(Yaku.HTS)
        if tile.CHUN + mentsu.KOUTSU in block.blocks:
            out.append(Yaku.CUN)

        return out
