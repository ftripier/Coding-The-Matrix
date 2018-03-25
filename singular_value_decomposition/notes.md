Lemma 11.1.1: The square of the Frobenius norm of A equals the sum of the squares of the rows of A.

Theorem 11.2.9 (Equation 11.8): The rank one matrix Â that minimizes ||A - Â||(F) is

Â = [
  [vector in span {v1} closest to a1],
  ...,
  [vector in span {v1} closest to am]
]

and
(||A - Â||(F))^2 = (||A||(F))^2 - first_singular_value_A^2

first_singular_value_A = ||Av1||
first_right_singular_vector = v1

Equation 11.11:
first_singular_value_A * u1 = Av1
Â = first_singular_value_A * u1 *v1^T

Definition 11.2.10: The first left singular vector of A is defined to be the vector u such that first_singular_value_A * u1 = A*v1, where first_singular_value_A and v1 are, respectively, the first singular value and the first right singular vector.


Theorem 11.1.11: The best rank-one approximation to A is first_singular_value_A*u1*v1^T

Lemma 11.3.6: Every row of A is in the span of the right singular vectors.

* What is one way to measure the distance between two matrices with the same row-labels and column-labels?

The frobenius norm, defined as the sum of the squares of the inner-product of each row-pair between the tow matrices.

* What are the singular values of a matrix? What are the left singular vectors and the right singular vectors?

The first singular value of a matrix A is the norm of that matrix multiplied against a vector v that minimizes the distance from it to the rows of that matrix. We dub this vector v1.

The first left singular vector is a norm one vector such that, when multiplied with the singular value, restores the vector A*v1.

The first right singular vector is just v1!

* What is the Singular Value Decomposition of a matrix?

The singular value decomposition is a decomposition of a matrix A into three matrices:

U*Sigma*V

where Sigma is a diagonal matrix of _singular values_ positive and of descending magnitude across the diagonal, and U and V are column orthogonal Matrix. From our definitions, V is the transpose of a matrix that draws from the rank(A) basis of vectors that minimize the distance to A (the right singular vectors), and U*sigma represents A*V, and thus the left singular vectors. We can think of U*sigma as being the decomposition of the left singular vectors in normalized vectors and their scalars.

* Given vectors a1,...,am how can we find a one-dimensional vector space closest to a1,...,am? Closest in what sense?

We find the norm 1 vector v that minimizes the distance to each vector a1, ..., am. The distance to each vector will be the perpendicular projection of a vector onto the span of v, which can be expressed as the square of the norm of the vector minus the square of the norm of the parallel projection (which comes from equational reasoning on the parallel-perpendicular decomposition of the vectors). The sums of the norm of the vectors reduces to the frobenius norm of a matrix A that draws its row space from them. Exploiting the unitary norm of v, the parallel components reduce to an inner product of the vectors of a with v - in sum represented as the squared norm of A*v.

So, we need v that minimizes frob_norm(A)^2 - norm(A*v)^2.

* Given in addition an integer k, how can we find the k-dimensional vector space closest to a1, ..., am?

Find the right singular vectors v1, ..., vm. The intuition for this draws from an inductive proof that proves each subsequent addition of vectors minimizes the distance of the vector space to A.
 
* Given a matrix A and an integer k, how can we find the rank-at-most-k matrix closest to A?

The rank-at-most-k matrix will be the drawn from the singular value decomposition ran up to dimension k.

* What use is finding this matrix?

Reduced rank matrices are much cheaper to store and multiply than their fully ranked counterparts.

* How can SVD be used to solve a least-squares problem?

By finding the singular value decomposition of a matrix, one finds that A*x = U*U^T*b via equational reasoning. Col U == Col A, and U^T*b is the coordinate representation of b in Col U, and U*U^T*B is the projection of b into Col U and therefore Col A. Finding this projection is the heart of the least squares problem.
