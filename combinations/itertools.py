from itertools import combinations, permutations, combinations_with_replacement
import math
# all permutations
numbers = [1, 2, 3]
print(list(permutations(numbers)))

#all permutations of 2 elements
print(list(permutations(numbers, 2)))
print(math.perm(3, 2))

# all combinations of 2 elements
print(list(combinations(numbers, 2)))
print(math.comb(3, 2))

# combination of the same element to the same element
print(list(combinations_with_replacement(numbers, 2)))