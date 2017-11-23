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
# EDIT: I was wrong it's totally possible.
# [1, 0] = 1 * [3, 4] - 2 * [1, 2]
# [0, 1] = (-0.5) * [3, 4] + 1.5 * [1, 2]

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
#
# it seems I need a third vector that isn't parallel to either of the given vectors.
# so, a vector with a non-1 dot product with either vector.
# so [1, 2, 3] should work

# [1, 0, 0] = 
# [0, 1, 0] =
# [0, 0, 1] =

def test_scalars(clist):
  from vector.vec import Vec
  D = {0, 1, 2}
  a = Vec(D, {0: 1, 1: 1, 2: 1})
  b = Vec(D, {0: 0.4, 1: 1.3, 2: -2.2})
  c = Vec(D, {0: 1.4, 1: 0.3, 2: -1.2})
  vlist = [a, b, c]
  result = lin_comb(vlist, clist)
  return [result[0], result[1], result[2]]

# the vectors in u1 + V are exactly the set of all affine combinations of u1, u2, and u3
# - affine combination means some linear combination where the coefficients sum to one.
# I think a good way to think about this is that the "sum to one" is a constraint on
# the "planeness" of the point-vectors.

# the set of all affine combinations of vectors is called the 'affine hull'
# does the affine hull always sketch out the geometry of the set of vectors? (the hull, I suppose)

# affine hull of a single object is a point
# affine hull of two vectors is a line
# affine hull of three vectors is a plane

# seems like it collapses the geometry of the linear combination down a dimension

# an affine space is the result of translating a vector space
# QUESTION: why are affine combinations and affine hulls constrained, but affine spaces seemingly unbounded?

# a flat is just an affine space that is a subset of R^n for some n.
# this makes sense because defining a flat as a "shape" kind of relies on some human context.
# really, the shape only exists because of the contrast between hull and negative space (a _subset_ of R^n)
# and the translation component is important because a flat isn't defined to be rooted at the origin, but a vector space must contain it
# in order to retain closure of composition

# although, it appears that you can biject an affine space to an affine hull of "some vectors"
# (not necessarily those that define the span of the affine's spaces space). This
# is probably useful because you can go from reasoning about vector spaces to reasoning
# about sets and affine combinations.

# convex combination is an affine combination where coefficients must be non-negative.
# the hull formed from convex combinations is the space defined inside of the vectors -
# so an affine hull would be a plane and a convex hull would be a triangle

