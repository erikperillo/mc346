module IntsFromString
(
    wordsListFromLines,
    intsFromWords,
    intsListFromWordsList,
    intsListFromString
)
where

--gets a list of lists of words from string containing line separators.
wordsListFromLines :: [String] -> [[String]]
wordsListFromLines lines = filter (not . null) $ map words lines

--converts a list of strings into a list of ints.
intsFromWords :: [String] -> [Int]
intsFromWords wordsList = map (read :: String -> Int) wordsList

--converts a list of lists of ints from a list of lists of strings.
intsListFromWordsList :: [[String]] -> [[Int]]
intsListFromWordsList wordsList = map intsFromWords wordsList

--gets a list of lists of ints from a string containing line separators.
intsListFromString :: String -> [[Int]]
intsListFromString str =
    intsListFromWordsList . wordsListFromLines . lines $ str
