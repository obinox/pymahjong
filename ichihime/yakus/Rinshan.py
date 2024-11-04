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


class rinshan(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Rinshan kaihou"
    eng = "blooming on the ridge"
    abb = "RIN"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.aru == _ARU.RINSHAN:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class rinshankaihou(rinshan):
    pass


rinshankaihou = rinshan


class toukanhou(base):
    menzen_han = 13
    fuuro_han = 13

    is_min = True
    is_yakuman = True

    name = "Toukanhou"
    eng = "the first blooming"
    abb = "TKA"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.aru == _ARU.RINSHAN and blocks.agari.ippatsu == _ARU.IPPATSU and (not blocks.agari.riichi):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han
