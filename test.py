from enum import Enum

from ichihime.enums import *
from ichihime.src import *
from ichihime.test import testblock
from ichihime.yakus import dora

# oya = 3
# ko = 2
# print(ko << ko)
# print(ko << oya)
# print(oya << ko)
# print(f"{ko}:ko {oya}:oya")
yama.setyama()
# print(yama.tiles)
# print(yama.yama)
print(yama.doraidc)
# print(yama.udoraidc)
# print(yama.rinshan)
# a = yama.gethaipai()
# print(a)
# print(base.__str__())


ba = tile.NANN
ji = tile.SHAA
s6 = "p1p2p3p4p1p2p3p4p1p2p3p4p5"
b1 = blocks.getBlocks(testblock.toTile(s6), ba, ji, tenpai.getTenpai(s6)[0], agari.by_int(32))[0]

a1 = dora()
a2 = dora()
print([a1, a2])
print(id(a1), id(a2))
a1.check(b1, yama)
