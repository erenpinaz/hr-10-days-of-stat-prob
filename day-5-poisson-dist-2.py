import math

def poi_dist(l, k):
    return (pow(l, k) * pow(2.71828, -1 * l)) / math.factorial(k)

def calculate_cost(t, x):
    return t + (40 * pow(x, 2))

l = list(map(float, input().split()))

print('{0:.3f}'.format(poi_dist(l[0], calculate_cost(160, l[0]))), end = ' ')
print('{0:.3f}'.format(poi_dist(l[1], calculate_cost(140, l[1]))), end = ' ')
