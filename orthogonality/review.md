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

* What is the inverse of an orthogonal matrix?

* How can you use matrix-vector multiplication to find the coordinate representation of a vector in terms of an orthonormal basis?

* What is the QR factorization of a matrix?

* How can the QR factorization be used to solve a matrix equation?

* How can the QR factorization be computed?

* How can the QR factorization be used to solve a least-squares problem?

* How can solving a least-squares problem help in fitting data to a line or quadratic?

* How can solving a least-squares problem help to get more accurate output?

* What is the orthogonal complement?

The orthogonal complement of a subspace U of a vector space W is a subpace of W, V, such that for every vector u in U, every vector v in V, v is orthogonal to u.

* What is the connection between orthogonal complement and direct sum?

If two vector subspaces are orthogonal complements, then their direct sum forms their original vector space. Because they're orthogonal complements, they only share the zero vector, and therefore have direct sum defined on them. They form the original space because the direct sum is a subset of the original space  (being composed of two subspaces), and the original space is a subset as a result of having all of its vectors parallel and perpendicular components espoused in either operand of the direct sum.

