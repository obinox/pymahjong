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


class riichi(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Riichi"
    eng = "fixed"
    abb = "RII"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.riichi == _ARU.RIICHI:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class daburi(base):
    menzen_han = 2
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Daburu riichi"
    eng = "fixed from the beginning"
    abb = "DRI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.riichi == _ARU.DABURI:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class ippatsu(base):
    menzen_han = 1
    fuuro_han = None

    is_min = False
    is_yakuman = False

    name = "Ippatsu"
    eng = "one shot"
    abb = "IPP"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.ippatsu == _ARU.IPPATSU:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class dabururiichi(daburi):
    pass


class doubleriichi(daburi):
    pass


dabururiichi = daburi
doubleriichi = daburi


class openri(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Open riichi"
    eng = "fixed with open"
    abb = "ORI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.riichi == _ARU.OPENRI:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class openriichi(openri):
    pass


openriichi = openri
