from enum import IntEnum


class Player(IntEnum):
    OYA = 3
    KO = 2

    KOKO = KO << KO
    OYAKO = OYA << KO
    KOOYA = KO << OYA
