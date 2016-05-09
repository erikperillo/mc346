module Distance
    where

type Distance = Float

cmToM :: Distance -> Distance
cmToM x = x*0.01

mToCm :: Distance -> Distance
mToCm x = x*100.0

cmToIn :: Distance -> Distance
cmToIn x = x/2.54

inToCm :: Distance -> Distance
inToCm x = x*2.54

mToIn :: Distance -> Distance
mToIn x = cmToIn . mToCm $ x

inToM :: Distance -> Distance
inToM x = cmToM . inToCm $ x

yToCh :: Distance -> Distance
yToCh x = x/22

chToY :: Distance -> Distance
chToY x = x*22

yToM :: Distance -> Distance
yToM x = x*0.9144

mToY :: Distance -> Distance
mToY x = x/0.9144

chToM :: Distance -> Distance
chToM x = yToM . chToY $ x

mToCh :: Distance -> Distance
mToCh x = yToCh . mToY $ x
