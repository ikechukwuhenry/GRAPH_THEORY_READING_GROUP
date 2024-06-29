def congruence(a, mod):
    return a % mod

print(congruence(-1, 9))


import numpy as np

# create a finite field with p number of elements
p = 9
a = b = np.arange(1, p)

# find the outer products of these 2 sets of elements
outer_product = np.outer(a, b)

# find the mod of each to check if each element has a multiplicative inverse
ans = outer_product % p
print(ans)
