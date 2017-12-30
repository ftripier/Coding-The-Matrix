from matrix.matutil import listlist2mat, coldict2mat
from matrix.bitutil import mat2bits, bits2mat, str2bits, bits2str
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

R = listlist2mat([
    [zero, zero, zero, zero, zero, zero, one],
    [zero, zero, zero, zero, zero, one, zero],
    [zero, zero, zero, zero, one, zero, zero],
    [zero, zero, one, zero, zero, zero, zero]
])

print("\ndecoded by inversion: %s" % (R * encoded))

H = listlist2mat([
    [zero, zero, zero, one, one, one, one],
    [zero, one, one, zero, zero, one, one],
    [one, zero, one, zero, one, zero, one],
])

print("\nHG is %s" % (H * G))

def find_error(error_syndrome):
    comparison = (error_syndrome[0], error_syndrome[1], error_syndrome[2])
    column_map = {
        (zero, zero, one): list2vec([one, zero, zero, zero, zero, zero, zero]),
        (zero, one, zero): list2vec([zero, one, zero, zero, zero, zero, zero]),
        (zero, one, one): list2vec([zero, zero, one, zero, zero, zero, zero]),

        (one, zero, zero): list2vec([zero, zero, zero, one, zero, zero, zero]),
        (one, zero, one): list2vec([zero, zero, zero, zero, one, zero, zero]),
        (one, one, zero): list2vec([zero, zero, zero, zero, zero, one, zero]),
        (one, one, one): list2vec([zero, zero, zero, zero, zero, zero, one]) 
    }
    return column_map[comparison]

non_codeword = list2vec([one, zero, one, one, zero, one, one])

print("\nnon codeword is: %s" % non_codeword)

non_codeword_error_syndrome = H * non_codeword

print("\nthe error syndrome is: %s" % non_codeword_error_syndrome)

non_codeword_error = find_error(non_codeword_error_syndrome)

print("\nThe error vector is: %s" % non_codeword_error)

correct_codeword = non_codeword + non_codeword_error

print("\n The correct codeword is: %s" % correct_codeword)

original_message = R * correct_codeword

print("\n The original message is: %s" % original_message)
# 
def find_error_matrix(S):
    print(S.D)
    return coldict2mat(
        {c: find_error(list2vec([S[r, c] for r in S.D[0]])) for c in S.D[1]}
    )

test_matrix = coldict2mat({
    0: list2vec([one, one, one]),
    1: list2vec([zero, zero, one])
})

print("\n find_error_matrix_test: %s" % (find_error_matrix(test_matrix)))

inBits = str2bits("I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it.")
fromBits = bits2str(inBits)

print("\nbitutils test: %s", (inBits, fromBits))

testBitsAsMat = bits2mat(inBits)
decodedTestBitsAsMat = mat2bits(testBitsAsMat)
fromMat = bits2str(decodedTestBitsAsMat)

print("\nbitutils matrix test: s", (testBitsAsMat, decodedTestBitsAsMat, fromMat))
