module RectCompat
(
    compatible,
    compatibleWithGroup,
    compatibleGroupWith
)
where

import Data.List(intersect)
import Rect

--determines whether two rectangles are compatible or not.
compatible :: Rect -> Rect -> Bool
compatible rectA rectB = 
    maxX rectA < minX rectB && maxY rectA < minY rectB ||
    maxX rectB < minX rectA && maxY rectB < minY rectA

compatibleWithGroup :: Rect -> [Rect] -> Bool
compatibleWithGroup rect rectGroup = all (compatible rect) rectGroup

compatibleGroupWith :: Rect -> [Rect] -> [Rect]
compatibleGroupWith rect rectGroup = 
    compatibleGroupWith' rectGroup [rect]
    where
        compatibleGroupWith' :: [Rect] -> [Rect] -> [Rect]
        compatibleGroupWith' [] [x] = []
        compatibleGroupWith' [] acc = acc
        compatibleGroupWith' (r:rs) acc = 
            if compatibleWithGroup r acc then
                compatibleGroupWith' rs (r:acc)
            else
                compatibleGroupWith' rs acc

