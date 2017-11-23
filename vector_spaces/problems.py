import vector.vecutil

def vec_select(veclist, k):
  return [vec for vec in veclist if vec[k] == 0.0]

def vec_sum(veclist, D):
  return sum(veclist, vector.vecutil.zero_vec)
