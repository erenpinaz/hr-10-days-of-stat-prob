from fractions import Fraction as frac

urns = [[4, 7], [5, 9], [4, 8]]
prx = urns[0][0] / urns[0][1]
pry = urns[1][0] / urns[1][1]
prz = urns[2][0] / urns[2][1]

print(frac((prx * pry * (1 - prz)) + (prx * (1 - pry) * prz) + ((1 - prx) * pry * prz)).limit_denominator())
