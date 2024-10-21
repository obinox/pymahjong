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
    def check(cls, block: _BS, yama: _YA = None, *args) -> int:
        bl, cnt = Counter(block.mentsu).most_common()[1]
        if bl < _MT.KOUTSU and cnt >= 2:
            return cls.menzen_han if block.is_menzen() else cls.fuuro_han
