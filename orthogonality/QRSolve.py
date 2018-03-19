import triangular
import QR
from matrix import matutil
from vec import Vec
from mat import Mat

def QR_solve(A, b):
  # Q*R*x = b
  # Q^T*Q*R*x = Q^t*b
  # I*R*x = Q^t *b
  Q, R = QR.factor(A)
  Q_t = Q.transpose()
  print(Q_t, b)
  b = Q_t * b
  sorted_labels = sorted(A.D[1], key=repr)
  rowlist = matutil.mat2rowdict(R)
  solved = triangular.triangular_solve(rowlist, sorted_labels, b)
  return solved

A = Mat(({'a', 'b', 'c'}, {'A', 'B'}), {
  ('a', 'A'): -1,
  ('a', 'B'): 2,
  ('b', 'A'): 5,
  ('b', 'B'): 3,
  ('c', 'A'): 1,
  ('c', 'B'): -2
})
b = Vec({'a', 'b', 'c'}, {'a': 1, 'b': -1})
x = QR_solve(A, b)
print(x)
