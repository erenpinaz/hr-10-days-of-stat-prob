import math

def cumulative_normal_dist(u, s, v):
    return 0.5 * (1 + math.erf((v - u) / (s * math.sqrt(2))))


u, s = list(map(float, input().split()))
v = float(input())
l = list(map(float, input().split()))

print('{0:.3f}'.format(cumulative_normal_dist(u, s, v)))
print('{0:.3f}'.format(cumulative_normal_dist(u, s, l[1]) - cumulative_normal_dist(u, s, l[0])))