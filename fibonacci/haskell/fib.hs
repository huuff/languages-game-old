import System.Environment
import System.Exit
import Data.List (insert, intercalate)

fib :: Integer -> Integer
fib 1 = 1
fib 2 = 1
fib n = fib (n-1) + fib (n-2)

main = do args <- getArgs
          let n = read (head args) :: Integer
          putStrLn $ show (fib n)
