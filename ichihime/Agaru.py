from enum import IntEnum
from typing import Literal


class Agaru(IntEnum):
    TSUMO = 0x00, "tsumo"
    RON = 0x04, "ron"

    DABURI = 0x20, "double riichi"
    RIICHI = 0x10, "riichi"
    IPPATSU = 0x08, "ippatsu"

    HAITEI = 0x02, "haitei"
    HOUTEI = 0x06, "houtei"
    CHANKAN = 0x05, "chankan"
    RINSHAN = 0x01, "rinshan"

    #       0x00             0x10            0x20
    # 0x00  tsumo            RCH SMO         DRI SMO
    # 0x01  rinshan  (tsumo) RCH RIN SMO     DRI RIN SMO
    # 0x02  haitei   (tsumo) RCH HAI SMO     DRI HAI SMO
    # 0x03  x                x               x
    # 0x04  ron              RCH             DRI
    # 0x05  chankan    (ron) RCH CHK         x     (chankan)
    # 0x06  houtei     (ron) RCH HOU         DRI HOU
    # 0x07  x                x               x
    # 0x08  x (ippatsu nomi) RCH IPP SMO     DRI IPP SMO
    # 0x09  x                x     (rinshan) x     (rinshan)
    # 0x0a  x                RCH IPP HAI SMO x  (impossible)
    # 0x0b  x                x               x
    # 0x0c  x                RCH IPP         DRI IPP
    # 0x0d  x                RCH IPP CHK     x     (chankan)
    # 0x0e  x                x      (houtei) x      (houtei)
    # 0x0f  x                x               x

    def __new__(cls, value: int, string: str):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.string = string
        return obj

    def __init__(self, value: int, string: str) -> None:
        self._value_ = value
        self.string: str

    @staticmethod
    def rental(
        tsumo: bool = True,
        riichi: Literal[0, 1, 2] = 0,
        aru: Literal[0, 1, 2] = 0,
        ippatsu: bool = False,
    ) -> int:
        possibility = [
            Agaru.TSUMO,
            Agaru.RINSHAN,
            Agaru.HAITEI,
            Agaru.RON,
            Agaru.CHANKAN,
            Agaru.HOUTEI,
            Agaru.RIICHI + Agaru.TSUMO,
            Agaru.RIICHI + Agaru.RINSHAN,
            Agaru.RIICHI + Agaru.HAITEI,
            Agaru.RIICHI + Agaru.RON,
            Agaru.RIICHI + Agaru.CHANKAN,
            Agaru.RIICHI + Agaru.HOUTEI,
            Agaru.RIICHI + Agaru.IPPATSU + Agaru.TSUMO,
            Agaru.RIICHI + Agaru.IPPATSU + Agaru.HAITEI,
            Agaru.RIICHI + Agaru.IPPATSU + Agaru.RON,
            Agaru.RIICHI + Agaru.IPPATSU + Agaru.CHANKAN,
            Agaru.DABURI + Agaru.TSUMO,
            Agaru.DABURI + Agaru.RINSHAN,
            Agaru.DABURI + Agaru.HAITEI,
            Agaru.DABURI + Agaru.RON,
            Agaru.DABURI + Agaru.HOUTEI,
            Agaru.DABURI + Agaru.IPPATSU + Agaru.TSUMO,
            Agaru.DABURI + Agaru.IPPATSU + Agaru.RON,
        ]
        out = Agaru.RIICHI * riichi + Agaru.IPPATSU * ippatsu + Agaru.TSUMO * tsumo + aru

        return out if out in possibility else None
