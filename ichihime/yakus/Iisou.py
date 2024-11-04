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


class honiisou(base):
    menzen_han = 3
    fuuro_han = 2

    is_min = True
    is_yakuman = False

    name = "Honiisou"
    eng = "half flush"
    abb = "HNI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        cts = _CT.HONMANZUA, _CT.HONPINZUA, _CT.HONSOUZUA
        if any(map(lambda y: all(map(lambda x: x in y, blocks.getTiles())), cts)) and any(map(lambda x: x in _CT.SHUUPAIA, blocks.getTiles())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class chiniisou(base):
    menzen_han = 6
    fuuro_han = 5

    is_min = True
    is_yakuman = False

    name = "Chiniisou"
    eng = "full flush"
    abb = "CNI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        cts = _CT.MANZUA, _CT.PINZUA, _CT.SOUZUA
        if any(map(lambda y: all(map(lambda x: x in y, blocks.getTiles())), cts)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class tsuiisou(base):
    menzen_han = 13
    fuuro_han = 13

    is_min = True
    is_yakuman = True

    name = "Tsuiisou"
    eng = "all words"
    abb = "TSI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if all(map(lambda x: x in _CT.JIHAI, blocks.getTiles())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class ryuiisou(base):
    menzen_han = 13
    fuuro_han = 13

    is_min = True
    is_yakuman = True

    name = "Ryuiisou"
    eng = "all greens"
    abb = "RYI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if all(map(lambda x: x in _CT.MIDORIPAI, blocks.getTiles())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class honitsu(honiisou):
    pass


class chinitsu(chiniisou):
    pass


honitsu = honiisou
chinitsu = chiniisou


class junseiryuiisou(base):
    menzen_han = 26
    fuuro_han = 26

    is_min = True
    is_yakuman = True

    name = "Junsei ryuiisou"
    eng = "pure greens"
    abb = "JRI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if all(map(lambda x: x in _CT.MIDORIPAI, blocks.getTiles())) and all(map(lambda x: x in _CT.SOUZUA, blocks.getTiles())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class benikujku(base):
    menzen_han = 13
    fuuro_han = 13

    is_min = True
    is_yakuman = True

    name = "Benikujaku"
    eng = "red peakcok"
    abb = "BEN"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if all(map(lambda x: x in _CT.JAKUPAI, blocks.getTiles())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class kokuiisou(base):
    menzen_han = 13
    fuuro_han = 13

    is_min = True
    is_yakuman = True

    name = "Kokuiisou"
    eng = "all blacks"
    abb = "KKI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if all(map(lambda x: x in _CT.KUROPAI, blocks.getTiles())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han
