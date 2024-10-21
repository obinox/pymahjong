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


class pinfu(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Pinfu"
    eng = "flat hand"
    abb = "PFU"

    @classmethod
    def check(cls, block: _BS, yama: _YA = None, *args) -> int:
        # TODO change logic to calculating score with no additional fu
        if (
            block.is_menzen()
            and all(map(lambda x: x < _MT.KOUTSU, block.mentsu))
            and block.jantou.tiles[0] not in {*_CT.SANGENPAI, block.bakaze, block.jikaze}
            and block.tenpai.machi in {_MC.RML, _MC.RMR}
        ):
            return cls.menzen_han if block.is_menzen() else cls.fuuro_han
