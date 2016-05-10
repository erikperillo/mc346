module RectGroup
(
    groupArea,
    maxGroupArea    
)
where

import Rect

--determines index of first ocurrence of specified element in list.
--assumes element is indeed in the list.
index :: (Eq a) => a -> [a] -> Int
index _ [] = error "element not in list"
index y (x:xs) 
    | y == x = 0
    | otherwise = 1 + index y xs

--determines area of group of rectangles, that is, 
--the sum of the areas of each rectangle in that group.
groupArea :: [Rect] -> Int
groupArea rectGroup = sum . map area $ rectGroup

--given a list of groups of rectangles, returns a tuple
--containing the maximum group area of the set and the 
--position of the group with maximum area in the list.
maxGroupArea :: [[Rect]] -> (Int, Int)
maxGroupArea rectGroups = (maxArea, index maxArea rectGroupsAreas)
    where
        rectGroupsAreas = map groupArea rectGroups
        maxArea = maximum rectGroupsAreas
