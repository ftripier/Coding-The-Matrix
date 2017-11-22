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
# 2. [1, 1], [2, 2], [3, 3]

