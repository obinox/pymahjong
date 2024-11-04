from typing import Literal, Self

from ichihime.enums import agaru as _ARU


class agari:
    __slots__ = ("tsumo", "riichi", "aru", "ippatsu")

    #       0x00             0x10            0x20
    # 0x00  tsumo            RII SMO         DRI SMO
    # 0x01  rinshan  (tsumo) RII RIN SMO     DRI RIN SMO
    # 0x02  haitei   (tsumo) RII HAI SMO     DRI HAI SMO
    # 0x03  x                x               x
    # 0x04  ron              RII             DRI
    # 0x05  chankan    (ron) RII CHK         x     (chankan) -> valid from kokushi
    # 0x06  houtei     (ron) RII HOU         DRI HOU
    # 0x07  x                x               x
    # 0x08  x (ippatsu nomi) RII IPP SMO     DRI IPP SMO
    # 0x09  x                x     (rinshan) x     (rinshan)
    # 0x0a  x                RII IPP HAI SMO x  (impossible)
    # 0x0b  x                x               x
    # 0x0c  x                RII IPP         DRI IPP
    # 0x0d  x                RII IPP CHK     x     (chankan) -> valid from kokushi
    # 0x0e  x                x      (houtei) x      (houtei)
    # 0x0f  x                x               x
    possibility = [
        (_ARU.TSUMO, None, None, None),
        (_ARU.TSUMO, None, _ARU.RINSHAN, None),
        (_ARU.TSUMO, None, _ARU.HAITEI, None),
        (_ARU.RON, None, None, None),
        (_ARU.RON, None, _ARU.CHANKAN, None),
        (_ARU.RON, None, _ARU.HOUTEI, None),
        (_ARU.TSUMO, _ARU.RIICHI, None, None),
        (_ARU.TSUMO, _ARU.RIICHI, _ARU.RINSHAN, None),
        (_ARU.TSUMO, _ARU.RIICHI, _ARU.HAITEI, None),
        (_ARU.RON, _ARU.RIICHI, None, None),
        (_ARU.RON, _ARU.RIICHI, _ARU.CHANKAN, None),
        (_ARU.RON, _ARU.RIICHI, _ARU.HOUTEI, None),
        (_ARU.TSUMO, _ARU.RIICHI, None, _ARU.IPPATSU),
        (_ARU.TSUMO, _ARU.RIICHI, _ARU.HAITEI, _ARU.IPPATSU),
        (_ARU.RON, _ARU.RIICHI, None, _ARU.IPPATSU),
        (_ARU.RON, _ARU.RIICHI, _ARU.CHANKAN, _ARU.IPPATSU),
        (_ARU.TSUMO, _ARU.DABURI, None, None),
        (_ARU.TSUMO, _ARU.DABURI, _ARU.RINSHAN, None),
        (_ARU.TSUMO, _ARU.DABURI, _ARU.HAITEI, None),
        (_ARU.RON, _ARU.DABURI, None, None),
        (_ARU.RON, _ARU.DABURI, _ARU.HOUTEI, None),
        (_ARU.TSUMO, _ARU.DABURI, None, _ARU.IPPATSU),
        (_ARU.RON, _ARU.DABURI, None, _ARU.IPPATSU),
    ]
    kokushi = [  # kokushi only
        (_ARU.RON, _ARU.DABURI, _ARU.CHANKAN, None),
        (_ARU.RON, _ARU.DABURI, _ARU.CHANKAN, _ARU.IPPATSU),
    ]

    def __init__(
        self,
        tsumo: Literal[_ARU.TSUMO, _ARU.RON] = _ARU.TSUMO,
        riichi: Literal[None, _ARU.RIICHI, _ARU.DABURI, _ARU.OPENRI, _ARU.OPENDABURI] = None,
        aru: Literal[None, _ARU.RINSHAN, _ARU.CHANKAN, _ARU.HAITEI, _ARU.HOUTEI] = None,
        ippatsu: Literal[None, _ARU.IPPATSU] = None,
        kokushi: bool = False,
    ) -> None:
        if tuple([tsumo, riichi, aru, ippatsu]) in agari.possibility:
            self.tsumo = tsumo
            self.riichi = riichi
            self.aru = aru
            self.ippatsu = ippatsu
        elif tuple([tsumo, riichi, aru, ippatsu]) in agari.kokushi and kokushi:
            self.tsumo = tsumo
            self.riichi = riichi
            self.aru = aru
            self.ippatsu = ippatsu
        else:
            raise ValueError

    def __hash__(self) -> int:
        if self.aru:
            return self.riichi if self.riichi else 0 + self.aru if self.aru else 0 + self.ippatsu if self.ippatsu else 0
        else:
            return self.tsumo + self.riichi if self.riichi else 0 + self.ippatsu if self.ippatsu else 0

    def __eq__(self, value: object) -> bool:
        return self.__hash__() == value.__hash__()

    def __int__(self) -> int:
        return self.__hash__()

    def __str__(self) -> str:
        return f"[{" ".join(map(lambda x: x.name, filter(None, [self.tsumo, self.riichi, self.aru, self.ippatsu])))}{" KOKUSHI" if self.kokushi else ""}]"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(0x{self.__hash__():0>2x})"

    @classmethod
    def by_int(cls, n: int, kokushi: bool = False) -> Self:
        tsumo = _ARU.TSUMO if n // _ARU.RON % 2 == 0 else _ARU.RON
        riichi = _ARU.DABURI if n // _ARU.RIICHI == 2 else _ARU.RIICHI if n // _ARU.RIICHI == 1 else None
        aru = _ARU(n % _ARU.IPPATSU) if n % _ARU.IPPATSU in {_ARU.RINSHAN, _ARU.CHANKAN, _ARU.HAITEI, _ARU.HOUTEI} else None
        ippatsu = _ARU.IPPATSU if n // _ARU.IPPATSU % 2 == 1 else None
        return agari(tsumo, riichi, aru, ippatsu, kokushi)
