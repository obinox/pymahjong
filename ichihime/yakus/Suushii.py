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


class shousuushii(base):
    menzen_han = 13
    fuuro_han = 13

    is_min = True
    is_yakuman = True

    name = "Shousuushii"
    eng = "little tempest"
    abb = "SSS"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        kaze = list(filter(lambda x: x.tiles[0] in _CT.KAZEHAI, blocks.blocks))
        if len(kaze) == 4:
            if sum(map(lambda x: 1 if _BL.isKoutsu(x) or _BL.isKantsu(x) else 0, kaze)) >= 3:
                return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class daisuushii(base):
    menzen_han = 26
    fuuro_han = 26

    is_min = True
    is_yakuman = True

    name = "Daisuushii"
    eng = "big tempest"
    abb = "DSS"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        kaze = list(filter(lambda x: x.tiles[0] in _CT.KAZEHAI and (_BL.isKoutsu(x) or _BL.isKantsu(x)), blocks.blocks))
        if len(kaze) == 4:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class sanpuukou(base):
    menzen_han = 2
    fuuro_han = 2

    is_min = True
    is_yakuman = False

    name = "Sanpuukou"
    eng = "third wind"
    abb = "SPU"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        kaze = list(filter(lambda x: x.tiles[0] in _CT.KAZEHAI and (_BL.isKoutsu(x) or _BL.isKantsu(x)), blocks.blocks))
        if len(kaze) >= 3:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han
