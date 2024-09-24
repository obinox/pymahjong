from collections import Counter
from typing import List, Self

from ichihime.Category import Category
from ichihime.Machi import Machi
from ichihime.Test import TenpaiTest
from ichihime.Tile import Tile


class Tenpai:
    def __init__(self, tile: Tile, machi: Machi) -> None:
        self.tile = Tile(tile)
        self.machi = Machi(machi)

    def __repr__(self) -> str:
        return f"<{repr(self.tile)}: {repr(self.machi)}>"

    def __int__(self) -> int:
        return self.tile * 10 + self.machi

    def __hash__(self) -> int:
        return hash(int(self))

    def __eq__(self, value: object) -> bool:
        return hash(self) == hash(value)

    @staticmethod
    def getTenpai(tefuda: List[Tile] | TenpaiTest | str) -> List[Self]:
        if type(tefuda) == TenpaiTest:
            tefuda = tefuda.value
        elif type(tefuda) == str:
            tefuda = TenpaiTest.toTile(tefuda)
        stack = []
        groups = [[], [], [], [], []]
        target: List[Tile]
        sub: List[Tile]
        wait = []
        shapon = []
        out = []

        ## prepare stack
        for t in tefuda:
            groups[t.group].append(t)
        for g in groups:
            stack.append(sorted(g))

        count = Counter(tefuda)
        if list(count.values()).count(2) == 6:
            wait.append(Tenpai(sorted(count.items(), key=lambda x: x[1])[0][0], Machi.CHI))
        elif Category.allIn(tefuda, Category.YAOCHUUHAI):
            if len(list(count.keys())) == 12:
                wait.append(
                    Tenpai(
                        [x for x in Category.YAOCHUUHAI if not tefuda.count(x)][0],
                        Machi.KMU,
                    )
                )
            elif len(list(count.keys())) == 13:
                for i in range(13):
                    wait.append(Tenpai(Category.YAOCHUUHAI[i], Machi.K13))

        ## recursion
        while stack:
            target = stack.pop()
            target.sort()
            sub = []
            match len(target):
                case 0:
                    pass
                case 1:
                    wait.append(Tenpai(target[0], Machi.TAN))
                case 2:
                    match target[1] - target[0]:
                        case 0:
                            shapon.append(Tenpai(target[0], Machi.SHP))
                        case 1:
                            if target[0].actual != 0:
                                if target[0].actual == 1:
                                    wait.append(Tenpai(target[0] + 2, Machi.PN3))
                                elif target[1].actual == 9:
                                    wait.append(Tenpai(target[0] - 1, Machi.PN7))
                                else:
                                    wait.append(Tenpai(target[0] - 1, Machi.RML))
                                    wait.append(Tenpai(target[0] + 2, Machi.RMR))
                        case 2:
                            if target[0].actual != 0:
                                wait.append(Tenpai(target[0] + 1, Machi.KAN))
                case x:
                    if x == 4:
                        for i in range(3):
                            sub = []
                            if target.count(target[i]) >= 2:
                                sub = sorted(target)
                                sub.remove(target[i])
                                sub.remove(target[i])
                                stack.append(sub)
                    for i in range(x - 2):
                        sub = []
                        if target.count(target[i]) >= 3:
                            sub = sorted(target)
                            sub.remove(target[i])
                            sub.remove(target[i])
                            sub.remove(target[i])
                            stack.append(sub)
                        if target.count(target[i]) >= 1 and target.count(target[i] + 1) >= 1 and target.count(target[i] + 2) >= 1:
                            if target[0].actual != 0:
                                sub = sorted(target)
                                sub.remove(target[i])
                                sub.remove(target[i] + 1)
                                sub.remove(target[i] + 2)
                                stack.append(sub)
        wait = list(set(wait))
        shapon = list(set(shapon))
        out: List[Tenpai] = list(set(wait)) + (list(set(shapon)) if len(shapon) >= 2 else [])
        out.sort(key=lambda x: x.tile)
        return out
