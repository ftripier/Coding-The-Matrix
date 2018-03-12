import cancer_data
import vec

def read_training_data():
  return cancer_data.read_training_data('inner_product/train.data')

def signum(u):
  """
  input: a Vec u
  output: the Vec v with the same domain as u such that
          +1 if u[d] >= 0
  v[d]= {
          -1 if u[d] < 0
  """
  return vec.Vec(u.D, {d: 1 if u[d] >= 0 else -1 for d in u.D})

assert(signum(vec.Vec({'A', 'B'}, {'A': 3, 'B': -2})) == vec.Vec({'A', 'B'}, {'A': 1, 'B': -1}))

A, b = read_training_data()
