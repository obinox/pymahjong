from typing import List

from ichihime.enums import cat as _CT
from ichihime.enums import group as _GR
from ichihime.enums import tile as _TL
from ichihime.src import blocks as _BL
from ichihime.src import yama as _YA
from ichihime.yakus import base


class dora(base):
    menzen_han = 1
    fuuro_han = 1

    is_min = False
    is_yakuman = False

    name = "Dora"
    eng = "dora"
    abb = "DRA"

    @classmethod
    def check(cls, block, yama) -> bool:
        yama.idc_open = 4
        doraidc = map(lambda x: x, yama.doraidc[: yama.idc_open + 1])
        for t in doraidc:
            print(
                t,
                _CT.getCat(t)[0][t.actual % t.group.count],
                _CT.getCat(t)[1][t.actual % t.group.count],
            )
