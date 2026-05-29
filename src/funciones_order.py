"""
@author: luisorteg
"""
from typing import Callable

current: int = 0

# lambda all in line single
sum_two_value: Callable[[int, int], int] = lambda f_value, s_value: f_value+s_value

print(sum_two_value(12, 36))

# mejor practica funcion estandar de una sola linea

def sum_two(firts_v: int, second_v: int) -> int: return firts_v+second_v


def multiply(firts_v: float, second_v: float) -> float: return firts_v**second_v

# void
def firt_info() -> None: print(f'El resultado de la lambda es {sum_two_value(10, 2)} y de la funcion de una sola linea {sum_two(12,16)}')

print(sum_two(12, 16))
firt_info()
print(multiply(2, 8))