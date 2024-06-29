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
finite_field = multiply_finite_field(5)

# multiply finite field of 9 elements
# Looking closely we discover we cant user integers for finite field of 9 elements
# because elements 3 and 6 do not have multiplicative inverse
finite_field2 = multiply_finite_field(9)

def isFiniteField(field):
    for row in field:
        if 1 not in row:
            print("not an integer finite field")
            return False
    print("is a finite field")
    return True



# Testing
# Finite Field of 5 element is a finite field
isFiniteField(finite_field)

# Finite Field of 9 integer element is not a finite field 
isFiniteField(finite_field2)
