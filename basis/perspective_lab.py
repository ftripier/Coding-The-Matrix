from vector import vecutil
from matrix import matutil
from vec import Vec
from mat import Mat
import solver

C = {'x1', 'x2', 'x3'}
R = {'y1', 'y2', 'y3'}
D = {
  ('y1', 'x1'),
  ('y2', 'x1'),
  ('y3', 'x1'),

  ('y1', 'x2'),
  ('y2', 'x2'),
  ('y3', 'x2'),

  ('y1', 'x3'),
  ('y3', 'x3'),    
  ('y2', 'x3')
}

def move2board(y):
  return Vec(
      {'y1', 'y2', 'y3'},
      {
        'y1': y['y1']/y['y3'],
        'y2': y['y2']/y['y3'],
        'y3': y['y3']/y['y3'],
      }
    )

def make_equations(x1, x2, w1, w2):

  u = Vec(D, {
    ('y3', 'x1'): w1 * x1,
    ('y3', 'x2'): w1 * x2,
    ('y3', 'x3'): w1,
    ('y1', 'x1'): -x1,
    ('y1', 'x2'): -x2,
    ('y1', 'x3'): -1
  })
  v = Vec(D, {
    ('y3', 'x1'): w2 * x1,
    ('y3', 'x2'): w2 * x2,
    ('y3', 'x3'): w2,
    ('y2', 'x1'): -x1,
    ('y2', 'x2'): -x2,
    ('y2', 'x3'): -1
  })
  return [u, v]

w = Vec(D, {
  ('y1', 'x1'): 1
})

l0, l1 = make_equations(358, 36, 0, 0)
l4, l5 = make_equations(329, 597, 0, 1)
l2, l3 = make_equations(592, 157, 0, 1)
l6, l7 = make_equations(580, 483, 0, 1)

L = matutil.rowdict2mat({
  0: l0,
  1: l1,
  2: l2,
  3: l3,
  4: l4,
  5: l5,
  6: l6,
  7: l7,
  8: w,    
})

b = vecutil.list2vec([0, 0, 0, 0, 0, 0, 0, 0, 1])

print(solver.solve(L, b))
