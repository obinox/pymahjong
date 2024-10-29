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

from .Reference.ChantaReference import CHANTAREF, JUNCHANREF


class chanta(base):
    menzen_han = 2
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Chanta"
    eng = "mixed terminals"
    abb = "CHA"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if all(bl in CHANTAREF for bl in blocks.blocks):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class junchan(base):
    menzen_han = 3
    fuuro_han = 2

    is_min = True
    is_yakuman = False

    name = "Junchan"
    eng = "mixed ends"
    abb = "JUN"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if all(bl in JUNCHANREF for bl in blocks.blocks):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class honchantaiyaochuu(chanta):
    pass


class chantaiyaochuu(chanta):
    pass


class chantaiyao(chanta):
    pass


class junchantaiyaochuu(junchan):
    pass


class junchanta(junchan):
    pass


honchantaiyaochuu = chanta
chantaiyaochuu = chanta
chantaiyao = chanta
junchantaiyaochuu = junchan
junchanta = junchan
