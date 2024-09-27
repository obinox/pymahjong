import random as rand
from collections import Counter
from typing import List, Literal, Self, Tuple

from ichihime.Enum.Agaru import Agaru
from ichihime.Enum.Category import Category
from ichihime.Enum.Machi import Machi
from ichihime.Enum.Mentsu import Mentsu
from ichihime.Enum.Tile import Tile
from ichihime.src.Agari import Agari
from ichihime.src.Tenpai import Tenpai


class Block:
    _mentsu = []
    _toitsu = []

    @classmethod
    def rdInit(cls) -> None:
        for _i in range(0, 3):
            for _c in range(1, 8):
                for _ in range(4):
                    cls._mentsu.append(0x10 * _i + _c)
        for _i in Tile:
            cls._mentsu.append(Mentsu.KOUTSU + _i.value)
            cls._toitsu.append(Mentsu.TOITSU + _i.value)

    @classmethod
    def rdBlock(cls) -> tuple[List[Tile], Tile]:
        cls.rdInit()
        mentsu = sorted(cls._mentsu)
        toitsu = sorted(cls._toitsu)
        n = 0
        blocks = []
        const = []
        for i in range(4):
            n = mentsu[rand.randint(0, len(mentsu) - 1)]
            const.append(n)
            if n > Mentsu.KOUTSU:
                blocks.append((Tile(n % 0x40), Tile(n % 0x40), Tile(n % 0x40)))
                mentsu.remove(n)
                for i in range(9):
                    try:
                        mentsu.remove(n % 0x40 - i % 3)
                    except:
                        pass
                try:
                    toitsu.remove(n % 0x40 + Mentsu.TOITSU)
                except:
                    pass
            else:
                blocks.append((Tile(n + 0x00), Tile(n + 0x01), Tile(n + 0x02)))
                for i in range(3):
                    try:
                        mentsu.remove(n + i)
                    except:
                        pass
                for i in range(3):
                    if mentsu.count(n - i) < 3:
                        try:
                            mentsu.remove(n + 0x40 - i)
                        except:
                            pass
                        try:
                            mentsu.remove(n + 0x41 - i)
                        except:
                            pass
                        try:
                            mentsu.remove(n + 0x42 - i)
                        except:
                            pass
                    if mentsu.count(n - i) < 2:
                        try:
                            toitsu.remove(n % 0x40 + Mentsu.TOITSU)
                        except:
                            pass
        n = toitsu[rand.randint(0, len(toitsu) - 1)]
        const.append(n)
        blocks.append((Tile(n % 0x40), Tile(n % 0x40)))
        try:
            toitsu.remove(n)
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
        bakaze: Literal[Tile.TON, Tile.NAN, Tile.SHAA, Tile.PEI] = Tile.TON,
        jikaze: Literal[Tile.TON, Tile.NAN, Tile.SHAA, Tile.PEI] = Tile.TON,
        tenpai: Tenpai = None,
        agari: Agari = Agari(),
        remain: List[Tile] = None,
    ) -> None:
        self.jantou = jantou
        self.mentsu = sorted(mentsu)
        self.blocks = [self.jantou, *self.mentsu]
        self.remain = remain
        self.bakaze = bakaze
        self.jikaze = jikaze
        self.tenpai = tenpai
        self.agari = agari

    # TODO
    def __hash__(self) -> int:
        return int(str(self), 16)

    def __eq__(self, value: object) -> bool:
        return self.__hash__() == value.__hash__()

    def __str__(self) -> str:
        wind = f"{(self.bakaze - Tile.TON) * 0x04 + (self.jikaze - Tile.TON):x}"
        if self.jantou >= Mentsu.KOKUSHI:
            return wind + f"{hash(self.tenpai):0>2x}" + f"{hash(self.agari):0>2x}" + "".join([f"{x:x}" for x in self.blocks])
        elif self.jantou >= Mentsu.CHIITOI:
            return wind + f"{hash(self.tenpai):0>2x}" + f"{hash(self.agari):0>2x}" + "".join([f"{x:0>2x}" for x in self.blocks])
        else:
            return wind + f"{hash(self.tenpai):0>2x}" + f"{hash(self.agari):0>2x}" + "".join([f"{x:0>3x}" for x in self.blocks])

    def __repr__(self) -> str:
        return self.blocks.__str__()

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
    def getBlocks(
        tefuda: List[Tile],
        bakaze: Literal[Tile.TON, Tile.NAN, Tile.SHAA, Tile.PEI],
        jikaze: Literal[Tile.TON, Tile.NAN, Tile.SHAA, Tile.PEI],
        tenpai: Tenpai,
        agari: Agari = Agari(),
    ):
        stack: List[Block] = []
        target: Block
        sub: List[Tile]
        out = []
        jantou: int
        chiitoi: List[int] = []
        mentsu: int
        counts = List[Tuple[Tile, int]]
        info = {"bakaze": bakaze, "jikaze": jikaze, "tenpai": tenpai, "agari": agari}
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
                stack.append(Block(None, *[mentsu], remain=sub, **info))
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
                stack.append(Block(None, *[mentsu], remain=sub, **info))
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
                stack.append(Block(None, *[mentsu], remain=sub, **info))
            case Machi.SHP:
                t = Tile(tenpai.tile)
                mentsu = t.value + Mentsu.KOUTSU
                sub.remove(t)
                sub.remove(t)
                sub.remove(t)
                stack.append(Block(None, *[mentsu], remain=sub, **info))
            case Machi.TAN:
                t = Tile(tenpai.tile)
                jantou = t.value + Mentsu.TOITSU
                sub.remove(t)
                sub.remove(t)
                stack.append(Block(jantou, *[], remain=sub, **info))
            case Machi.CHI:
                t = Tile(tenpai.tile)
                chiitoi.append(t.value + Mentsu.TOITSU + Mentsu.CHIITOI)
                sub.remove(t)
                sub.remove(t)
                for i in range(6):
                    t0 = Tile(sub[2 * i])
                    chiitoi.append(t0.value)
                stack.append(Block(chiitoi[0], *chiitoi[1:], remain=None, **info))
            case Machi.KMU | Machi.K13:
                for i in range(13):
                    t = Tile(Category.YAOCHUUHAI[i])
                    if sub.count(t) == 2:
                        jantou = i + Category.YAOCHUUHAI.index(tenpai.tile) * 0x10 + Mentsu.KOKUSHI
                        sub.remove(t)
                        sub.remove(t)
                stack.append(Block(jantou, *[Category.YAOCHUUHAI.index(x) for x in sub], remain=None, **info))

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
                            stack.append(Block(jantou, *target.mentsu, remain=sub, **info))
                else:
                    for t, c in counts:
                        if c >= 3:
                            mentsu = t.value + Mentsu.KOUTSU
                            sub = sorted(target.remain)
                            sub.remove(t)
                            sub.remove(t)
                            sub.remove(t)
                            stack.append(Block(jantou, *sorted(target.mentsu + [mentsu]), remain=sub, **info))
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
                            stack.append(Block(jantou, *sorted(target.mentsu + [mentsu]), remain=sub, **info))
        out = list(set(out))
        out.sort()
        return out
