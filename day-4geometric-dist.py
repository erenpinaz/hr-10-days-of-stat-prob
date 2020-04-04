def geo_dist(q, n, p):
    return pow(q, n - 1) * p

pn, pd = list(map(float, input().split()))
n = int(input())
p = pn/pd
q = 1 - p

print('{0:.3f}'.format(geo_dist(q, n, p)))
