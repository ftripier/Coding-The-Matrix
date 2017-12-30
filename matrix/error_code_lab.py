from matrix.matutil import listlist2mat, coldict2mat
from matrix.bitutil import mat2bits, bits2mat, str2bits, bits2str, noise
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
    try:
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
    except KeyError:
        return list2vec([zero, zero, zero, zero, zero, zero, zero]) 

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

P = bits2mat(inBits)
PBits = mat2bits(P)
fromMat = bits2str(PBits)

print("\nbitutils matrix test: %s" % fromMat)

E = noise(P, 0.02)
perturbed = P + E
perturbedAsString = bits2str(mat2bits(perturbed))

print("\nperturbed: ", perturbedAsString)

encoded = G * P

print("\nencoded: %s" % encoded)

def decode_bits_mat(m):
    deencoded_mat = R * m
    as_string = bits2str(mat2bits(deencoded_mat))
    return as_string

print("\ndeencoded: %s" % decode_bits_mat(encoded))

perturbed_encoded = G * perturbed

print("\nperturbed-encoded: %s" % perturbed_encoded)

perturbed_deencoded = decode_bits_mat(perturbed_encoded)

print("perturbed-deencoded: %s" % perturbed_deencoded)

def correct(A):
    error_matrix = find_error_matrix(H * A)
    corrected = A + error_matrix
    return corrected

perturbed_corrected = correct(perturbed_encoded)
perturbed_corrected_deencoded = decode_bits_mat(perturbed_corrected)

error_matrix_test_string =  bits2mat(str2bits("test"))
print("LMAO %s" % error_matrix_test_string)

def get_column(m, colno):
    return G * list2vec([m[r, colno] for r in m.D[0]])

matrix_with_errors = coldict2mat({
    0: non_codeword,
    1: get_column(error_matrix_test_string, 0),
    2: get_column(error_matrix_test_string, 1),
    3: get_column(error_matrix_test_string, 2),
    4: get_column(error_matrix_test_string, 3),

    5: get_column(error_matrix_test_string, 4),
    6: get_column(error_matrix_test_string, 5),
    7: get_column(error_matrix_test_string, 6),
    8: get_column(error_matrix_test_string, 7)    
})

print("correct test: %s\n%s" % (decode_bits_mat(correct(matrix_with_errors)), decode_bits_mat(matrix_with_errors)))

print("perturbed corrected and decoded: %s" % perturbed_corrected_deencoded)
