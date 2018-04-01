from matrix import matutil
from vector import vecutil
from vec import Vec
import math
import pagerank_test
import pagerank

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
    quotient = 1/links[c]
    for r in rows:
      entry = L[(r, c)]
      if entry:
        L[(r, c)] = quotient
  return L

def load_small_links():
  global rows
  global columns
  rows = pagerank_test.small_links.D[0]
  columns = pagerank_test.small_links.D[1]
  return pagerank_test.small_links

small_links = load_small_links()
test_A1 = make_Markov(small_links)

assert(test_A1 == (
  matutil.coldict2mat({
    1: Vec(rows, {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }),
    2: Vec(rows, {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0 }),
    3: Vec(rows, {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0 }),
    
    4: Vec(rows, {1: 0.5, 2: 0.5, 3: 0, 4: 0, 5: 0, 6: 0 }),
    5: Vec(rows, {1: 0, 2: 1/3, 3: 0, 4: 1/3, 5: 0, 6: 1/3 }),
    6: Vec(rows, {1: 0, 2: 0.5, 3: 0, 4: 0, 5: 0.5, 6: 0 }),    
  })
))

def power_method(A1, x):
  initial = Vec(columns, {d: 1.0 for d in columns})
  n = len(rows)
  for i in range(x):
    before_norm = math.sqrt(initial*initial)
    tot = 0
    for d in columns:
      tot += initial[d]
    avg = tot/n
    term_avg = 0.15 * avg
    a1Term = 0.85 * (A1 * initial)
    a2Term = Vec(columns, {d: term_avg for d in columns})
    initial = a1Term + a2Term
    after_norm = math.sqrt(initial*initial)
    print("ratio: %s" % (before_norm/after_norm))
  return initial

def load_corpus():
  global rows
  global columns
  links = pagerank.read_data()
  rows = links.D[0]
  columns = links.D[1]
  return links


links = load_corpus()

def wikigoogle(w, k, p):
  related = pagerank.find_word(w)
  related.sort(key=lambda x:p[x], reverse=True)
  return related[:k]

wiki_A1 = make_Markov(links)
pagerank_eigenvector = power_method(wiki_A1, 10)
wikigoogle('jordan', 10, pagerank_eigenvector)
