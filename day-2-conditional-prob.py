import itertools as it
from fractions import Fraction as frac

F = ('b', 'g')
A = ('g', 'g')
S = list(it.product(F, repeat=2))
B = [p for p in S if p != A]

print(frac(1 / len(B)).limit_denominator())
