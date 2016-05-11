import System.IO
import MaxArea

-- main program. 
-- finds the maximum area of compatible rectangles given a set of rectangles.
main :: IO ()
main = do
    contents <- getContents
    let rects = preProcess contents
    putStr $ show $ maxArea rects
    putStrLn ";"
