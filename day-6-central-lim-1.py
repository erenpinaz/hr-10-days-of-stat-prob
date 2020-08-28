# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cumulative_normal_dist(x, u, s):
    return 0.5 * (1 + math.erf((x - u) / (s * math.sqrt(2))))

x = float(input())
n = float(input())
u = float(input())
s = float(input())

nu = n * u
ns = math.sqrt(n) * s

print('{0:.4f}'.format(cumulative_normal_dist(x, nu, ns)))