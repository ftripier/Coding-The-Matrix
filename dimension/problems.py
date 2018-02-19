# 6.7.5

# 1.
# a) {[1 2 0], [0 2 1]}
# This serves as a basis because both vectors in row space have zero entires in the others nonzero entry.

# b) {[1 0], [0 1]}
# This serves as a basis for column space becase [2 2] = 2 * [1 0] + 2 * [0 1]

# c) SAME DIMENSION SAME RANK
from vec import Vec
from dimension import independence
from vector import vecutil
from matrix import matutil

# 6.7.6
def my_is_independent(L):
  n = len(L)
  rank = independence.rank(L)
  return n == rank

a = [vecutil.list2vec([1, 2, 3]), vecutil.list2vec([2,2,2])]
assert(my_is_independent(a) == True)
assert(my_is_independent([vecutil.list2vec(v) for v in [[2, 4, 0], [8, 16, 4], [0, 0, 7]]]) == False)

# 6.7.7
def my_rank(L):
  while not independence.is_independent(L):
    L.pop()
  return len(L)

my_rank_test = [vecutil.list2vec(v) for v in [[1, 2, 3], [4, 5, 6], [1.1, 1.1, 1.1]]]
assert(my_rank(my_rank_test) == 2)


# 6.7.8
# if a vector has dimension n then it has a basis of size n. All vector spaces have basis of the same size, so any other vector could be expressed by some lienar combination of the basis vectors, therefore any n + 1 vectors will be linearly dependent

# 6.7.11

def direct_sum_decompose(U_basis, V_basis, w):
  from solver import solve
  full_basis = U_basis + V_basis
  combination_vector = solve(full_basis, w)

  u = [0 for c in w]
  for i in len(U_basis):
    u += (combination_vector[i]) * U_basis[i]

  v = [0 for c in w]
  for i in len(V_basis):
    moved_index = len(U_basis + i)
    v += (combination_vector[moved_index] * V_basis[i])
  return u, v

# 6.7.12

def is_invertible(M):
  # must be square
  if (M.D[0] != M.D[1]):
    return False
  # rank must equal domain dimension
  if (M.D[0] != independence.rank(M)):
    return False
  return True

# 6.7.13

def find_matrix_inverse(A):
  from solver import solve
  assert(len(A.D[0]) == len(A.D[1]))
  n = len(A.D[1])
  i = matutil.identity(A.D, n)
  inverse = {}
  for c in A.D[1]:
    inverse[c] = solve(A, i[c])
  
  return matutil.coldict2mat(inverse)

# 6.7.14

def find_triangular_matrix_inverse(A):
  assert(len(A.D[0]) == len(A.D[1]))
  n = len(A.D[1])
  i = matutil.identity(A.D, n)
  inverse = {}
  for c in A.D[1]:
    inverse[c] = independence.triangular_solve(A, i[c])
  return matutil.coldict2mat(inverse)