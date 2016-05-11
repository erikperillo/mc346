module RectCompat
(
    compatible,
    compatibleWithGroup,
    compatibleGroupWith,
    compatibleGroups
)
where

import Rect

--determines whether two rectangles are compatible or not.
compatible :: Rect -> Rect -> Bool
compatible rectA rectB = 
    maxX rectA < minX rectB && maxY rectA < minY rectB ||
    maxX rectB < minX rectA && maxY rectB < minY rectA

--determines whether a given rectangle is compatible with a given
--group of rectangles.
compatibleWithGroup :: Rect -> [Rect] -> Bool
compatibleWithGroup rect rectGroup = all (compatible rect) rectGroup

--given a specific rectangle R and a group of rectangles G,
--determines (if any) a group of compatible rectangles 
--that contains R and other rectangles from G.
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

--gives all possible groups of compatible rectangles given a group.
compatibleGroups :: [Rect] -> [[Rect]]
compatibleGroups rects = 
    filter (not . null) [compatibleGroupWith x rects | x <- rects]
