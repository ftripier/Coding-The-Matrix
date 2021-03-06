1. What is echelon form?

360 no scope answer:

Echelon form is a form wherein a set of vectors has a preorder of leading nonzero terms. In the set of vectors, the first vector would have its first nonzero term in the first element, the second in its second, etc.

Actual:

The above is correct, with some nuance: echelon form is for a matrix's rows (not any set of vectors), and the next leading nonzero term can be in any position that exceeds its predecessor's.

2. How can a matrix be converted into echelon form by multiplication by an invertible matrix?

Since echelon form reduces to a representation of the matrix's row space basis, it suffices to apply row-addition matrices to eliminate leading nonzero terms. These row-addition matrices can be multiplied into one, as they are all lienar transformations.

This process works, because, by the lienar combinations definition of a vector-matrix multiplication, the rowspace of a transformed matrix is contained within the rowspace of the original matrix, and vice-versa. Since we have existensial proof that we eliminate leading nonzero terms of rows via the row-addition transform, we can be assured that row-space has been preserved in row-echelon reduction.

3. How can Gaussian Elimination be used to find a basis for the null space of a matrix?

Given a matrix M for Matrix A such that MA = U where U is the reduced row echelon form of A, the null rows of U correspond to the basis of the null space of matrix A. This follows from the fact that the non-null rows will be the basis of the row space, and the rank of row space equals the rank of column space, and the rank of column space plus the rank of null space equals the rank of the image space.

4. How can Gaussian Elimination be used to solve a matrix-vector equation when the matrix is invertible?

When reduced to row-echelon form, a matrix's inverse is easily identifiable. Given the inverse M-1, you can solve the equation
M-1(MA)x = M-1(Mb) because the inverses will cancel out, leaving you with x = M-1Mb, with all the uknowns on one side.
