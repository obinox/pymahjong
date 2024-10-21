import random as rand
from collections import Counter
from typing import List, Literal, Tuple

from ichihime.enums import block as _BL
from ichihime.enums import cat as _CT
from ichihime.enums import machi as _MC
from ichihime.enums import mentsu as _MT
from ichihime.enums import tile as _TL
from ichihime.src import agari as _ARI
from ichihime.src import tenpai as _TP


class blocks:
    __slots__ = ("jantou", "mentsu", "blocks", "remain", "bakaze", "jikaze", "tenpai", "agari", "nuki")
    __mentsu = []
    __toitsu = []

    @classmethod
    def rdInit(cls) -> None:
        for _i in range(0, 3):
            for _c in range(1, 8):
                for _ in range(4):
                    cls.__mentsu.append(0x10 * _i + _c)
        for _i in _TL:
            cls.__mentsu.append(_MT.KOUTSU + _i.value)
            cls.__toitsu.append(_MT.TOITSU + _i.value)

    @classmethod
    def rdBlock(cls) -> tuple[List[_TL], _TL]:
        cls.rdInit()
        mentsu = sorted(cls.__mentsu)
        toitsu = sorted(cls.__toitsu)
        n = 0
        blocks = []
        const = []
        for i in range(4):
            n = mentsu[rand.randint(0, len(mentsu) - 1)]
            const.append(n)
            if n > _MT.KOUTSU:
                blocks.append((_TL(n % 0x40), _TL(n % 0x40), _TL(n % 0x40)))
                mentsu.remove(n)
                for i in range(9):
                    try:
                        mentsu.remove(n % 0x40 - i % 3)
                    except:
                        pass
                try:
                    toitsu.remove(n % 0x40 + _MT.TOITSU)
                except:
                    pass
            else:
                blocks.append((_TL(n + 0x00), _TL(n + 0x01), _TL(n + 0x02)))
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
                            toitsu.remove(n % 0x40 + _MT.TOITSU)
                        except:
                            pass
        n = toitsu[rand.randint(0, len(toitsu) - 1)]
        const.append(n)
        blocks.append((_TL(n % 0x40), _TL(n % 0x40)))
        try:
            toitsu.remove(n)
        except:
            pass

        tefuda: List[_TL] = list(sum(blocks, ()))
        tefuda.sort()

        agari = tefuda.pop(rand.randint(0, len(tefuda) - 1))
        # print(tefuda, repr(agari))

        return tefuda, agari, const

    def __init__(
        self,
        jantou: _BL | None,
        *mentsu: _BL,
        bakaze: Literal[_TL.TONN, _TL.NANN, _TL.SHAA, _TL.PEII] = _TL.TONN,
        jikaze: Literal[_TL.TONN, _TL.NANN, _TL.SHAA, _TL.PEII] = _TL.TONN,
        tenpai: _TP = None,
        agari: _ARI = _ARI(),
        nuki: int = 0,
        remain: List[_TL] = None,
    ) -> None:
        self.jantou = jantou
        self.mentsu = sorted(mentsu)
        self.blocks: List[_BL] = [self.jantou, *self.mentsu]
        self.remain = remain
        self.bakaze = bakaze
        self.jikaze = jikaze
        self.tenpai = tenpai
        self.agari = agari
        self.nuki = nuki

    # TODO
    def __hash__(self) -> int:
        return int(str(self), 16)

    def __eq__(self, value: object) -> bool:
        return self.__hash__() == value.__hash__()

    def __str__(self) -> str:
        wind = f"{(self.bakaze - _TL.TONN) * 0x04 + (self.jikaze - _TL.TONN):x}"
        if self.tenpai.machi == _MC.KMU or self.tenpai.machi == _MC.K13:
            return (
                wind
                + f"{hash(self.tenpai):0>3x}"
                + f"{hash(self.agari):0>2x}"
                + "".join([f"{_CT.YAOCHUUHAI.index(x - _MT.KOKUSHI):x}" for x in self.blocks])
                + str(self.nuki)
            )
        elif self.tenpai.machi == _MC.CHI:
            return wind + f"{hash(self.tenpai):0>3x}" + f"{hash(self.agari):0>2x}" + "".join([f"{x:0>2x}" for x in self.blocks]) + str(self.nuki)
        else:
            return wind + f"{hash(self.tenpai):0>3x}" + f"{hash(self.agari):0>2x}" + "".join([f"{x:0>3x}" for x in self.blocks])[1:] + str(self.nuki)

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
        tiles: List[_TL],
        bakaze: Literal[_TL.TONN, _TL.NANN, _TL.SHAA, _TL.PEII],
        jikaze: Literal[_TL.TONN, _TL.NANN, _TL.SHAA, _TL.PEII],
        tenpai: _TP,
        fuuros: List[_BL] = [],
        agari: _ARI = _ARI(),
        nuki: int = 0,
    ):
        stack: List[blocks] = []
        target: blocks
        sub: List[_TL]
        out: List[blocks] = []
        jantou: int
        chiitoi: List[int] = []
        mentsu: int
        counts = List[Tuple[_TL, int]]
        aka: List[_TL] = []
        info = {"bakaze": bakaze, "jikaze": jikaze, "tenpai": tenpai, "agari": agari, "nuki": nuki}

        ## prepare stack
        tenpaitile = tenpai.tile
        if tenpaitile in _CT.AKAPAI:
            aka.append(tenpaitile)
            tenpaitile = _TL(tenpaitile - _MT.AKA)

        sub = sorted(list(tiles) + [tenpaitile])

        for i, t in enumerate(sub):
            if t in _CT.AKAPAI:
                aka.append(t)
                sub[i] = _TL(t - _MT.AKA)
        sub.sort()

        match tenpai.machi:
            case _MC.RML | _MC.PN7:
                mentsu = _BL(_TL(tenpaitile) + _MT.SHUNTSH)
                for t in mentsu:
                    sub.remove(t)
                stack.append(blocks(None, *[mentsu], remain=sub, **info))
            case _MC.RMR | _MC.PN3:
                mentsu = _BL(_TL(tenpaitile - 2) + _MT.SHUNTSH)
                for t in mentsu:
                    sub.remove(t)
                stack.append(blocks(None, *[mentsu], remain=sub, **info))
            case _MC.KAN:
                mentsu = _BL(_TL(tenpaitile - 1) + _MT.SHUNTSH)
                for t in mentsu:
                    sub.remove(t)
                stack.append(blocks(None, *[mentsu], remain=sub, **info))
            case _MC.SHP:
                mentsu = _BL(_TL(tenpaitile) + _MT.KOUTSU)
                for t in mentsu:
                    sub.remove(t)
                stack.append(blocks(None, *[mentsu], remain=sub, **info))
            case _MC.TAN:
                jantou = _BL(_TL(tenpaitile) + _MT.TOITSU)
                for t in jantou:
                    sub.remove(t)
                stack.append(blocks(jantou, *[], remain=sub, **info))
            case _MC.CHI:
                jantou = _BL(_TL(tenpaitile) + _MT.TOITSU)
                for t in jantou:
                    sub.remove(t)
                for i in range(6):
                    t = _TL(sub[2 * i])
                    chiitoi.append(_BL(_TL(t) + _MT.TOITSU))
                stack.append(blocks(jantou, *chiitoi, remain=None, **info))
            case _MC.KMU | _MC.K13:
                jantou = _BL(_TL(tenpaitile) + _MT.KOKUSHI)
                for t in jantou:
                    sub.remove(t)
                stack.append(blocks(jantou, *map(lambda x: _BL(x + _MT.KOKUSHI), sub), remain=None, **info))

        while stack:
            target = stack.pop()
            if target.remain == None or len(target.remain) == 0:
                out.append(target)
                continue
            else:
                counts = Counter(target.remain).most_common()
                if target.jantou == None:
                    for t0, c in counts:
                        if c >= 2:
                            jantou = _BL(_TL(t0) + _MT.TOITSU)
                            sub = sorted(target.remain)
                            for t in jantou:
                                sub.remove(t)
                            stack.append(blocks(jantou, *target.mentsu, remain=sub, **info))
                else:
                    for t0, c in counts:
                        if c >= 3:
                            mentsu = _BL(_TL(t0) + _MT.KOUTSU)
                            sub = sorted(target.remain)
                            for t in mentsu:
                                sub.remove(t)
                            stack.append(blocks(target.jantou, *sorted(target.mentsu + [mentsu]), remain=sub, **info))
                    for t0, c in counts:
                        if c >= 1 and target.remain.count(t0 + 1) >= 1 and target.remain.count(t0 + 2) >= 1:
                            mentsu = _BL(_TL(t0) + _MT.SHUNTSH)
                            sub = sorted(target.remain)
                            for t in mentsu:
                                sub.remove(t)
                            stack.append(blocks(target.jantou, *sorted(target.mentsu + [mentsu]), remain=sub, **info))
        out = list(set(out))
        if len(aka) > 0:
            for oi, bs in enumerate(out):
                for a in aka:
                    for i, b in enumerate(bs.blocks):
                        if _CT.getCat(a)[0][4] in b.tiles:
                            out[oi].blocks[i] = _BL(bs.blocks[i] + _MT.AKA)
                            break
        out.sort()
        return out

    def is_menzen(self) -> bool:
        return True
