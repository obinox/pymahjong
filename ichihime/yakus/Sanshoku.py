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

from .Reference.SanshokuReference import SANDOUJUNREF, SANSHOKUREF


class doujun(base):
    menzen_han = 2
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Sanshoku doujun"
    eng = "three colored sequence"
    abb = "SDJ"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if any(all(any(b in blocks.getShuntsu() for b in bl) for bl in san) for san in SANSHOKUREF):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class doukou(base):
    menzen_han = 2
    fuuro_han = 2

    is_min = True
    is_yakuman = False

    name = "Sanshoku doukou"
    eng = "three colored triplet"
    abb = "SDO"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if any(all(any(b in blocks.getKoutsu() for b in bl) for bl in san) for san in SANDOUJUNREF):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class sanshoku(doujun):
    pass


class sandoukou(doukou):
    pass


class sanshokudoujun(doujun):
    pass


class sanshokudoukou(doukou):
    pass


sanshoku = doujun
sandoukou = doukou
sanshokudoujun = doujun
sanshokudoukou = doukou
