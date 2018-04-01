from matrix import matutil
from vector import vecutil
from vec import Vec
import pagerank_test

rows = set()
columns = set()

def add_a2(w):
  D = w.D
  n = len(D)
  avg = sum(w)/n
  return Vec(D, {d: w[d] + avg for d in D})

def find_num_links(L):
  """
  input: L, a matrix with all nonzero entries 1, representing
  the article link structure. Specifically entry rc is 1 if
  article c points to article r.

  output: a vector num_links whose label set is the column-label
  set of L, such that, for each column-label c, entry c of num_links
  is the number of nonzero entries in column c of L.
  """
  Lt = L.transpose()
  sum_vec = Vec(rows, {d:1.0 for d in rows})
  return Lt * sum_vec

def make_Markov(L):
  """ make  L work like A1 via mutation"""
  links = find_num_links(L)
  for c in columns:
    for r in rows:
      entry = L[(r, c)]
      if entry:
        L[(r, c)] = 1/links[c]
  return L

rows = pagerank_test.small_links.D[0]
columns = pagerank_test.small_links.D[1]
assert(make_Markov(pagerank_test.small_links) == (
  matutil.coldict2mat({
    1: Vec(rows, {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }),
    2: Vec(rows, {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0 }),
    3: Vec(rows, {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0 }),
    
    4: Vec(rows, {1: 0.5, 2: 0.5, 3: 0, 4: 0, 5: 0, 6: 0 }),
    5: Vec(rows, {1: 0, 2: 1/3, 3: 0, 4: 1/3, 5: 0, 6: 1/3 }),
    6: Vec(rows, {1: 0, 2: 0.5, 3: 0, 4: 0, 5: 0.5, 6: 0 }),    
  })
))
  

