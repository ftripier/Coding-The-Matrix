import math
import image

def forward_no_normalization(v):
  """
  input: a list representing a vector in R^n
  where n is some power of two.


  output: a dictionary giving the representation
  of the input vector in terms of the unnormalized
  Haar wavelet basis. The key for the coefficient
  of wi^j should be the tuple (j, i).
  """

  D = {}
  while len(v) > 1:
    k = len(v)
    # v is a k-element list
    vnew = [(v[2*i] + v[2*i+1])/2 for i in range(k//2)] # compute downsampled 1-d image of size k//2 from v
    # vnew is a k//2-element list
    w = [(v[2*i] - v[2*i+1]) for i in range(k//2)] # compute unnormalized coefficients of basis for W(k/2)
    # w is a list of coefficients
    diaganolized_dict = {(k//2, i): w[i] for i in range(len(w))} # dictionary with keys (k//2, 0), (k//2, 1)... (k//2, k//2-1) and values from w
    D.update(diaganolized_dict)
    v = vnew

  # v is a 1-element list
  D[(0, 0)] = v[0]
  return D

assert(forward_no_normalization([1, 2, 3, 4]) == {
  (2, 0): -1,
  (1, 0): -2.0,
  (0, 0): 2.5,
  (2, 1): -1
})

def normalize_coefficients(n, D):
  """
    input: dimension n of original space, dictionary D of the form
    returned by forward_no_normalization
    
    output: D with coefficients normalized
  """
  return {
    d: (D[d] * math.sqrt(n/(4*d[0]))) if d != (0, 0) else D[d]*math.sqrt(n)
    for d in D
  }
assert(normalize_coefficients(4, forward_no_normalization([1, 2, 3, 4])) == {
  (2, 0): -0.7071067811865476,
  (1, 0): -2.0,
  (0, 0): 5.0,
  (2, 1): -0.7071067811865476
})

def forward(v):
  n = len(v)
  return normalize_coefficients(n, forward_no_normalization(v))

assert(forward([1, 2, 3, 4]) == {
  (2, 0): -math.sqrt(1/2),
  (2, 1): -math.sqrt(1/2),
  (1, 0): -2,
  (0, 0): 5  
})

def suppress(D, threshold):
  return {
    d: D[d] if abs(D[d]) >= threshold else 0
    for d in D
  }

assert(suppress(forward([1, 2, 3, 4]), 1) == {
  (2, 0): 0,
  (1, 0): -2.0,
  (0, 0): 5.0,
  (2, 1): 0
})

def sparsity(D):
  normalized = [1 if D[d] else 0 for d in D]
  k = len(normalized)
  return sum(normalized)/k

assert(sparsity(forward([1, 2, 3, 4])) == 1.0)
assert(sparsity(suppress(forward([1, 2, 3, 4]), 1)) == 0.5)

def unnormalize_coefficients(n, D):
  return {
    d: (D[d] / math.sqrt(n/(4*d[0]))) if d != (0, 0) else D[d]/math.sqrt(n)
    for d in D
  }

def backward_no_normalization(D):
  n = len(D)
  v = [D[(0, 0)]]# the one element list whose entry is the coefficient of b0^0
  while len(v) < n:
    new_v = []
    k = len(v)
    for i in range(k):
      # hand inverted the system of equations to find x and y
      # [[1, 1] * [x, y] = [2z, w]
      #  [1, -1]]
      z = v[i]
      w = D[(k, i)]
      x = w/2 + z
      y = -w/2 + z
      new_v += [x, y]
    v = new_v
  v.reverse()
  return v

assert(backward_no_normalization({
  (2, 0): -1,
  (1, 0): -2.0,
  (0, 0): 2.5,
  (2, 1): -1
}) == [4, 3, 2, 1])

def backward(D):
  n = len(D)
  return backward_no_normalization(unnormalize_coefficients(n, D))

assert(backward({
  (2, 0): -math.sqrt(1/2),
  (2, 1): -math.sqrt(1/2),
  (1, 0): -2,
  (0, 0): 5  
}) == [4, 3, 2, 1])

def dictlist_helper(dlist, k):
  return [d[k] for d in dlist]

def forward2d(listlist):
  D_list = [forward(row) for row in listlist]
  L_dict = {k: dictlist_helper(D_list, k) for k in D_list[0]}
  D_dict = {k: forward(L_dict[k]) for k in L_dict}
  return D_dict

def suppress2d(D_dict, threshold):
  return {
    k: suppress(D_dict[k], threshold) for k in D_dict
  }

def sparsity2d(D_dict):
  sparsities = [sparsity(D_dict[k]) for k in D_dict]
  return sum(sparsities)/len(sparsities)

def listdict2dict(L_dict, i):
  return {
    k:L_dict[k][i] for k in L_dict
  }

def listdict2dictlist(listdict):
  sorted_keys = sorted([k for k in listdict])
  first_object = listdict[sorted_keys[0]]
  return [listdict2dict(listdict, k) for k in range(len(first_object))]

def backward2d(dictdict):
  listdict = {k:backward(dictdict[k]) for k in dictdict}
  transposed = listdict2dictlist(listdict)
  result = [backward(k) for k in transposed]
  result.reverse()
  return result

assert(backward2d(forward2d([[1, 2, 3, 4]])) == [[4, 3, 2, 1]])

def import_flag():
  loaded = image.file2image('special_bases/flag.png')
  return image.color2gray(loaded)

def image_round(image):
  return [[abs(round(p)) if p < 255 else 255 for p in row] for row in image]

loaded = import_flag()
image.image2display(loaded)

wavelet = forward2d(loaded)
listlistrep = backward2d(wavelet)
rounded = image_round(listlistrep)

image.image2display(rounded)

compressed = suppress2d(wavelet, 2)
suppressed = 2
while sparsity2d(compressed) > 0.02:
  suppressed += 1
  compressed = suppress2d(wavelet, suppressed)
listlistrep = backward2d(compressed)
rounded = image_round(listlistrep)
image.image2display(rounded)



