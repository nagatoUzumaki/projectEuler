import math
import functools

for _ in range(int(input())):
    n = int(input())
    print(functools.reduce(lambda x, y: x * y // math.gcd(x, y), range(1, n + 1)))