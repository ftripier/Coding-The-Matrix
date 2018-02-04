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