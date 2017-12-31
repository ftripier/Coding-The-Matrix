- Transpose of the matrix is the mapping of row space to column space and vice-versa
- Sparsity of a matrix is the proportion of zero-valued entries in it. U can just ignore zero usually so if you're trying to compute a lot you can do that for really sparse matrices bye man.
- linear combination definition of matrix-vector multiplication is that a matrix-vector multiplication yields a vector with components from the  linear combination of vector components as scalars with the matrix columns.
- linear combination definition of vector-matrix multiplication is that a vector-matrix multiplication yields a vector with components from the linear combination of vector components as scalars with the matrix rows.
- dot-product definition of matrix-vector multiplication is that a matrix-vector multiplication yields a vector with components from the dot product of the vector with each matrix row.
- dot-product definition of vector-matrix multiplication is that a vector-matrix multiplication yields a vector with components from the dot product of the vector with each matrix column.
- An identity matrix is a matrix with the standard basis vectors in both column and row space.
- an upper-triangular matrix has no nonzero values in the lower diagonal.
- A diagonal matrix only has nonzero values on its diagonal.
- A linear function is a function that obeys linearity e.g.
 A * f(x) = f(A * x) and f(x) + f(y) = f(x + y)
- A linear function f: F^n -> F^m can be represented by a matrix R X C such that f(x) = M * x for every vector in F^C. I'm not sure what the second way is...
- The null space is the vector space of vectors that yield zero when input into the matrix's corresponding linear function, the column space is the span of the column, and the row space is the span of the rows.
- the matrix-vector definition of matrix-matrix multiplication is
  column s of AB = A * (column s of B)
- the vector-matrix definition of matrix-matrix multiplication is
  row r of AB = (row r of A) * B
- the dot-product definition of matrix-matrix multiplication is
  entry ij of AB = row i of A * column j of B
- Associativity of matrix-matrix multiplication is that matrix-matrix multiplication is associative what do you want man
- matrix-vector and vector-matrix multiplication can be represented by matrix-matrix multiplication by assuming the vector is either a one column or one row matrix.
- the outer product of two vectors is the component wise multiplication of the vectors
- a dot-product is just matrix-matrix multiplication of a one row matrix against a one column matrix
- the inverse of matrix A is a matrix B such that A * B = I
- one criterion for two matrices being inverses is their fuckin definition that I just wrote
