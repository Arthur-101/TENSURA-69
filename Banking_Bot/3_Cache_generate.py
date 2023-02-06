import string
import random

cache0 = ''.join(random.choices(string.digits+string.ascii_letters,k=8))
cache1 = print(cache0)

for i in range(6):
    r1 = random.choice(range(8))
    r2 = random.choice(['-','*','^','+','?'])
    cache0 = cache0[:r1] + r2 + cache0[r1:]
    r1 += 1
cache = print(cache0)
