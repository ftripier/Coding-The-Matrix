from vector.vec import Vec
from matrix.mat import Mat
from matrix import matutil, solver

# def zero_matrix(i, j):
#   return [[0 for a in range(i)] for b in range(j)]

# def zero_column_matrix(i, j):
#   return [[(a - b) for a in range(j)] for b in range(i)]

# M = Mat(
# ({'a', 'b'}, {'@', '#', '?'}),
# {
#    ('a', '@'): 1,
#    ('a', '#'): 2,
#    ('a', '?'): 3,

#    ('b', '@'): 10,
#    ('b', '#'): 20,
#    ('b', '?'): 30,
# })
# class Mat:
#   def __init__(self, labels, function):
#     self.D = labels
#     self.f = function

# def identity(D): return Mat(D, {(d, d): 1 for d in D})

# def mat2rowdict(M):
#   return {r: Vec(M.D[1], {c: M[r, c] for c in M.D[1]}) for r in M.D[0]}

# def mat2codict(M):
#   return {c: Vec(M.D[0], {r: M[r, c] for r in M.D[0]}) for c in M.D[1]}

# 4.6.3
def determine_consumption():
  D = {'radio', 'sensor', 'memory', 'CPU'}
  v0 = Vec(D, {'radio': .1, 'CPU':.3})
  v1 = Vec(D, {'sensor': .2, 'CPU':.4})
  v2 = Vec(D, {'memory': .3, 'CPU':.1})
  v3 = Vec(D, {'memory': .5, 'CPU':.4})
  v4 = Vec(D, {'radio': .2, 'CPU':.5})

  b = Vec({0, 1, 2, 3, 4}, {0: 140.0, 1: 170.0, 2: 60.0, 3: 170.0, 4:250.0})
  A = matutil.rowdict2mat([v0, v1, v2, v3, v4])
  rate = solver.solve(A, b)