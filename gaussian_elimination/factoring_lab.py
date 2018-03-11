import math
import factoring_support
import random
from GF2 import one
from vec import Vec

def is_integer(n):
  return math.floor(n) == n

def root_method(N):
  """
  1. initialize integer a to be an integer greater than root(N)
  2. check if root(a^2 - N) is an integer
  3. is so, let b = root(a^2 - N). return a - b.
  4. If not, repeat with the next greater value of a.
  """
  a = math.floor(factoring_support.intsqrt(N)) + 1
  while True:
    b = factoring_support.intsqrt(a**2 - N)
    if is_integer(b):
      return a - b
    a += 1

assert(root_method(55))
assert(root_method(77))
assert(root_method(146771))
assert(root_method(118))

def gcd(x, y): return x if y == 0 else gcd(y, x % y)
r = random.randint(100, 500)
s = random.randint(1000, 50000)
t = random.randint(20000, 200000)

a = r * s
b = s * t

d = gcd(a, b)
assert((a % d) == 0)
assert((b % d) == 0)
assert(d >= s)

def task782():
  N = 367160330145890434494322103
  a = 67469780066325164
  b = 9429601150488992
  assert(((a*a - b*b) % N) == 0)
  return gcd(a - b, N)

print(task782())

def task784():
  primeset = {2, 3, 5, 7, 11, 13}
  print(factoring_support.dumb_factor(12, primeset))
  print(factoring_support.dumb_factor(154, primeset))
  print(factoring_support.dumb_factor(2*3*3*3*11*11*13, primeset))
  print(factoring_support.dumb_factor(2*17, primeset))
  print(factoring_support.dumb_factor(2*3*5*7*19, primeset))

task784()

def int2GF2(i):
  if (i % 2) == 0:
    return 0
  else:
    return one

def make_Vec(primeset, factors):
  return Vec(primeset, {pair[0]: int2GF2(pair[1]) for pair in factors})

assert(make_Vec({2, 3, 5, 7, 11}, [(3, 1)]) == Vec({3, 2, 11, 5, 7}, {3: one}))