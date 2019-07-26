import itertools

d1 = list(range(1, 7))
d2 = list(range(1, 7))

prod = list(itertools.product(d1, d2))
count_prob = sum(1 for p in prod if(p[0] + p[1] <= 9))

print(count_prob, '/', len(prod))
