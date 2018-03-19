from vector import vec, vecutil
from matrix import matutil
import math
Vec = vec.Vec

def is_zero_vector(v):
  for d in v.D:
    if v[d]:
      return False
  return True

def find_sigma(b, v):
  return ((b*v)/(v*v)) if v*v > 1e-20 else 0

def project_along(b, v):
  return find_sigma(b, v) * v

def project_orthogonal(b, vlist):
  for v in vlist:
    b = b - project_along(b, v)
  return b

def aug_project_orthogonal(b, vlist):
  sigmadict = {len(vlist): 1}
  for i, v in enumerate(vlist):
    sigma = find_sigma(b, v)
    sigmadict[i] = sigma
    b = b - sigma*v
  return (b, sigmadict)

def orthogonalize(vlist):
  vstarlist = []
  for v in vlist:
    vstarlist.append(project_orthogonal(v, vstarlist))
  return vstarlist

def find_basis(vlist):
  orthogonal_basis = orthogonalize(vlist)
  return [v for v in orthogonal_basis if not is_zero_vector(v)]

def find_subset_basis(vlist):
  orthogonal_basis = orthogonalize(vlist)
  return [vlist[v] for v in range(len(orthogonal_basis)) if not is_zero_vector(orthogonal_basis[v])]

def aug_orthogonalize(vlist):
  vstarlist = []
  sigma_vecs = []
  D = set(range(len(vlist)))
  for v in vlist:
    (vstar, sigmadict) = aug_project_orthogonal(v, vstarlist)
    vstarlist.append(vstar)
    sigma_vecs.append(Vec(D, sigmadict))
  return vstarlist, sigma_vecs

def find_orthogonal_complement(U_basis, W_basis):
  combined = U_basis + W_basis
  orthogonalized = orthogonalize(combined)
  w_orthogonal = orthogonalized[len(U_basis)]
  return [W_basis[v] for v in range(len(w_orthogonal)) if not is_zero_vector(w_orthogonal[v])]

def vec_norm(v):
  return math.sqrt(v * v)

def orthonormalization(L):
  """
  input: a list L of linearly independent Vecs
  output: a list L* of len(L) orthonormal Vecs such that,
  for i = 1, ..., len(L), the first i Vecs of L*
  and the first i vecs of L span the same space
  """
  orthed_up = orthogonalize(L)
  norms = [vec_norm(v) for v in orthed_up]
  return [
    (1/norms[i] * orthed_up[i]) for i in range(len(orthed_up))
  ]

orth_test_list = [
  vecutil.list2vec([4, 3, 1, 2]),
  vecutil.list2vec([8, 9, -5, -5]),
  vecutil.list2vec([10, 1, -1, 5])
]

orth_test = orthonormalization(orth_test_list)
orth_test_rounded = [
 (vecutil.list2vec([round(o[d], 2) for d in o.D]))  for o in orth_test
]
assert(
  orth_test_rounded == [
    Vec({0, 1, 2, 3},{0: 0.73, 1: 0.55, 2: 0.18, 3: 0.37}),
    Vec({0, 1, 2, 3},{0: 0.19, 1: 0.4, 2: -0.57, 3: -0.69}),
    Vec({0, 1, 2, 3},{0: 0.53, 1: -0.65, 2: -0.51, 3: 0.18})
  ]
)

def aug_orthonormalize(L):
  orth, sigmas = aug_orthogonalize(L)

  def adjust(v, multipliers):
    return vecutil.list2vec([v[d] * multipliers[d] for d in v.D])
  
  norms = [vec_norm(v) for v in orth]
  QList = [1/norms[i] * orth[i] for i in range(len(orth))]

  RList = [adjust(v, norms) for v in sigmas]

  return QList, RList

aug_test_list = [
  vecutil.list2vec(v) for v in [[4, 3, 1, 2], [8, 9, -5, -5], [10, 1, -1, 5]]
]

QList, RList = aug_orthonormalize(aug_test_list)

