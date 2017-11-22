import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
from vec import Vec
import vecutil

def addn(a, b):
  return [a[i] + b[i] for i in range(len(a))]

def scalar_mult(a, v):
  return [a * v[i] for i in range(len(v))]

def subn(a, b):
  return [a[i] - b[i] for i in range(len(a))]

def plot(points):
  fig = plt.figure(1)
  ax = SubplotZero(fig, 111)
  fig.add_subplot(ax)
  plt.ylim([-10, 10])
  plt.xlim([-10, 10])
  ax.plot(*zip(*points), marker='o', color='r', ls='')
  for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

  for direction in ["left", "right", "bottom", "top"]:
      ax.axis[direction].set_visible(False)
  plt.show()

def get_line_segment(u, v):
  return [addn(scalar_mult(i/100.0, u), scalar_mult(1 - (i/100.0), v)) for i in range(101)]

# class Vec:
#   def __init__(self, labels, function):
#     self.D = labels
#     self.f = function
  
#   def setitem(self, d, val):
#     self.f[d] = val

#   def getitem(self, d):
#     return self.f[d] if d in self.f else 0.0

#   def scalar_mult(self, alpha):
#     return Vec(self.D, {d: alpha * value for d, value in self.f.items()})

#   def add(self, v):
#     return Vec(self.D, {d: self.getitem(d) + v.getitem(d) for d in self.D})

#   def neg(self):
#     return self.scalar_mult(-1.0)

#   def list_dot(self):
#     return sum([self.getitem(d) * v.getitem(d) for d in self.D])

def list_dot(a, b):
  return sum([c * d for (c, d) in zip(a, b)])

def dot_product_list(needle, haystack):
  n = len(needle)
  return [list_dot(needle, haystack[i: i + n]) for i in range(len(haystack) - n)]

def triangular_solve_n(rowlist, b):
  D = rowlist[0].D
  n = len(D)
  assert D == set(range(n))
  x = vecutil.zero_vec(D)
  for i in reversed(range(n)):
    x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
  return x
