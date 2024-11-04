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

from .Reference.ChuurenReference import CHUURENREF


class chuuren(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Chuuren poutou"
    eng = "nine lotus lantern"
    abb = "CRP"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if any(map(lambda r: all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), r.items())), CHUURENREF)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class junsei(base):
    menzen_han = 26
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Junsei chuuren poutou"
    eng = "white nine lotus lantern"
    abb = "JCR"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = list(blocks.getTiles())
        tiles.remove(blocks.tenpai.tile)
        if any(map(lambda r: all(map(lambda x: any(map(lambda y: tiles.count(y) == x[1], x[0])), r.items())), CHUURENREF)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class chuurenpoutou(chuuren):
    pass


class junseichuurenpoutou(junsei):
    pass


class kyuumen(junsei):
    pass


class chuurenkyuumenmachi(junsei):
    pass


chuurenpoutou = chuuren
junseichuurenpoutou = junsei
kyuumen = junsei
chuurenkyuumenmachi = junsei
