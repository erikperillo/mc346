module Rect
(
    Rect,
    area,
    minX,
    maxX,
    minY,
    maxY
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
        x :: Int, 
        y :: Int,
        w :: Int,
        h :: Int
    }
    deriving(Show)

--returns the area of a certain rectangle.
area :: Rect -> Int
area rect = (w rect) * (h rect)

--returns minimum x point of rectangle
minX :: Rect -> Int
minX = x

--returns maximum x point of rectangle
maxX :: Rect -> Int
maxX rect = x rect + w rect

--returns minimum y point of rectangle
minY :: Rect -> Int
minY = y

--returns maximum y point of rectangle
maxY :: Rect -> Int
maxY rect = y rect + h rect
