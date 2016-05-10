-- Reads rectangles and outputs them

import System.IO

process :: [String] -> String
process = unlines . map ("linha: " ++)

-- | 'main' runs the main program
main :: IO ()
main = do
  contents <- getContents
  putStrLn $ process $ lines contents

