from collections import Counter
from typing import List, Self

from ichihime.enums import cat as _CT
from ichihime.enums import machi as _MC
from ichihime.enums import mentsu as _MT
from ichihime.enums import tile as _TL
from ichihime.test import testblock as _TB


class tenpai:
    __slots__ = ("tile", "machi")

    def __init__(self, tile: _TL, machi: _MC) -> None:
        self.tile = _TL(tile)
        self.machi = _MC(machi)

    def __repr__(self) -> str:
        return f"{self.tile.name}: {self.machi.name}"  # f"{self.__class__.__name__}(0x{self.tile:0>2x}, 0x{self.machi:0>2x})"

    def __str__(self) -> str:
        return f"{self.tile.name} {self.machi.name}"

    def __int__(self) -> int:
        return self.tile + self.machi * 0x100

    def __hash__(self) -> int:
        return hash(int(self))

    def __eq__(self, value: object) -> bool:
        return self.__hash__() == value.__hash__()

    @staticmethod
    def getTenpai(tefuda: List[_TL] | _TB | str) -> List[Self]:
        if type(tefuda) == _TB:
            tefuda = tefuda.value
        elif type(tefuda) == str:
            tefuda = _TB.toTile(tefuda)
        stack = []
        groups = [[], [], [], [], []]
        target: List[_TL]
        sub: List[_TL]
        wait = []
        aka = []
        shapon = []
        out: List[tenpai] = []
        akaout: List[tenpai] = []

        ## prepare stack
        tefuda = list(tefuda)
        for i, t in enumerate(tefuda):
            if t in _CT.AKAPAI:
                aka.append(t)
                tefuda[i] = _TL(t - _MT.AKA)
        for t in tefuda:
            groups[t.group].append(t)
        for g in groups:
            stack.append(sorted(g))

        count = Counter(tefuda)
        if list(count.values()).count(2) == 6:
            wait.append(tenpai(sorted(count.items(), key=lambda x: x[1])[0][0], _MC.CHI))
        elif _CT.allIn(tefuda, _CT.YAOCHUUHAI):
            if len(list(count.keys())) == 12:
                wait.append(
                    tenpai(
                        [x for x in _CT.YAOCHUUHAI if not tefuda.count(x)][0],
                        _MC.KMU,
                    )
                )
            elif len(list(count.keys())) == 13:
                for i in range(13):
                    wait.append(tenpai(_CT.YAOCHUUHAI[i], _MC.K13))

        ## recursion
        while stack:
            target = stack.pop()
            target.sort()
            sub = []
            match len(target):
                case 0:
                    pass
                case 1:
                    wait.append(tenpai(target[0], _MC.TAN))
                case 2:
                    match target[1] - target[0]:
                        case 0:
                            shapon.append(tenpai(target[0], _MC.SHP))
                        case 1:
                            if target[0] not in _CT.JIHAI:
                                if target[0].actual == 1:
                                    wait.append(tenpai(target[0] + 2, _MC.PN3))
                                elif target[1].actual == 9:
                                    wait.append(tenpai(target[0] - 1, _MC.PN7))
                                else:
                                    wait.append(tenpai(target[0] - 1, _MC.RML))
                                    wait.append(tenpai(target[0] + 2, _MC.RMR))
                        case 2:
                            if target[0] not in _CT.JIHAI:
                                wait.append(tenpai(target[0] + 1, _MC.KAN))
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
                            if target[0] not in _CT.JIHAI:
                                sub = sorted(target)
                                sub.remove(target[i])
                                sub.remove(target[i] + 1)
                                sub.remove(target[i] + 2)
                                stack.append(sub)
        wait = list(set(wait))
        shapon = list(set(shapon))
        out = list(set(wait)) + (list(set(shapon)) if len(shapon) >= 2 else [])
        for o in out:
            if o.tile.actual == 5 and _TL(o.tile + _MT.AKA) not in aka:
                akaout.append(tenpai(_TL(o.tile + _MT.AKA), o.machi))
        out += akaout
        out.sort(key=lambda x: x.tile)
        return out
