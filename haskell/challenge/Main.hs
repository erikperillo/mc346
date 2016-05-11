import System.IO
import Rect
import RectCompat
import RectGroup
import IntsFromString(intsListFromString)
import Data.List(sortBy)

--preprocessing area: all these functions filter input and transform it into 
--relevant data.
--gets a list of lists of ints and removes the head from each list
cutHeads :: [[Int]] -> [[Int]]
cutHeads ints = map tail ints

--gets a rect from a list of 4 ints
rectFromInts :: [Int] -> Rect
rectFromInts [xmin,xmax,ymin,ymax] = Rect xmin xmax ymin ymax

--gets a list of rects from a list of lists of ints
rectsFromInts :: [[Int]] -> [Rect]
rectsFromInts ints = 
    map rectFromInts $ filter (not . null) ints

--final preprocessing of input
preProcess :: String -> [Rect]
preProcess str = rectsFromInts . cutHeads . intsListFromString $ str

--gets desired answer from pre-processed string
getAnswer :: [Rect] -> Int
getAnswer rects = fst . maxGroupArea . compatibleGroups $ rects

-- | 'main' runs the main program
main :: IO ()
main = do
    contents <- getContents
    let rects = preProcess contents in
        putStr $ show $ getAnswer rects
    putStrLn ";"
