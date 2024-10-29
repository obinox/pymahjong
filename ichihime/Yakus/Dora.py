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

from .Reference.DoraReference import *


class dora(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = False
    is_yakuman = False

    name = "Dora"
    eng = "dora"
    abb = "DRA"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA, ref=None, *args) -> int | None:
        han = 0
        menzen = blocks.isMenzen()
        doraidc = yama.doraidc[: yama.idc_open + 1]

        if ref == 4 or ref == None:
            ref = DEFAULT_DORAREF
        elif ref == 3:
            ref = SANMA_DORAREF

        dorapai = []
        for t in doraidc:
            dorapai += ref[t]

        dorapai.sort()

        te = sum(map(lambda x: x.tiles, blocks.blocks), ())

        for t in te:
            for d in dorapai:
                if d == t:
                    han += cls.menzen_han if menzen else cls.fuuro_han

        return han


class uradora(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = False
    is_yakuman = False

    name = "Uradora"
    eng = "hidden dora"
    abb = "URD"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA, ref=None, *args) -> int | None:
        han = 0
        menzen = blocks.isMenzen()
        udoraidc = yama.udoraidc[: yama.idc_open + 1]

        if ref == 4 or ref == None:
            ref = DEFAULT_DORAREF
        elif ref == 3:
            ref = SANMA_DORAREF

        udorapai = []
        for t in udoraidc:
            udorapai += ref[t]

        udorapai.sort()

        te = sum(map(lambda x: x.tiles, blocks.blocks), ())

        for t in te:
            for d in udorapai:
                if d == t:
                    han += cls.menzen_han if menzen else cls.fuuro_han

        return han


class akadora(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = False
    is_yakuman = False

    name = "Akadora"
    eng = "red five dora"
    abb = "AKD"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA, ref=None, *args) -> int | None:
        han = 0
        menzen = blocks.isMenzen()

        te = sum(map(lambda x: x.tiles, blocks.blocks), ())

        for t in te:
            for d in _CT.AKAPAI:
                if d == t:
                    han += cls.menzen_han if menzen else cls.fuuro_han

        return han


class nukidora(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = False
    is_yakuman = False

    name = "Nukidora"
    eng = "replacement dora"
    abb = "NKD"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA, ref=None, *args) -> int | None:
        han = 0
        menzen = blocks.isMenzen()

        han += (cls.menzen_han if menzen else cls.fuuro_han) * blocks.nuki

        return han


class ura(uradora):
    pass


class aka(akadora):
    pass


class nuki(nukidora):
    pass


class peidora(nukidora):
    pass


ura = uradora
aka = akadora
nuki = nukidora
peidora = nukidora
