from ichihime.Enum.Agaru import Agaru
from ichihime.Enum.Category import Category
from ichihime.Enum.Tile import Tile
from ichihime.Enum.Yaku import Yaku
from ichihime.src.Agari import Agari
from ichihime.src.Block import Block
from ichihime.src.Tenpai import Tenpai
from ichihime.test.BlockTest import Test

print(Block.rdBlock())

ba = Tile.NAN
ji = Tile.SHAA


def blocktest(s):
    print(Tenpai.getTenpai(s))
    for t in Tenpai.getTenpai(s):
        print(Block.getBlocks(Test.toTile(s), ba, ji, t, Agari.by_int(32)))
        for b in Block.getBlocks(Test.toTile(s), ba, ji, t, Agari.by_int(32)):
            print(b)


s1 = "m1m9p1p9s1s9z1z2z3z4z5z6z7"
blocktest(s1)
s1 = "m1m9p1p9s1s9z1z2z3z4z5z6z6"
blocktest(s1)
s2 = "z1z1z2z2z3z3z4z4z5z5z6z6z7"
blocktest(s2)
s3 = Test.W90.value
blocktest(s3)
s4 = "m1m1m1m2m2m2m3m3m3m4m4m4m5"
blocktest(s4)
s5 = "m1m2m3m4m1m2m3m4m1m2m3m4m5"
blocktest(s5)
s6 = "p1p2p3p4p1p2p3p4p1p2p3p4p5"
blocktest(s6)
y6 = Yaku.yaku(Block.getBlocks(Test.toTile(s6), ba, ji, Tenpai.getTenpai(s6)[0], Agari.by_int(32))[0])
print(y6)
s7 = "z2z2z2z3z3z3z5z5z5z6z6z6z4"
blocktest(s7)

y7 = Yaku.yaku(Block.getBlocks(Test.toTile(s7), ba, ji, Tenpai.getTenpai(s7)[0], Agari.by_int(32))[0])
print(y7)

print(Agari.by_int(32).__repr__())
# TODO: 몸통 계산 -> 하나 빼고 계산(대기형태 때문)
# TODO: 치또이/국사


# 5개중에 하나에서 대기패
# 나머지 13개 패로 다시 역 계산

# 손역 없음/멘젠시에만 역 있음
# 리치(높은 확률로)/멘젠쯔모/영상개화(깡쯔가 있으면)/해저로월, 하저로어
# 손역 있음h
# 다마텐/후로/리치(높은 확률로)/영상개화(깡쯔가 있으면)/해저로월, 하저로어

# 리치시
# 낮은 확률로 일발/멘젠쯔모

print(Agari.by_int(0x2C))
