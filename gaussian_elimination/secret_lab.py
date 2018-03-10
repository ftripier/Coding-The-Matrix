from GF2 import one
from vector.vecutil import list2vec
from dimension import independence
from matrix import bitutil, matutil
import random

a0 = list2vec([one, one, 0, one, 0, one])
b0 = list2vec([one, one, 0, 0, 0, one])

def randGF2():
  return random.randint(0, 1) * one

def create_random_vector(n):
  return list2vec([randGF2() for i in range(n)])

def choose_secret_vector(s, t):
  """
  input: GF(2) field elements s and t (i.e bits)
  output: a random 6-vector u such that a0 * u = s and b0 * u = t
  """
  u = create_random_vector(6)
  while a0 * u != s and b0 * u != t:
    u = create_random_vector(6)
  
  return u
s = 0
t = one
u = choose_secret_vector(s, t)
print(u)

def generate_remaining_vectors():
  def generate_candidates():
    return [create_random_vector(6) for i in range(8)]
  
  def choose_three_independent(L):
    n = len(L)
    for i in range(n):
      for j in range(i + 1, n):
        for k in range(j + 1, n):
          if not independence.is_independent([L[i], L[j], L[k]]):
            return False
    return True

  candidates = generate_candidates()
  all_vectors = [a0, b0] + candidates

  while not choose_three_independent(all_vectors):
    candidates = generate_candidates()

  return candidates

coded = "memelover"
codedbits = bitutil.str2bits(coded)

U = matutil.coldict2mat({
  column: choose_secret_vector(codedbits[column][0], codedbits[column][1]) for column in codedbits.D[1]
})

remaining = generate_remaining_vectors()

A = matutil.rowdict2mat({
  0: a0,
  1: b0,
  2: remaining[0],
  3: remaining[1],
  4: remaining[2],
  5: remaining[3],
  6: remaining[4],
  7: remaining[5],
})

shares = A * U
