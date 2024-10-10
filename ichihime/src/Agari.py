from typing import Literal, Self

from ichihime.Enum.Agaru import Agaru


class Agari:
    __slots__ = ("tsumo", "riichi", "aru", "ippatsu")

    #       0x00             0x10            0x20
    # 0x00  tsumo            RCH SMO         DRI SMO
    # 0x01  rinshan  (tsumo) RCH RIN SMO     DRI RIN SMO
    # 0x02  haitei   (tsumo) RCH HAI SMO     DRI HAI SMO
    # 0x03  x                x               x
    # 0x04  ron              RCH             DRI
    # 0x05  chankan    (ron) RCH CHK         x     (chankan) -> valid from kokushi
    # 0x06  houtei     (ron) RCH HOU         DRI HOU
    # 0x07  x                x               x
    # 0x08  x (ippatsu nomi) RCH IPP SMO     DRI IPP SMO
    # 0x09  x                x     (rinshan) x     (rinshan)
    # 0x0a  x                RCH IPP HAI SMO x  (impossible)
    # 0x0b  x                x               x
    # 0x0c  x                RCH IPP         DRI IPP
    # 0x0d  x                RCH IPP CHK     x     (chankan) -> valid from kokushi
    # 0x0e  x                x      (houtei) x      (houtei)
    # 0x0f  x                x               x
    possibility = [
        (Agaru.TSUMO, None, None, None),
        (Agaru.TSUMO, None, Agaru.RINSHAN, None),
        (Agaru.TSUMO, None, Agaru.HAITEI, None),
        (Agaru.RON, None, None, None),
        (Agaru.RON, None, Agaru.CHANKAN, None),
        (Agaru.RON, None, Agaru.HOUTEI, None),
        (Agaru.TSUMO, Agaru.RIICHI, None, None),
        (Agaru.TSUMO, Agaru.RIICHI, Agaru.RINSHAN, None),
        (Agaru.TSUMO, Agaru.RIICHI, Agaru.HAITEI, None),
        (Agaru.RON, Agaru.RIICHI, None, None),
        (Agaru.RON, Agaru.RIICHI, Agaru.CHANKAN, None),
        (Agaru.RON, Agaru.RIICHI, Agaru.HOUTEI, None),
        (Agaru.TSUMO, Agaru.RIICHI, None, Agaru.IPPATSU),
        (Agaru.TSUMO, Agaru.RIICHI, Agaru.HAITEI, Agaru.IPPATSU),
        (Agaru.RON, Agaru.RIICHI, None, Agaru.IPPATSU),
        (Agaru.RON, Agaru.RIICHI, Agaru.CHANKAN, Agaru.IPPATSU),
        (Agaru.TSUMO, Agaru.DABURI, None, None),
        (Agaru.TSUMO, Agaru.DABURI, Agaru.RINSHAN, None),
        (Agaru.TSUMO, Agaru.DABURI, Agaru.HAITEI, None),
        (Agaru.RON, Agaru.DABURI, None, None),
        (Agaru.RON, Agaru.DABURI, Agaru.HOUTEI, None),
        (Agaru.TSUMO, Agaru.DABURI, None, Agaru.IPPATSU),
        (Agaru.RON, Agaru.DABURI, None, Agaru.IPPATSU),
    ]
    kokushi = [  # kokushi only
        (Agaru.RON, Agaru.DABURI, Agaru.CHANKAN, None),
        (Agaru.RON, Agaru.DABURI, Agaru.CHANKAN, Agaru.IPPATSU),
    ]

    def __init__(
        self,
        tsumo: Literal[Agaru.TSUMO, Agaru.RON] = Agaru.TSUMO,
        riichi: Literal[None, Agaru.RIICHI, Agaru.DABURI, Agaru.OPENRI, Agaru.OPENDABURI] = None,
        aru: Literal[None, Agaru.RINSHAN, Agaru.CHANKAN, Agaru.HAITEI, Agaru.HOUTEI] = None,
        ippatsu: Literal[None, Agaru.IPPATSU] = None,
        kokushi: bool = False,
    ) -> None:
        if tuple([tsumo, riichi, aru, ippatsu]) in Agari.possibility:
            self.tsumo = tsumo
            self.riichi = riichi
            self.aru = aru
            self.ippatsu = ippatsu
        elif tuple([tsumo, riichi, aru, ippatsu]) in Agari.kokushi and kokushi:
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
        tsumo = Agaru.TSUMO if n // Agaru.RON % 2 == 0 else Agaru.RON
        riichi = Agaru.DABURI if n // Agaru.RIICHI == 2 else Agaru.RIICHI if n // Agaru.RIICHI == 1 else None
        aru = Agaru(n % Agaru.IPPATSU) if n % Agaru.IPPATSU in {Agaru.RINSHAN, Agaru.CHANKAN, Agaru.HAITEI, Agaru.HOUTEI} else None
        ippatsu = Agaru.IPPATSU if n // Agaru.IPPATSU % 2 == 1 else None
        return Agari(tsumo, riichi, aru, ippatsu, kokushi)
