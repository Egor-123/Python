import math


def sqrt_round(n):
    return int(math.sqrt(n))


sqrt_round_lambda = lambda m: int(math.sqrt(m))

n = int(input())
print(sqrt_round)
print(sqrt_round_lambda)
