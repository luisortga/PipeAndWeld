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

print(sum_two(12, 16))