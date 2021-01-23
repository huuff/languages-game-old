import System.Environment
import System.Exit
import Data.List (insert, intercalate)

insertionSort :: Ord a => [a] -> [a]
insertionSort = foldr insert []

main = do args <- getArgs
          let output = insertionSort $ map (read :: String->Int) args
          putStrLn $ intercalate " " (map (show :: Int->String) output)
