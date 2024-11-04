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
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        shun = list(map(lambda x: _BL(x - _MT.AKA) if x % _GR.PIN > _TL.MAN9 else x, blocks.getShuntsu()))
        if any(map(lambda x: shun.count(x) >= 2, shun)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class ryanpeikou(base):
    menzen_han = 3
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Ryanpeikou"
    eng = "doubled double sequence"
    abb = "RPK"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        shun = list(map(lambda x: _BL(x - _MT.AKA) if x % _GR.PIN > _TL.MAN9 else x, blocks.getShuntsu()))
        if sum(map(lambda x: 1 if shun.count(x) >= 2 else 0, shun)) >= 2:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class ipeko(iipeikou):
    pass


class rpeko(ryanpeikou):
    pass


class peko(iipeikou):
    pass


class pekopeko(ryanpeikou):
    pass


ipeko = iipeikou
rpeko = ryanpeikou
peko = iipeikou
pekopeko = ryanpeikou

from .Reference.SharinReference import *


class daisharin(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Daisharin"
    eng = "wheel of fortune"
    abb = "DSH"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), DAISHARINREF.items())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class daichikurin(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Daichikurin"
    eng = "bamboo forest"
    abb = "DCK"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), DAICHIKURINREF.items())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class daisuurin(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Daisuurin"
    eng = "numerous numbers"
    abb = "DSU"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), DAISUURINREF.items())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class chunsharin(base):
    menzen_han = 3
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Chunsharin"
    eng = "wheel of fate"
    abb = "CSH"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), CHUNSHARINREF.items())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class chunchikurin(base):
    menzen_han = 3
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Chunchikurin"
    eng = "bamboo field"
    abb = "CCK"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), CHUNCHIKURINREF.items())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class chunsuurin(base):
    menzen_han = 3
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Chunsuurin"
    eng = "natural numbers"
    abb = "CSU"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), CHUNSUURINREF.items())):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class shousharin(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Shousharin"
    eng = "wheel of destiny"
    abb = "SSH"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if any(map(lambda r: all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), r.items())), SHOUSHARINREF)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class shouchikurin(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Shouchikurin"
    eng = "bamboo tree"
    abb = "SCK"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if any(map(lambda r: all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), r.items())), SHOUCHIKURINREF)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class shousuurin(base):
    menzen_han = 1
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Shousuurin"
    eng = "normal numbers"
    abb = "SSU"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        tiles = blocks.getTiles()
        if any(map(lambda r: all(map(lambda x: any(map(lambda y: tiles.count(y) >= x[1], x[0])), r.items())), SHOUSUURINREF)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class isshokusanjun(base):
    menzen_han = 3
    fuuro_han = 2

    is_min = True
    is_yakuman = False

    name = "Isshoku sanjun"
    eng = "triple sequence"
    abb = "ISS"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        shun = list(map(lambda x: _BL(x - _MT.AKA) if x % _GR.PIN > _TL.MAN9 else x, blocks.getShuntsu()))
        if any(map(lambda x: shun.count(x) >= 3, shun)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class isshokuyonjun(base):
    menzen_han = 13
    fuuro_han = 13

    is_min = True
    is_yakuman = True

    name = "Isshoku yonjun"
    eng = "quadruple sequence"
    abb = "ISY"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        shun = list(map(lambda x: _BL(x - _MT.AKA) if x % _GR.PIN > _TL.MAN9 else x, blocks.getShuntsu()))
        if any(map(lambda x: shun.count(x) >= 4, shun)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class suurentaihou(base):
    pass


suurentaihou = isshokuyonjun


class ryanpeikoudoujun(base):
    menzen_han = 3
    fuuro_han = None

    is_min = True
    is_yakuman = False

    name = "Ryanpeikou doujun"
    eng = "two colored double sequence"
    abb = "RPK"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        shun = list(map(lambda x: _BL(x - _MT.AKA) if x % _GR.PIN > _TL.MAN9 else x, blocks.getShuntsu()))
        shunmod = list(map(lambda x: (_BL(x - _MT.AKA) if x % _GR.PIN > _TL.MAN9 else x).value % _GR.PIN, blocks.getShuntsu()))
        if sum(map(lambda x: 1 if shun.count(x) >= 2 else 0, shun)) >= 2 and any(map(lambda x: shunmod.count(x) >= 4, shunmod)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class ryandoujun(ryanpeikoudoujun):
    pass


ryanpeikoudoujun = ryandoujun
