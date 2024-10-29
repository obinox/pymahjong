import random
from typing import List

from ichihime.enums import cat as _CT
from ichihime.enums import tile as _TL

from .YamaReference import *


class yama:
    tiles: List[_TL] = []
    yama: List[_TL] = []
    rinshan: List[_TL] = []
    doraidc: List[_TL] = []
    udoraidc: List[_TL] = []
    idc_open: int = 0
    is_setted = False

    def __new__(cls) -> None:
        raise AttributeError

    def __init__(self) -> None:
        raise AttributeError

    @classmethod
    def setyama(cls, tiles: List[_TL] = None, seed=None, rinshan: int = 4) -> None:
        if tiles == None or tiles == 4:
            tiles = list(map(lambda x: [x[0]] * x[1], DEFAULT_YAMA_CONFIG.items()))
            tiles = sorted(sum(tiles, []))
        elif tiles == 3:
            tiles = list(map(lambda x: [x[0]] * x[1], SANMA_YAMA_CONFIG.items()))
            tiles = sorted(sum(tiles, []))
        print(tiles)

        random.seed(seed)
        random.shuffle(tiles)
        random.seed(None)

        cls.is_setted = True
        cls.tiles = tiles
        cls.yama = tiles[10 + rinshan :]
        cls.doraidc = tiles[rinshan : 10 + rinshan : 2]
        cls.udoraidc = tiles[rinshan + 1 : 10 + rinshan + 1 : 2]
        cls.rinshan = tiles[:rinshan]

    @classmethod
    def gethaipai(cls, p: int = 4, n: int = 13) -> List[List[_TL]]:
        if not cls.is_setted:
            cls.setyama()
        haipais = [[] for _ in range(p)]
        for k in range(n // 4 * p):
            for _ in range(4):
                haipais[k % p].append(cls.yama.pop())
        for k in range(p):
            for _ in range(n % 4):
                haipais[k % p].append(cls.yama.pop())
        return haipais

    @classmethod
    def gettsumo(cls) -> _TL:
        if not cls.is_setted:
            cls.setyama()
        if len(cls.yama) > cls.idc_open:
            return cls.yama.pop()
        else:
            return None

    @classmethod
    def kan(cls) -> _TL:
        if not cls.is_setted:
            cls.setyama()
        if len(cls.yama) > cls.idc_open:
            cls.idc_open += 1
            return cls.doraidc[cls.idc_open]

    @classmethod
    def getrinshan(cls) -> _TL:
        if not cls.is_setted:
            cls.setyama()
        if len(cls.yama) > cls.idc_open:
            return cls.rinshan.pop(0)
        else:
            return None
