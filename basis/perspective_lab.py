from vector import vecutil
from vec import Vec
from mat import Mat

C = {'x1', 'x2', 'x3'}
R = {'y1', 'y2', 'y3'}

def move2board(y):
  return vecutil.list2vec([
    y['y1']/y['y3'],
    y['y2']/y['y3'],
    y['y3']/y['y3'],
  ])

def make_equations(x1, x2, w1, w2):
  u = vecutil.list2vec([
    (w1 * x1),
    (w1 * x2),
    w1,
    -x1,
    -x2,
    -1
  ])
  v = vecutil.list2vec([
    (w2 * x1),
    (w2 * x2),
    w2,
    -x1,
    -x2,
    -1
  ])
  return [u, v]