import math

def poi_exp(a):
    return (a + pow(a, 2))

def calculate_costA(ex):
    return 160 + (40 * ex)

def calculate_costB(ey):
    return 128 + (40 * ey)

l = list(map(float, input().split()))

print('{0:.3f}'.format(calculate_costA(poi_exp(l[0]))))
print('{0:.3f}'.format(calculate_costB(poi_exp(l[1]))))
