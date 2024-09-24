import random as rand
from collections import Counter
from enum import IntEnum
from typing import List, Self, Tuple

from ichihime.Agari import Agari
from ichihime.Agaru import Agaru
from ichihime.Category import Category
from ichihime.Machi import Machi
from ichihime.Tenpai import Tenpai
from ichihime.Tile import Tile


class Mentsu(IntEnum):
    SHUNTSH = 0x00, 0
    KOUTSU = 0x40, 4
    TOITSU = 0x80, 0
    KANTSU = 0xB0, 16

    MINJUN = 0x100, 0
    MINKOU = 0x140, 2
    KAKAN = 0x180, 8
    DAIMINKAN = 0x1B0, 8

    CHIITOI = 0x400, 25
    KOKUSHI = 0x800, 8

    def __new__(cls, value: int, fu: int) -> Self:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.fu = fu
        return obj

    def __init__(self, value: int, fu: int) -> None:
        self._value_ = value
        self.fu = fu


class Block:
    _mentsu = []
    _toitsu = []

    for _i in range(0, 3):
        for _c in range(1, 8):
            for _ in range(4):
                _mentsu.append(0x10 * _i + _c)
    for _i in Tile:
        _mentsu.append(Mentsu.KOUTSU + _i.value)
        _toitsu.append(Mentsu.TOITSU + _i.value)

    @classmethod
    def rdBlock(cls) -> tuple[List[Tile], Tile]:
        mentsu = sorted(cls._mentsu)
        toitsu = sorted(cls._toitsu)
        a = 0
        blocks = []
        const = []
        for i in range(4):
            a = mentsu[rand.randint(0, len(mentsu) - 1)]
            const.append(a)
            if a > Mentsu.KOUTSU:
                blocks.append((Tile(a % 0x40), Tile(a % 0x40), Tile(a % 0x40)))
                mentsu.remove(a)
                for i in range(9):
                    try:
                        mentsu.remove(a % 0x40 - i % 3)
                    except:
                        pass
                try:
                    toitsu.remove(a % 0x40 + Mentsu.TOITSU)
                except:
                    pass
            else:
                blocks.append((Tile(a + 0x00), Tile(a + 0x01), Tile(a + 0x02)))
                for i in range(3):
                    try:
                        mentsu.remove(a + i)
                    except:
                        pass
                for i in range(3):
                    if mentsu.count(a - i) < 3:
                        try:
                            mentsu.remove(a + 0x40 - i)
                        except:
                            pass
                        try:
                            mentsu.remove(a + 0x41 - i)
                        except:
                            pass
                        try:
                            mentsu.remove(a + 0x42 - i)
                        except:
                            pass
                    if mentsu.count(a - i) < 2:
                        try:
                            toitsu.remove(a % 0x40 + Mentsu.TOITSU)
                        except:
                            pass
        a = toitsu[rand.randint(0, len(toitsu) - 1)]
        const.append(a)
        blocks.append((Tile(a % 0x40), Tile(a % 0x40)))
        try:
            toitsu.remove(a)
        except:
            pass

        tefuda: List[Tile] = list(sum(blocks, ()))
        tefuda.sort()

        agari = tefuda.pop(rand.randint(0, len(tefuda) - 1))
        # print(tefuda, repr(agari))

        return tefuda, agari, const

    def __init__(
        self,
        jantou: int | None,
        *mentsu: int,
        remain: List[Tile] = None,
        tenpai: Tenpai = None,
        agari: Agari = Agari(),
    ) -> None:

        self.block = [jantou, *sorted(mentsu)]
        self.jantou = jantou
        self.mentsu = sorted(mentsu)
        self.remain = remain
        self.tenpai = tenpai
        self.agari = agari

    def __repr__(self) -> str:
        return self.block.__str__()

    # TODO
    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, value: object) -> bool:
        return self.__hash__() == value.__hash__()

    def __str__(self) -> str:
        if self.jantou >= Mentsu.KOKUSHI:
            return "0" + "".join([f"{x:x}" for x in self.block])
        elif self.jantou >= Mentsu.CHIITOI:
            return "0" + "".join([f"{x:0>2x}" for x in self.block])
        else:
            return str(self.agari) + "".join([f"{x:0>3x}" for x in self.block])[1:]

    def __int__(self) -> int:
        return int(str(self), 16)

    def __ne__(self, value: object) -> bool:
        return self.__hash__() != value.__hash__()

    def __lt__(self, value: object) -> bool:
        return int(self) < int(value)

    def __le__(self, value: object) -> bool:
        return int(self) <= int(value)

    def __gt__(self, value: object) -> bool:
        return int(self) > int(value)

    def __ge__(self, value: object) -> bool:
        return int(self) >= int(value)

    @staticmethod
    def getBlocks(tefuda: List[Tile], tenpai: Tenpai, agari: Agari = Agari()):
        stack: List[Block] = []
        target: Block
        sub: List[Tile]
        out = []
        jantou: int
        chiitoi: List[int] = []
        mentsu: int
        counts = List[Tuple[Tile, int]]
        ## prepare stack

        sub = sorted(list(tefuda) + [tenpai.tile])
        match tenpai.machi:
            case Machi.RML | Machi.PN7:
                t0, t1, t2 = (
                    Tile(tenpai.tile),
                    Tile(tenpai.tile + 1),
                    Tile(tenpai.tile + 2),
                )
                mentsu = t0.value + Mentsu.SHUNTSH
                sub.remove(t0)
                sub.remove(t1)
                sub.remove(t2)
                stack.append(Block(None, *[mentsu], remain=sub, tenpai=tenpai, agari=agari))
            case Machi.RMR | Machi.PN3:
                t0, t1, t2 = (
                    Tile(tenpai.tile - 2),
                    Tile(tenpai.tile - 1),
                    Tile(tenpai.tile),
                )
                mentsu = t0.value + Mentsu.SHUNTSH
                sub.remove(t0)
                sub.remove(t1)
                sub.remove(t2)
                stack.append(Block(None, *[mentsu], remain=sub, tenpai=tenpai, agari=agari))
            case Machi.KAN:
                t0, t1, t2 = (
                    Tile(tenpai.tile - 1),
                    Tile(tenpai.tile),
                    Tile(tenpai.tile + 1),
                )
                mentsu = t0.value + Mentsu.SHUNTSH
                sub.remove(t0)
                sub.remove(t1)
                sub.remove(t2)
                stack.append(Block(None, *[mentsu], remain=sub, tenpai=tenpai, agari=agari))
            case Machi.SHP:
                t = Tile(tenpai.tile)
                mentsu = t.value + Mentsu.KOUTSU
                sub.remove(t)
                sub.remove(t)
                sub.remove(t)
                stack.append(Block(None, *[mentsu], remain=sub, tenpai=tenpai, agari=agari))
            case Machi.TAN:
                t = Tile(tenpai.tile)
                jantou = t.value + Mentsu.TOITSU
                sub.remove(t)
                sub.remove(t)
                stack.append(Block(jantou, *[], remain=sub, tenpai=tenpai, agari=agari))
            case Machi.CHI:
                t = Tile(tenpai.tile)
                chiitoi.append(t.value + Mentsu.TOITSU + Mentsu.CHIITOI)
                sub.remove(t)
                sub.remove(t)
                for i in range(6):
                    t0 = Tile(sub[2 * i])
                    chiitoi.append(t0.value)
                stack.append(Block(chiitoi[0], *chiitoi[1:], remain=None, tenpai=tenpai, agari=agari))
            case Machi.KMU | Machi.K13:
                for i in range(13):
                    t = Tile(Category.YAOCHUUHAI[i])
                    if sub.count(t) == 2:
                        jantou = i + Category.YAOCHUUHAI.index(tenpai.tile) * 0x10 + Mentsu.KOKUSHI
                        sub.remove(t)
                        sub.remove(t)
                stack.append(Block(jantou, *[Category.YAOCHUUHAI.index(x) for x in sub], remain=None, tenpai=tenpai, agari=agari))
                del i

        while stack:
            target = stack.pop()
            if target.remain == None or len(target.remain) == 0:
                out.append(target)
                continue
            else:
                counts = Counter(target.remain).most_common()
                if target.jantou == None:
                    for t, c in counts:
                        if c >= 2:
                            jantou = t.value + Mentsu.TOITSU
                            sub = sorted(target.remain)
                            sub.remove(t)
                            sub.remove(t)
                            stack.append(Block(jantou, *target.mentsu, remain=sub, tenpai=tenpai, agari=agari))
                else:
                    for t, c in counts:
                        if c >= 3:
                            mentsu = t.value + Mentsu.KOUTSU
                            sub = sorted(target.remain)
                            sub.remove(t)
                            sub.remove(t)
                            sub.remove(t)
                            stack.append(Block(jantou, *sorted(target.mentsu + [mentsu]), remain=sub, tenpai=tenpai, agari=agari))
                    for t, c in counts:
                        if c >= 1 and target.remain.count(t + 1) >= 1 and target.remain.count(t + 2) >= 1:
                            t0, t1, t2 = (
                                Tile(t),
                                Tile(t + 1),
                                Tile(t + 2),
                            )
                            mentsu = t0.value + Mentsu.SHUNTSH
                            sub = sorted(target.remain)
                            sub.remove(t0)
                            sub.remove(t1)
                            sub.remove(t2)
                            stack.append(Block(jantou, *sorted(target.mentsu + [mentsu]), remain=sub, tenpai=tenpai, agari=agari))

        return sorted(list(set(out)))
        ## get Toitsu(head) not in Tanki machi.s
