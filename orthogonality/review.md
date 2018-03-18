* What does it mean to normalize a vector?
Make it length 1 boy

* What does it mean for several vectors to be mutually orthogonal?
They're all orthogonal to each other? What a question. If they're mutually orthogonal they form a basis, so that's nice.

* What are orthonormal vectors? What is an orthonormal basis?
I'm guessing this means they're mutually orthogonal normalized vectors, and an orthonomral basis is just a basis of orthonormal vectors. THe standard basis is an orthonormal basis.

* How can one find the vector in Span {v1, ..., vn} closest to b?

by finding the parallel component of v with respect to the Span. this basically works by an argument similar to the one explored in inner product, where we decompose a vector b into its perpendicular and parallel components like so:

b = b^parallel + b^perpendicular.

b - v^perpendicular is an arrow touching the basis directly beneath b, and equivalently, b^parallel.

* How does one find the projection of a vector v orthogonal to several mutually orthogonal vectors v1, ..., vn?

one can simply iteratively apply the equation
b = b - project_along(b, v^i).

This works because at each step i, b is orthogonal to every vector v^n where n <- (0, i).

* How does one find vectors that
(i) span the same space as v1, ..., vn
(ii) are mutually orthogonal
by running the orthogonalization algorithm. iteratively populate a set with the loop invariant that the set is mutually orthogonal by projecting the new vector onto the currently mutually orthogonal set of vectors, and adding the resulting vector instead.


* What is a column-orthogonal matrix? An orthogonal matrix?

A column-orthogonal matrix is a matrix with an orthonormal column space, i.e. the the column vectors are mutually orthogonal and of norm 1.

An orthogonal matrix is a square column-orthogonal matrix.

* What is the inverse of an orthogonal matrix?

Just get its transpose boyyy

This works by studying their multiplication. If we have Q^t*Q, then each entry ij will be the dot product of Qi * Qi, which, as the inner product of two norm one vectors, will be one. Every multiplication Qi * Qj will be zero, as the inner product of two orthogonal vectors.

* How can you use matrix-vector multiplication to find the coordinate representation of a vector in terms of an orthonormal basis?

Presumably if you make a matrix whose column space is drawn from the orthonormal basis, it suffices to multiply that matrix against the vector and use the ensuing vector as the coordinates.

Actual Answer:

I was misled by the term "coordinate representation". One would have to multiply the transpose of said matrix against the vector (or the vector against the matrix) to retrieve the coordinate representation. Multiplying the coordinates against the column orthogonal matrix retrieves the parallel projection of the vector against the basis.

* What is the QR factorization of a matrix?

The QR factorization describes an algorthm that decomposes a matrix A with linearly independent column space into a product of two matrices Q and R, where Q represents the column-orthogonal representation of A multiplied against R, the upper-triangular coefficient matrix whose rows have been multiplied against the non-unit norms of A.

* How can the QR factorization be used to solve a matrix equation?

Suppose you have a matrix vector equation

Ax = b

You can transform it into
QRx = b

by the QR factorization.

Then, one multiplies both sides by Qt, giving you

R*x = Qt*b

Because Qt and Q = I because Q is an orthogonal matrix.

b' = Qb, because both sides of the equation are known here.

R*x = b', and we can solve this using backwards substitution since R is an upper triangular matrix. 

* How can the QR factorization be computed?

The augmented orthogonalization procedure runs each column a of a matrix A through a process that returns the orthognalized vector and the coefficients of the lienar equation that restores the original vector a. From these components, one can make a matrix Q from the column space of the orthogonalized vectors, and the upper triangular matrix R of the components, with rows scaled by the norms of corresponding columns in A.

* How can the QR factorization be used to solve a least-squares problem?

Basically, the closest point in the column space of A to b will be the parallel component of b with respect to Col A.

The least squares problem finds the vector that minimizes the norm of applying a linear transformation A to a vector, and a goal vector b.

Solving the QR factorization of A returns a matrix such that

R * solution = Q^T*b

Multiplied by Q gives us
Q * R * solution = Q * Q^t * b

We know that Q * Q^t * b is the parallel component of b with respect to A (which is b in the event that Q is an orthogonal matrix and thus that its transpose is its own inverse) by the lienar combinations definition of matrix-vector multiplication, and by a trick of inner product lienarity appleid to the parallel and perpendicular decomposition of the vector (we add the inner product of the paralle component to the perpendicular component multiplied against every row of Q * Q^t, and we know the inner product of the perpendicular projection will be zero since it is by definition orthogonal).

* How can solving a least-squares problem help in fitting data to a line or quadratic?

In general, given a matrix of vectors of training points, one can multiply the matrix against a vector of weights to find a vector of predictions, and use the least squares problem to define a metric space such that one can find the weights that minimize the error of the regression line for linear solutions.

For quadratic regression, we need to regress to three uknowns for the generalized quadratic, equation f(x) = u0 + u1*x + u2*x^2. The application of least squares to the quadratic applied to this line in that it defines a metric space. We'd be trying to minimize the norm of

[
  [1, x1, x1^2]
  ...
  [1, xn, xn^2]
] * [u0, u1, u2]
- [y1, ..., yn]

* How can solving a least-squares problem help to get more accurate output?

If we have a linear equation with no solution, we use least squares to find the closest approximation. You can take a linear equation with a solution, consider more dimensions from the real world in your model, and instead use least squares to find the closest approximate solution.

* What is the orthogonal complement?

The orthogonal complement of a subspace U of a vector space W is a subpace of W, V, such that for every vector u in U, every vector v in V, v is orthogonal to u.

* What is the connection between orthogonal complement and direct sum?

If two vector subspaces are orthogonal complements, then their direct sum forms their original vector space. Because they're orthogonal complements, they only share the zero vector, and therefore have direct sum defined on them. They form the original space because the direct sum is a subset of the original space  (being composed of two subspaces), and the original space is a subset as a result of having all of its vectors parallel and perpendicular components espoused in either operand of the direct sum.

