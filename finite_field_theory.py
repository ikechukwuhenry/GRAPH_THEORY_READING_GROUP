import numpy as np

def congruence(a, mod):
    return a % mod

print(congruence(-1, 9))


def multiply_finite_field(p):
    # Create a finite field with p number of elements
    a = b = np.arange(1, p)

    # Find the outer products of these 2 sets of elements
    outer_product = np.outer(a, b)
    # Find the mod of each to check if each element has a multiplicative inverse
    result = outer_product % p
    print(result)
    return result


# Multiply finite field of 5 elements
multiply_finite_field(5)

# multiply finite field of 9 elements
# Looking closely we discover we cant user integers for finite field of 9 elements
# because elements 3 and 6 do not have multiplicative inverse
multiply_finite_field(9)


"""
# create a finite field with p number of elements
p = 9
a = b = np.arange(1, p)

# find the outer products of these 2 sets of elements
outer_product = np.outer(a, b)

# find the mod of each to check if each element has a multiplicative inverse
ans = outer_product % p
print(ans)
"""
