from matrix.matutil import listlist2mat
from matrix.bitutil import mat2bits, bits2mat
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
encoded = G * message1

print("the encoding of the message [one, 0, 0, one] is ", encoded)

def extract_original(encoded):
  decoded = [encoded[6], encoded[5], encoded[4], encoded[2]]
  return decoded

print("\ndecoded %s" % extract_original(encoded))

# we know that the kernel is trivial because G's row space spans GF(1)^4, and therefore that
# G represents a one-to-one function, and therefore that it is invertible

# heres the matrix dude!

G_INVERSE = listlist2mat([
    [zero, zero, zero, zero, zero, zero, one],
    [zero, zero, zero, zero, zero, one, zero],
    [zero, zero, zero, zero, one, zero, zero],
    [zero, zero, one, zero, zero, zero, zero]
])

print("\ndecoded by inversion: %s" % (G_INVERSE * encoded))
