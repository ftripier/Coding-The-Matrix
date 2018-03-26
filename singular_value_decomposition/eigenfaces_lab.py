import eigenfaces
import image
import vec

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


def import_faces():
  imported = eigenfaces.load_images('singular_value_decomposition/faces')
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

faces = import_faces()
centroid = compute_image_centroid(faces)
image.image2display(vector2image(centroid))
