#include <stdio.h>
#include <stdlib.h>

long fib(int n) {
  if (n == 1 || n == 2) {
    return 1;
  } else {
    return fib(n-1) + fib(n-2);
  }
}

void main(int argc, char** argv) {
  int n = atoi(argv[1]);
  printf("%d\n", fib(n));
}

