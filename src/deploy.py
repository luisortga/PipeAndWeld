# Generadores
# remember 12_000_000
# Generator

import time

"""
    Generadores
"""

gen_cuadrador = (x**2 for x in range(8))
print(next(gen_cuadrador))

for x in gen_cuadrador:
    time.sleep(4)
    print(x)

def contar():
    yield 1
    yield 2
    yield 3

g = contar()

print(next(g))
print(next(g))
print(next(g))