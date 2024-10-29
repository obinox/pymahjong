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


class toitoi(base):
    menzen_han = 2
    fuuro_han = 2

    is_min = True
    is_yakuman = False

    name = "Toitoi"
    eng = "all triplets"
    abb = "TOI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if all(map(lambda x: _BL.isKoutsu(x) or _BL.isKantsu(x), blocks.mentsu)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han
