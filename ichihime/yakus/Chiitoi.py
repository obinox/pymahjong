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


class chiitoi(base):
    menzen_han = 2
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Chiitoitsu"
    eng = "seven pairs"
    abb = "CHI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.tenpai.machi == _MC.CHI and all(map(lambda x: _BL.isToitsu(x), blocks.blocks)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class chiitoitsu(chiitoi):
    pass


class niconico(chiitoi):
    pass


chiitoitsu = chiitoi
niconico = chiitoi


class daichisei(base):
    menzen_han = 26
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Daichisei"
    eng = "septentrions"
    abb = "DCS"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if (
            blocks.tenpai.machi == _MC.CHI
            and all(map(lambda x: _BL.isToitsu(x), blocks.blocks))
            and all(map(lambda x: x in _CT.JIHAI, blocks.getTiles()))
        ):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class sangentoitsu(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Sangen toitsu"
    eng = "trinity heads"
    abb = "SGT"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        sangen = list(filter(lambda x: x.tiles[0] in _CT.SANGENPAI, blocks.blocks))
        if blocks.tenpai.machi == _MC.CHI and all(map(lambda x: _BL.isToitsu(x), blocks.blocks)) and len(sangen) == 3:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class suushitoitsu(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Suushi toitsu"
    eng = "tempest heads"
    abb = "SST"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        kaze = list(filter(lambda x: x.tiles[0] in _CT.KAZEHAI, blocks.blocks))
        if blocks.tenpai.machi == _MC.CHI and all(map(lambda x: _BL.isToitsu(x), blocks.blocks)) and len(kaze) == 4:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han
