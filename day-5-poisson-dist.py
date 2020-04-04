import math

def poi_dist(l, k):
    return (pow(l, k) * pow(2.71828, -1 * l)) / math.factorial(k)

l = float(input())
k = float(input())

print('{0:.3f}'.format(poi_dist(l, k)))
