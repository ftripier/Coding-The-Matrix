import math
import factoring_support
import echelon
import random
from GF2 import one
from vec import Vec
from matrix import matutil

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

# print(task782())

def task784():
  primeset = {2, 3, 5, 7, 11, 13}
  print(factoring_support.dumb_factor(12, primeset))
  print(factoring_support.dumb_factor(154, primeset))
  print(factoring_support.dumb_factor(2*3*3*3*11*11*13, primeset))
  print(factoring_support.dumb_factor(2*17, primeset))
  print(factoring_support.dumb_factor(2*3*5*7*19, primeset))

# task784()

def int2GF2(i):
  if (i % 2) == 0:
    return 0
  else:
    return one

def make_Vec(primeset, factors):
  return Vec(primeset, {pair[0]: int2GF2(pair[1]) for pair in factors})

assert(make_Vec({2, 3, 5, 7, 11}, [(3, 1)]) == Vec({3, 2, 11, 5, 7}, {3: one}))

def find_candidates(N, primeset):
  roots = []
  rowlist = []

  def can_be_factored_completely(x, primes):
    factors = factoring_support.dumb_factor(x, primes)
    return len(factors) > 0

  x = factoring_support.intsqrt(N) + 2
  while (len(roots) < len(primeset) + 1):
    candidate = x * x - N
    if can_be_factored_completely(candidate, primeset):
      roots.append(x)
      rowlist.append(make_Vec(primeset, factoring_support.dumb_factor(candidate, primeset)))
    x += 1
  
  return roots, rowlist
  
N = 2419
test_roots, test_rows = find_candidates(N, factoring_support.primes(32))

test_divisor = gcd((53 * 77) - (2 * 3 * 3 * 5 * 13), N)
assert((N % test_divisor) == 0)

M = echelon.transformation_rows(test_rows)

def find_a_and_b(v, roots, N):
  """
   a vector v
   the list roots
   the integer N to factor

   computes a pair of integers such that a**2 - b**2 is
   a multiple of N
  """
  alist = [roots[i] for i in v.D if v[i] != 0]
  a = factoring_support.prod(alist)
  c = factoring_support.prod([x * x - N for x in alist])
  assert(c > 0)
  b = factoring_support.intsqrt(c)
  assert(b * b == c)
  return (a, b)

last_row_of_M = M[len(test_rows) - 1]
second_to_last_row_of_M = M[len(test_rows) - 2]

def has_non_trivial_divisor(a, b):
  divisor = gcd(a, b)
  assert(divisor != 1 and divisor != a and divisor != b)

try:
  a, b = find_a_and_b(last_row_of_M, test_roots, N)
  has_non_trivial_divisor(a - b, N)
except AssertionError:
  a, b = find_a_and_b(second_to_last_row_of_M, test_roots, N)
  has_non_trivial_divisor(a - b, N)

N = 2461799993978700679
primelist = factoring_support.primes(10000)
roots, rowlist = find_candidates(N, primelist)
M = echelon.transformation_rows(rowlist, sorted(primelist, reverse=True))
v = M[len(rowlist) - 1]
a, b = find_a_and_b(v, roots, N)
has_non_trivial_divisor(a, b)
