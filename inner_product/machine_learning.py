import cancer_data
import vec
from vector import vecutil
from matrix import matutil

def read_training_data():
  return cancer_data.read_training_data('inner_product/train.data')

def signum(u):
  """
  input: a Vec u
  output: the Vec v with the same domain as u such that
          +1 if u[d] >= 0
  v[d]= {
          -1 if u[d] < 0
  """
  return vec.Vec(u.D, {d: 1 if u[d] >= 0 else -1 for d in u.D})

assert(signum(vec.Vec({'A', 'B'}, {'A': 3, 'B': -2})) == vec.Vec({'A', 'B'}, {'A': 1, 'B': -1}))

def fraction_wrong(A, b, w):
  """
  input: An R x C matrix A whose rows are feature vectors,
  an R-vector b whose entries are +1 and -1,
  and a C-vector w.

  output: The fraction of row labels r of A such that
  the sign of (row r of A) * w differs from that of b[r]
  """
  Aw = A.transpose() * w
  signs = signum(Aw)
  result = ((signs * b) - len(b.D))/(-2 * len(b.D))
  return abs(result)


assert(fraction_wrong(
  matutil.rowdict2mat({
    0: vecutil.list2vec([1, 0, 0]),
    1: vecutil.list2vec([0, 1, 0]),
    2: vecutil.list2vec([0, 0, 1]),
  }), vecutil.list2vec([-1, -1, -1]), vecutil.list2vec([1, 1, 1])) == 1
)

A, b = read_training_data()
