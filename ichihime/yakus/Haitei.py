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


class haitei(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Haitei raoyue"
    eng = "pulling the moon under the sea"
    abb = "HAI"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.aru == _ARU.HAITEI:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class houtei(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = True
    is_yakuman = False

    name = "Houtei raoyui"
    eng = "fishing under the riverbed"
    abb = "HOU"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.aru == _ARU.HOUTEI:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class haiteiraoyue(haitei):
    pass


class houteiraoyui(houtei):
    pass


class haiteitsumo(haitei):
    pass


class haiteiron(houtei):
    pass


haiteiraoyue = haitei
houteiraoyui = houtei
haiteitsumo = haitei
haiteiron = houtei


class ishinouenimosannen(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Ishino uenimo sannen"
    eng = "three years on a rock"
    abb = "ISH"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.agari.riichi == _ARU.DABURI and blocks.agari.aru in {_ARU.HAITEI, _ARU.HOUTEI}:
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class ishisan(ishinouenimosannen):
    pass


ishisan = ishinouenimosannen
