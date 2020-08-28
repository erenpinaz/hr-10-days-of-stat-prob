# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cumulative_normal_dist(u, s, v):
    return 0.5 * (1 + math.erf((v - u) / (s * math.sqrt(2))))

u, s = list(map(float, input().split()))
q1 = float(input())
q2 = float(input())

print('{0:.2f}'.format((1 - cumulative_normal_dist(u, s, q1)) * 100))
print('{0:.2f}'.format((1 - cumulative_normal_dist(u, s, q2)) * 100))
print('{0:.2f}'.format(cumulative_normal_dist(u, s, q2) * 100))