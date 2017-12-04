from matrix.matutil import listlist2mat
from vector.vecutil import list2vec
from GF2 import zero, one

G = listlist2mat([
  [one, zero, one, one],
  [one, one, zero, one],
  [zero, zero, zero, one],
  [one, one, one, zero],
  [zero, zero, one, zero],
  [zero, one, zero, zero],
  [one, zero, zero, zero],  
])

message1 = list2vec([one, zero, zero, one])

print("the encoding of the message [1, 0, 0, 1] is ", G * message1)

twobytwo = listlist2mat([
  [one, one],
  [zero, one]
])

inverse = listlist2mat([
  [one, zero],
  [one, zero]
])

print("GF(2) inverses", twobytwo * inverse)


