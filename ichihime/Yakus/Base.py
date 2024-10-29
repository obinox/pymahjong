from abc import *
from typing import List, Self

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


class base:
    __: Self = None
    menzen_han: int = 0
    fuuro_han: int = 0

    is_min: bool = True
    is_yakuman: bool = False

    upper_yaku: List = None

    name: str = None
    eng: str = None
    abb: str = None

    def __new__(cls):
        if not cls.__:
            cls.__ = super(base, cls).__new__(cls)
        return cls.__

    @classmethod
    @abstractmethod
    def check(cls, blocks: _BS, yama: _YA = None, *args) -> int | None:
        raise NotImplementedError

    def __str__(self) -> str:
        if self.name:
            return self.name
        raise NotImplementedError

    def __repr__(self) -> str:
        if self.abb:
            return self.abb
        raise NotImplementedError
