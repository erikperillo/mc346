module Rect
(
    Rect(..),
    area,
    width,
    height
)
where

--constructor for rectangle data type, where
--  x is the x position of the left uppermost part of rectangle;
--  y is the y position of the left uppermost part of rectangle;
--  w is the width of the rectangle;
--  h is the height of the rectangle.
data Rect = 
    Rect 
    {
        minX :: Int, 
        maxX :: Int,
        minY :: Int,
        maxY :: Int
    }
    deriving(Show)

--returns the width of a certain rectangle.
width :: Rect -> Int
width rect = (maxX rect) - (minX rect)

--returns the height of a certain rectangle.
height :: Rect -> Int
height rect = (maxY rect) - (minY rect)

--returns the area of a certain rectangle.
area :: Rect -> Int
area rect = (width rect) * (height rect)
