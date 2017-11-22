from plotting import plot
from math import e, pi

POINTS = [2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j]
CONJUGATES = [x.conjugate() for x in POINTS]
TRANSLATED = {x + (-2 - 2j) for x in POINTS}
ROTSCALED = {(x * 0.5j) + (2  - 1j) for x in POINTS}

def w (n):
  return e ** (2 * pi * 1j /n)

complexes = {w(x) for x in range(1, 21)}

def rotate(z, theta):
  return z * (e ** (theta * 1j))

def rotate_points(theta):
  return { rotate(x, theta) for x in POINTS }

rads = [ x * (pi * 0.25) for x in range(8) ]

# plot(rotate_points(rads[1]), 4)


