from vector import vecutil
from matrix import matutil

def row_rearrange_algorithm(rowlist):
  col_label_list = sorted(rowlist[0].D, key=hash)
  new_rowlist = []
  rows_left = set(range(len(rowlist)))

  for c in col_label_list:
    rows_with_nonzero = [r for r in rows_left if rowlist[r][c] != 0]
    if rows_with_nonzero != []:
      pivot = rows_with_nonzero[0]
      new_rowlist.append(rowlist[pivot])
      rows_left.remove(pivot)
  
  return new_rowlist

def print_rowlist(rowlist):
  as_mat = matutil.rowdict2mat(rowlist)
  print("%s" % as_mat)

test = [
  [0, 2, 3, 4, 5],
  [0, 0, 0, 3, 2],
  [1, 2, 3, 4, 5],
  [0, 0, 0, 6, 7],
  [0, 0, 0, 9, 9]
]
a = [vecutil.list2vec(v) for v in test]

print_rowlist(row_rearrange_algorithm(a))
