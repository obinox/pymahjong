from enum import Enum

from ichihime.enums import *
from ichihime.src import *
from ichihime.test import testblock
from ichihime.yakus import *

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
print(yama.udoraidc)
# print(yama.udoraidc)
# print(yama.rinshan)
# a = yama.gethaipai()
# print(a)
# print(base.__str__())


ba = tile.NANN
ji = tile.SHAA
s6 = "p1p2p3p2p3p4p3p4p5p4p0p6z1"
b0 = blocks.getBlocks(testblock.toTile(s6), ba, ji, tenpai.getTenpai(s6)[0], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(s6))
print(b0)
b1 = blocks.getBlocks(testblock.toTile(s6), ba, ji, tenpai.getTenpai(s6)[-1], agari.by_int(32), nuki=2)[0]
print(b1.blocks)
print(dora().check(b1, yama))
print(uradora().check(b1, yama))
print(nukidora().check(b1, yama))
print(akadora().check(b1, yama))

rs = "m2m2m3m3m4m4m5m6m6m7m7m8m8"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[3], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)

print(iipeikou().check(rb, yama))
print(ryanpeikou().check(rb, yama))
print(pinfu().check(rb, yama))
