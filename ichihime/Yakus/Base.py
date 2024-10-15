from abc import *
from typing import List, Self

from ichihime.enums import cat as _CT
from ichihime.src import blocks as _BL
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
    def check(cls, block: _BL, yama: _YA = None) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        if self.name:
            return self.name
        raise NotImplementedError

    def __repr__(cls) -> str:
        if cls.abb:
            return cls.abb
        raise NotImplementedError
