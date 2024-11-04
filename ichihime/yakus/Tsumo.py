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


class tsumo(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Menzenchin tsumohou"
    eng = "all by oneself"
    abb = "TSM"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.tsumo == _ARU.TSUMO:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class tenhou(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Tenhou"
    eng = "blessing of the heaven"
    abb = "TNH"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.tsumo == _ARU.TSUMO and blocks.agari.ippatsu == _ARU.IPPATSU and (not blocks.agari.riichi) and blocks.jikaze == _YA.oya:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class chiihou(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Chiihou"
    eng = "blessing of the earth"
    abb = "CHH"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.tsumo == _ARU.TSUMO and blocks.agari.ippatsu == _ARU.IPPATSU and (not blocks.agari.riichi) and blocks.jikaze != _YA.oya:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class menzentsumo(tsumo):
    pass


class menzenchintsumohou(tsumo):
    pass


menzentsumo = tsumo
menzenchintsumohou = tsumo


class renhou(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "renhou"
    eng = "blessing of the saint"
    abb = "REH"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.tsumo == _ARU.RON and blocks.agari.ippatsu == _ARU.IPPATSU and (not blocks.agari.riichi):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han
