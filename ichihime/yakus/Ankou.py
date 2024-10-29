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


class sanankou(base):
    menzen_han = 2
    fuuro_han = 2

    is_min = True
    is_yakuman = False

    name = "sanankou"
    eng = "three concealed triplets"
    abb = "SNA"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if sum(map(lambda x: 1 if _BL.isAnkou(x) or _BL.isAnkan(x) else 0, blocks.blocks)) >= 3:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class suuankou(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "suuankou"
    eng = "four concealed triplets"
    abb = "SUA"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if sum(map(lambda x: 1 if _BL.isAnkou(x) or _BL.isAnkan(x) else 0, blocks.blocks)) >= 4:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han
