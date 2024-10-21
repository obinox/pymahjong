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


class temp(base):
    menzen_han = 0
    fuuro_han = 0

    is_min = True
    is_yakuman = False

    name = "None"
    eng = "None"
    abb = "None"

    @classmethod
    def check(cls, block: _BS, yama: _YA = None, *args) -> int:
        raise NotImplementedError
