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


class kokushi(base):
    menzen_han = 13
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Kokushi musou"
    eng = "thirteen orphans"
    abb = "KMU"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.tenpai.machi in {_MC.KMU, _MC.K13} and all(map(lambda x: _BL.isKokushi(x), blocks.blocks)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class juusan(base):
    menzen_han = 26
    fuuro_han = None

    is_min = True
    is_yakuman = True

    name = "Kokushi musou 13-men machi"
    eng = "all out thirteen orphans"
    abb = "KMJ"

    @classmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        if blocks.tenpai.machi == _MC.K13 and all(map(lambda x: _BL.isKokushi(x), blocks.blocks)):
            return cls.menzen_han if blocks.isMenzen() else cls.fuuro_han


class kokushimusou(kokushi):
    pass


class kokushi13(juusan):
    pass


class juusanmen(juusan):
    pass


class juusanmenmachi(juusan):
    pass


class kokushijuusanmenmachi(juusan):
    pass


class kokushimusoujuusanmenmachi(juusan):
    pass


kokushimusou = kokushi
kokushi13 = juusan
juusanmen = juusan
juusanmenmachi = juusan
kokushijuusanmenmachi = juusan
kokushimusoujuusanmenmachi = juusan
