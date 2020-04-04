def geo_dist(q, n, p):
    return pow(q, n - 1) * p

pn, pd = list(map(float, input().split()))
n = int(input())
p = pn/pd
q = 1 - p

prob = sum([geo_dist(q, i, p) for i in range (1, n + 1)])
print('{0:.3f}'.format(prob))
