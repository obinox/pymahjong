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


class bakaze(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Bakaze"
    eng = "round wind"
    abb = "BAK"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(blocks.bakaze):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class jikaze(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Jikaze"
    eng = "seat wind"
    abb = "JIK"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(blocks.jikaze):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class haku(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Haku"
    eng = "white dragon"
    abb = "HKU"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(_TL.HAKU):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class hatsu(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Hatsu"
    eng = "green dragon"
    abb = "HTS"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(_TL.HTSU):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class chun(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Chun"
    eng = "rad dragon"
    abb = "CUN"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(_TL.CHUN):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class bagen(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Jigen"
    eng = "round dragon"
    abb = "BAG"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(blocks.bagen):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class jigen(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: bagen"
    eng = "seat dragon"
    abb = "JIG"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(blocks.jigen):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class ton(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Ton"
    eng = "east wind"
    abb = "TON"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(_TL.TONN):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class nan(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Nan"
    eng = "south wind"
    abb = "NAN"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(_TL.NANN):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class shaa(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Shaa"
    eng = "west wind"
    abb = "SHA"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(_TL.SHAA):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class pei(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Yakuhai: Pei"
    eng = "north wind"
    abb = "PEI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.isInclude(_TL.PEII):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han
