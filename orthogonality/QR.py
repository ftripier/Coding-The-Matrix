# Copyright 2013 Philip N. Klein
from dictutil import dict2list, list2dict
from matrix import matutil
mat2coldict = matutil.mat2coldict
coldict2mat = matutil.coldict2mat
from orthogonalize import aug_orthonormalize

def factor(A):
    col_labels = sorted(A.D[1], key=repr)
    Acols = dict2list(mat2coldict(A),col_labels)
    Qlist, Rlist = aug_orthonormalize(Acols)
    #Now make Mats
    Q = coldict2mat(Qlist)
    R = coldict2mat(list2dict(Rlist, col_labels))
    return Q,R
