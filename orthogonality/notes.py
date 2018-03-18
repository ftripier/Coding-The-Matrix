from inner_product.notes import project_along
from vector import vecutil
import math

def project_orthogonal(b, vlist):
  """
  input:
  vector b and a list vlist of vectors

  output:
  the projection of b orthogonal to Span vlist
  """
  for v in vlist:
    b = b - project_along(b, v)
  return b


def classical_project_orthogonal(b, vlist):
  w = vecutil.zero_vec({i for i in range(len(b.D))})
  for v in vlist:
    w = w + project_along(b, v)
  return b - w

def test_method_non_orthogonal(method):
  first = vecutil.list2vec([1, 0])
  second = vecutil.list2vec([math.sqrt(2)/2, math.sqrt(2)/2])
  vlist = [first, second]
  b = vecutil.list2vec([1, 1])
  return method(b, vlist)

def test_method_orthogonal(method):
  b = vecutil.list2vec([1, 1, 1])
  v1 = vecutil.list2vec([0, 2, 2])
  v2 = vecutil.list2vec([0, 1, -1])
  vlist = [v1, v2]
  return method(b, vlist)


# problem 9.2.5
# just as a lazy hand-wavy proof because I'm hungry,
# we can prove classical_project_orthogonal and project_orthogonal are
# equivalent by a proof of induction on 
# i Ǝ N
# where for a set of vectors of size k
# project_orthogonal^i == classical_project_orthogonal^(k - i)
# where we are free to rearrange vectors in classical_project_orthogonal by commutativity
# of vector addition.
# for example, at i == 1, we've subtracted one iteration from b, and
# we are one iteration away from having completed classical_project_orthogonal,
# making the two equivalent.

def aug_project_orthogonal(b, vlist):
  sigmadict = {len(vlist): 1}
  for i, v in enumerate(vlist):
    sigma = (b * v)/(v * v) if v*v > 1e-20 else 0
    sigmadict[i] = sigma
    b = b - sigma*v
  return (b, sigmadict)


