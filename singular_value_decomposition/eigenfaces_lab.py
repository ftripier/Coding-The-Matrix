import eigenfaces
import image
import math
import vec
import svd
from matrix import matutil
from vector import vecutil

def image2vector(image):
  D = set()
  F = {}
  for i in range(len(image)):
    row = image[i]
    for j in range(len(row)):
      pixel = row[j]
      coord = (i, j)
      D.add(coord)
      F[coord] = pixel
  return vec.Vec(D, F)

def vector2image(vector):
  rows = 0
  columns = 0
  for coord in vector.D:
    rows = max(coord[0], rows)
    columns = max(coord[1], columns)
  image = [[0 for j in range(columns + 1)] for i in range(rows + 1)]
  for p in vector.f:
    pixel = vector.f[p]
    image[p[0]][p[1]] = pixel
  
  return image


def import_faces(source, n=20):
  imported = eigenfaces.load_images(source, n)
  return {
    i: image2vector(imported[i]) for i in imported
  }

def compute_image_centroid(images):
  """image is a listlist"""
  final = None
  for i in images:
    if final is None:
      final = images[i]
    else:
      final = final + images[i]
  
  return (1/len(images)) * final

faces = import_faces('singular_value_decomposition/faces')
centroid = compute_image_centroid(faces)
# image.image2display(vector2image(centroid))

centered_image_vectors = {
  k: faces[k] - centroid for k in faces
}

def norm(v):
  return math.sqrt(v * v)


A = matutil.rowdict2mat(centered_image_vectors)

U, Sigma, V = svd.factor(A)
Vt = V.transpose()
tenset = {i for i in range(10)}
Uten = matutil.submatrix(U, tenset, tenset)
Sigmaten = matutil.submatrix(Sigma, tenset, tenset)
Vten = matutil.submatrix(Vt, {i for i in range(10)}, Vt.D[1])

eigenfaces_basis = Uten*Sigmaten*Vten

def projected_representation(M, x):
  """
  input: a matrix M with orthonormal rows and a vector x with D from Col M
  output: the coordinate representation of the parallel of projection of x onto Row M
  """
  Mt = M.transpose()
  return Mt * x

def projection_length_squared(M, x):
  term = M * projected_representation(M, x)
  return term * term

def distance_squared(M, x):
  plen = projection_length_squared(M, x)
  x2 = x * x
  perpendicular = plen - x2
  return math.sqrt(perpendicular * perpendicular)

e_t = eigenfaces_basis.transpose()
classified_distances = [distance_squared(e_t, centered_image_vectors[x]) for x in centered_image_vectors]
print(classified_distances)

unclassified = import_faces('singular_value_decomposition/unclassified', 10)
# for k in unclassified:
#   vector = unclassified[k]
#   centered = vector - centroid
#   distance = distance_squared(e_t, centered)
#   print(distance)
#   image.image2display(vector2image(vector))

def project(M, x):
  return M * projected_representation(M, x)

image.image2display(vector2image(project(e_t, unclassified[1])))
image.image2display(vector2image(project(e_t, unclassified[2])))
image.image2display(vector2image(project(e_t, unclassified[3])))

# non-face
image.image2display(vector2image(project(e_t, unclassified[0])))



