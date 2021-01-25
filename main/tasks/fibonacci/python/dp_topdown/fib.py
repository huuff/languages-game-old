#!/usr/bin/env python
import sys

class Memoized(object):
    cache = {}

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        arg = args[0]
        if arg in self.cache:
            return self.cache[arg]
        else:
            result = self.f(*args, **kwargs)
            self.cache[arg] = result
            return result

@Memoized
def fib(n): 
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(int(sys.argv[1])))
