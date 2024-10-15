from typing import List

from ichihime.enums import category as _CT
from ichihime.src import blocks as _BL


class Basic:
    menzen_han: int = 0
    fuuro_han: int = 0

    is_min: bool = True
    is_yakuman: bool = False
    is_mangan: bool = False

    upper_yaku: List = None

    name: str = ""
    translate: str = ""
    abb: str = ""

    @classmethod
    def check(cls, block: _BL) -> bool:
        pass

    @classmethod
    def __str__(self) -> str:
        return self.name

    @classmethod
    def __repr__(self) -> str:
        return self.abb
