from typing import Literal, Self

from ichihime.Agaru import Agaru


class Agari:
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

    def __init__(
        self,
        tsumo: Literal[Agaru.TSUMO, Agaru.RON] = Agaru.TSUMO,
        riichi: Literal[None, Agaru.RIICHI, Agaru.DABURI] = None,
        aru: Literal[None, Agaru.RINSHAN, Agaru.CHANKAN, Agaru.HAITEI, Agaru.HOUTEI] = None,
        ippatsu: Literal[None, Agaru.IPPATSU] = None,
    ) -> None:
        if tuple([tsumo, riichi, aru, ippatsu]) in Agari.possibility:
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
        return f"{self.__hash__():0>2x}"

    @classmethod
    def by_int(cls, n) -> Self:
        tsumo = Agaru.TSUMO if n // Agaru.RON % 2 == 0 else Agaru.RON
        riichi = Agaru.DABURI if n // Agaru.RIICHI == 2 else Agaru.RIICHI if n // Agaru.RIICHI == 1 else None
        aru = Agaru(n % Agaru.IPPATSU) if n % Agaru.IPPATSU in {Agaru.RINSHAN, Agaru.CHANKAN, Agaru.HAITEI, Agaru.HOUTEI} else None
        ippatsu = Agaru.IPPATSU if n // Agaru.IPPATSU % 2 == 1 else None
        return Agari(tsumo, riichi, aru, ippatsu)
