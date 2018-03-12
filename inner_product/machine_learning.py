import cancer_data

def read_training_data():
  return cancer_data.read_training_data('inner_product/train.data')

A, b = read_training_data
