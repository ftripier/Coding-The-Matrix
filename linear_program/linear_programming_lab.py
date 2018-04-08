from linear_program import cancer_data
from matrix import matutil
from vec import Vec

training = cancer_data.read_training_data('linear_program/train.data', {'area(worst)', 'smoothness(worst)', 'texture(mean)'})

def main_constraint(i, a_i, d_i, features):
  d_i_sign = 1 if d_i >= 0 else -1
  constraint_vector = {
    d: d_i_sign * a_i[d] for d in features
  }
  constraint_vector.update({
    'gamma': -d_i_sign,
    i: 1
  })
  return constraint_vector

def nonneg_constraint(i):
  return {i: 1}

def make_matrix(feature_vectors, diagnoses, features):
  ids = {i for i in feature_vectors}
  D = ids | features | {'gamma'}
  constraints = {
    d: Vec(D, main_constraint(d, feature_vectors[d], diagnoses[d], features)) for d in feature_vectors
  }
  constraints.update({
    -d: Vec(D, nonneg_constraint(d)) for d in feature_vectors    
  })
  return matutil.rowdict2mat(constraints)

def right_hand_side_vector(ids):
  neg = {-i for i in ids}
  constraints = {
    i: 1 for i in ids
  }
  constraints.update({
    i: 0 for i in neg    
  })
  return Vec(ids | neg, constraints)

def objective_function(ids, features):
  D = ids | features | {'gamma'}
  return Vec(D, {i: 1 for i in ids})

feature_vectors = matutil.mat2rowdict(training[0])
features = training[0].D[1]
diagnoses = training[1]
ids = training[0].D[0]
A = make_matrix(feature_vectors, diagnoses, features)
b = right_hand_side_vector(ids)
c = objective_function(ids, features)


