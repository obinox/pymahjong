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


class shousangen(base):
    menzen_han = 2
    fuuro_han = 2

    is_min = True
    is_yakuman = False

    name = "Shousangen"
    eng = "little trinity"
    abb = "SSG"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        sangen = list(filter(lambda x: x.tiles[0] in _CT.SANGENPAI, blocks.blocks))
        if len(sangen) == 3:
            if sum(map(lambda x: 1 if _BL.isKoutsu(x) or _BL.isKantsu(x) else 0, sangen)) >= 2:
                return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class daisangen(base):
    menzen_han = 13
    fuuro_han = 13

    is_min = True
    is_yakuman = True

    name = "Daisangen"
    eng = "big trinity"
    abb = "DSG"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        sangen = list(filter(lambda x: x.tiles[0] in _CT.SANGENPAI and (_BL.isKoutsu(x) or _BL.isKantsu(x)), blocks.blocks))
        if len(sangen) == 3:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han
