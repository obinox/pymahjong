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
yama.idc_open = 4
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

rs = "m2m2m3m3m4m4m0m6m6m7m7m8m8"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[3], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)

print(iipeikou().check(rb, yama))
print(ryanpeikou().check(rb, yama))
print(pinfu().check(rb, yama))
print(tanyao().check(rb, yama))

rs = "m1m2m3m4m0m6m7m8m9m1m4m5m6"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[1], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(ittsu().check(rb, yama))
print(iipeikou().check(rb, yama))

rs = "m1m2m3p1p2p3s1s2s3m8m9m9m9"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[0], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)

print(doukou().check(rb, yama))
print(doujun().check(rb, yama))
print(chanta().check(rb, yama))
print(junchan().check(rb, yama))

rs = "m3m3m3p3p3p3s3s3s3z1z1z2z2"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[1], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(doukou().check(rb, yama))
print(doujun().check(rb, yama))


rs = "z1z1z1z2z2z2z3z3z3z4z4z4z5"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[0], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(bakaze().check(rb, yama))
print(jikaze().check(rb, yama))
print(ton().check(rb, yama))
print(nan().check(rb, yama))
print(shaa().check(rb, yama))
print(pei().check(rb, yama))


rs = "z5z5z5z6z6z6z7z7z7z1z1z2z2"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[1], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(haku().check(rb, yama))
print(hatsu().check(rb, yama))
print(chun().check(rb, yama))
print(bakaze().check(rb, yama))
print(jikaze().check(rb, yama))
print(ton().check(rb, yama))
print(nan().check(rb, yama))
print(shaa().check(rb, yama))
print(pei().check(rb, yama))


rs = "z5z5z5z6z6z6z7z7z7z1z1z2z2"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[1], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(honitsu().check(rb, yama))
print(chiniisou().check(rb, yama))
print(shousangen().check(rb, yama))

rs = "m1m1m1m2m3m4m5m6m7m8m9m9m9"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[1], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(honitsu().check(rb, yama))
print(chiniisou().check(rb, yama))

rs = "p1p1p2p2p3p3p4p4p5p5p6p6z3"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[1], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(honitsu().check(rb, yama))
print(chiniisou().check(rb, yama))

rs = "z5z5z5z6z6z6z7z7z1z1z1z2z2"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[0], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(shousangen().check(rb, yama))
print(toitoi().check(rb, yama))

rs = "z1z1z2z2z3z3z4z4z5z5z6z6z7"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[0], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(shousangen().check(rb, yama))
print(toitoi().check(rb, yama))
print(chiitoi().check(rb, yama))
print(honitsu().check(rb, yama))

rs = "m1m9p1p9s1s9z1z2z3z4z4z5z6"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[0], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(kokushi().check(rb, yama))
print(juusanmen().check(rb, yama))

rs = "m1m9p1p9s1s9z1z2z3z4z5z6z7"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[0], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(kokushi().check(rb, yama))
print(kokushi13().check(rb, yama))

rs = "m1m1m1m2m3m4m5m6m7m8m9m9m9"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[0], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(chuuren().check(rb, yama))
print(kyuumen().check(rb, yama))

rs = "s1s1s1s2s2s3s4s5s6s7s8s9s9"
rbs = blocks.getBlocks(testblock.toTile(rs), ba, ji, tenpai.getTenpai(rs)[1], agari.by_int(32), nuki=2)
print(tenpai.getTenpai(rs))
rb = rbs[0]
print(rbs)
print(rb.blocks)
print(chuuren().check(rb, yama))
print(kyuumen().check(rb, yama))

