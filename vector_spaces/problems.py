import vector.vecutil

def vec_select(veclist, k):
  return [vec for vec in veclist if vec[k] == 0.0]

def vec_sum(veclist, D):
  return sum(veclist, vector.vecutil.zero_vec)

def vec_select_sum(D, veclist, k):
  selected = vec_select(veclist, k)
  return vec_sum(selected, D)

def scale_vecs(vecdict):
  return [(1/k) * vecdict[k] for k in vecdict]

def GF2_span(D, L):
  if len(L) == 0:
    return [[]]
  
  first = l[0]
  rest = L[1:]
  powerset_combinations = GF2_span(D, rest)
  all_combinations = []

  for combination in powerset_combinations:
    for d in D:
      all_combinations.append([d * first] + combination)
  
  return all_combinations
    
# real numbers a, b
# z = ax + by
# prove there are two 3-vectors v1, v2 such that the set of points [x, y, z] satisfying
# the equation is exactly the set of linear combinations of v1 and v2.
#
# first thought: isn't this just the equation of a line? maybe the standard generators for
# r^2 will be fine.
# nope, the equation of a line is y = mx + b
# well, the existensial qualifier for a, b, and c seems to imply that they can be any real numbers.
# if that's the case, then I feel that the R2 vector space is fine, and therefore the standard generators
# , since I don't see what points x, y, and z this equation precludes.

# actually, the real solution will probably involve a and b in the vectors somehow,
# the problem presumes that a and b will be rooted, but they can be rooted to arbitrary
# values in R.

# 0 = ax + by + z
# homogenous linear equation ^
# the solution set of this should be equivalent to a vector space, and therefore, a vector span, and therefore
# a linear combination of two vectors.

# {a1 * [3, 1] : a1 from R where a1 >= 0 and a1 <= 3}
# convex hull of {[0, 0, 0], [2, 2, 2], [2, 2, 0]}
# -> {a1 * [0, 0, 0] + a2 * [2, 2, 2] + a3 * [2, 2, 0] : a1, a2, a3 from R where a1, a2, a3 > 0 and a1 + a2 + a3 = 1}

# {[x, y, z] : x, y, z E R, x + y + z = 1} is not a vector space because it doesn't include the zero vector and
# it isn't closed under addition or multiplication.

# {[x, y, z] : x, y, z E R, x + y + z = 0} is a vector space. all vector components equal zero,
# and zero annihilates all scalars under multiplication, and is the identity for addition
# in a set where all other vectors inner sum is equal to zero (by commutativity ensuring that component-wise
# addition would remain zero)

# {[x1, x2, x3, x4, x5] : x1, x2, x3, x4, x5 E R, x2 = 0 or x5 = 0} is not a vector
# space because it isn't closed under addition. example:
# [1, 0, 1, 1, 1] + [1, 1, 1, 1, 0] = [1, 1, 1, 1, 1]

# The set of 5 vectors over GF(2) that has an even number of 1's is a vector space because:
# it contains the zero vector (no 1s)
# it is closed under multiplication (can either be multiplied by 1 which ids the vector or by zero
# which makes it the zero vector)
# it is closed under addition (either there are no conflicting components, in which case parity
# is maintained by adding an even number to an even number, or there are conflicting components. If there are conflicting
# components, there can either be an even number of them or an odd number. if there are an even number,
# but vectors would subtract an even number of 1s, maintaining parity. If there was an odd number, then the final
# mask would've been of odd parity, and by subtracting an odd number of components, we maintain parity).


# the set of 5 vectors over GF(2) that have an odd number of 1s isn't a vector space because it
# doesn't contain the zero vector.


