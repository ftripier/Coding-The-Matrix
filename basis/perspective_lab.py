from vector import vecutil
from vec import Vec
from mat import Mat

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