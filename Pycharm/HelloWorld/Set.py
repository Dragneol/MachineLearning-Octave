# Program to perform different set operations
# as we do in  mathematics

# sets are define
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

# union
print("A Union B:", A | B)
print("B Union A:", B.union(A))

# intersection
print("A Intersection B:", A & B)
print("B Intersection A:", B.intersection(A))

# difference
print("A Difference B:", A - B)
print("B Difference A:", B.difference(A))

# symmetric difference
print("A Symmetric difference B:", A ^ B)
print("B Symmetric difference A:", B.symmetric_difference(A))
