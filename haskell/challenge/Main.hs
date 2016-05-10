import System.IO
import Rect
import RectCompat
import RectGroup

wordsListFromLines :: [String] -> [[String]]
wordsListFromLines lines = filter (not . null) $ map words lines

wordsListFromString :: String -> [[String]]
wordsListFromString string = wordsListFromLines . lines $ string

intsFromWords :: [String] -> [Int]
intsFromWords wordsList = map (read :: String -> Int) wordsList

intsListFromWordsList :: [[String]] -> [[Int]]
intsListFromWordsList wordsList = map intsFromWords wordsList

--preProcess :: String -> [[Int]]
--preProcess contents = 
 --   intsListFromWordsList . wordsListFromString $ contents
preProcess :: String -> String
preProcess str = "hue"

-- | 'main' runs the main program
main :: IO ()
main = do
    contents <- getContents
    putStrLn $ show $ preProcess contents
