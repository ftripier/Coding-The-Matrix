def lin_comb(vlist, clist):
  return sum([coeff * v for (coeff, v) in zip(clist, vlist)])

# write each of the old vectors [3, 0, 0] [0, 2, 0] and [0, 0, 1] as a linear
# combination of the new vectors [2, 0, 1] [1, 0, 2] [2, 2, 2] and [0,1, 0]

# [3, 0, 0] = 2 * [2, 0, 1] - [1, 0, 2]
# [0, 2, 0] = 2 * [0, 1, 0]
# [0, 0, 1] = [2, 2, 2] - [2, 0, 1] - 2 * [0, 1, 0]

def standard(D, one):
  return [Vec(D, {d: one}) for d in D]

# do these span r2
# r2 standard generators = [1, 0], [0, 1]
# 1. [1, 2], [3, 4]
# [1, 0] = 1 * [3, 4] - 2 * [1, 2]
# [0, 1] = can't do it! there's no way to invert the parity of the second component
# but if we add [3, 3]
# 1 * [3, 4] - 1 * [3, 3]
#
# 2. [1, 1], [2, 2], [3, 3]
# [1, 0] = impossible, there's no difference of one between and vector's first component
# but if we add [1, 2]
# [1, 0] = 1 * [2, 2] - 1 * [1, 2]
# [0, 1] = 1 * [1, 2] - 1 * [1, 1]
#
# 3. [1, 1], [1, -1], [0, 1]
# [1, 0] = 1 * [1, 1] + -1 * [1, -1] + -1 * [0, 1]
# [0, 1] = 0 * everything_else + 1 * [0, 1]

# span r3 with [1, 1, 1] and [0.4, 1.3, -2.2] and a vector x
# basically I need a pairwise difference of one for all components in my new vector
# or wait, I guess the only interesting thing about the other two vectors are the differences
# between the second vector's components. The first one could be multiplied by some real valued
# number to cancel out the decimal difference.
# perhaps if I multiplied the vectors by 10 it would be easier to reason about how to search
# for x.
# [10, 10, 10] and [3, 13, -22]
# difference is [7, -3, 33]
# still not getting anything.
# TODO: solve this problem
# 

# [1, 0, 0] = 
# [0, 1, 0] =
# [0, 0, 1] =


