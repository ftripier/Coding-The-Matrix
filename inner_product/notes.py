from matrix import matutil

def project_along(b, v):
  sigma = ((b*v)/(v*v)) if v*v > 1e-20 else 0
  return sigma * v

def project_orthogonal_1(b, v):
  return b - project_along(b, v)

def projection_matrix(v):
  # 1/||v|| * (v * v^T)
  v_trans = matutil.rowdict2mat({0: v})
  unit_length_projection = v * v_trans
  length_squared_inverse = 1/(v * v)
  return length_squared_inverse * unit_length_projection


# problem 8.3.16
# The rank of matrix M such that project_v(x) = M*x should be 1,
# because it is a linear combination of a rank 1 matrix another.