from collections import Counter

from ichihime.enums import agaru as _ARU
from ichihime.enums import block as _BL
from ichihime.enums import cat as _CT
from ichihime.enums import fuuro as _FU
from ichihime.enums import group as _GR
from ichihime.enums import machi as _MC
from ichihime.enums import mentsu as _MT
from ichihime.enums import player as _PL
from ichihime.enums import tile as _TL
from ichihime.src import agari as _ARI
from ichihime.src import blocks as _BS
from ichihime.src import tenpai as _TP
from ichihime.src import yama as _YA
from ichihime.yakus import base


class iipeikou(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Iipeikou"
    eng = "double sequence"
    abb = "IPK"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        bl, cnt = Counter(blocks.mentsu).most_common()[0]
        if _BL.isShuntsu(bl) and cnt >= 2:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class ryanpeikou(base):
    menzen_han = 3
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Ryanpeikou"
    eng = "double double sequence"
    abb = "RPK"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        bl1, cnt1 = Counter(blocks.mentsu).most_common()[0]
        bl2, cnt2 = Counter(blocks.mentsu).most_common()[1]
        if _BL.isShuntsu(bl1) and cnt1 >= 2 and _BL.isShuntsu(bl2) and cnt2 >= 2:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class ipeko(iipeikou):
    pass


class rpeko(ryanpeikou):
    pass


class peko(iipeikou):
    pass


class pekopeko(ryanpeikou):
    pass


ipeko = iipeikou
rpeko = ryanpeikou
peko = iipeikou
pekopeko = ryanpeikou
