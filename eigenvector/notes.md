* What must be true of Matrix A for Matrix A to have an eigenvalue?
It must be square.

* What are an eigenvalue and eigenvector of a matrix?

For all such scalars a, and vectors v such that A*v = a*v, a is an eigenvalue and v is an eigenvector.

* For what kind of problems are eigenvalues and eigenvectors useful?

Generally, knowing eigenvalues and eigenvectors amortizes the computational cost of compounding relations significantly.

* What is a diagonalizable matrix?

A diagonalizable matrix is a matrix that is similar to a matrix with nonzero values only across the diagonal. A matrix is simlar to another if there is a change of basis from it to the other, i.e. there is an invertible matrix S such that S-1*A*S = B. Similar matrices have the same eigenvalues. If a matrix is diagnolizable, then it has the same eigenvalues as its diagonal form, i.e. the eigenvalues are the nonzero elements of the diagonal matrix. If we multiply the diagnolizability equation by S we have A*S = S*B where B is the diagonal form. Since each nonzero entry of B is an eigenvalue, this equation implies that for each i, A times Column i of S equals an eigenvector times column i of S, and that column is therefore an eigenvector. So, if a matrix is diagonalizable, then its diagonal elements are eigenvalues and the columns of S linearly independent eigenvectors (they're linearly independent because S is invertible). Conversely, if any n*n matrix A has n linearly independent eigenvectors, one can show that it is diagonalizable by the following equational reasoning:

S is a matrix with column space drawn from the eigenvectors
^ is the diagonal matrix of the eigenvalues. A*S = S*^ by definition of an eigenvector A*v = ^i*v extrapolated to Matrix-Matrix multiplication Since S is square and linearly independent, it is invertible, and so has an inverse S-1. Multiplying by the inverse gives us A = S*^*S-1, showing that A is diagonalizable.

* What is an example of a matrix that has eigenvalues but is not diagonalizable?

 Upper triangular matrices with repeated entries across the diagonal e.g. [[1, 1], [0, 1]]. This is because a number A can only be an eigenvalue of a matrix U if U - A*I is not invertible. If it is invertible, it's nullspace is trivial and it doesn't have a nonzero eigenvector, thereby breaking the definition of an eigenvector: Uv = Av.

* Under what conditions is a matrix guaranteed to be diagonalizable?

An n*n matrix is diagonalizable iff it has n linearly independent eigenvectors, as shown above.

* What are some advantages of diagonalizable matrices?

Diagonalizable matrix multiplications are super easy to store and compute.

* Under what conditions does a matrix have linearly independent eigenvectors?

Uhhh not sure what this question is asking. In which it's diagnolizable? In which it has the maximum amount of eigenvalues for its size?

* What are the advantages to a matrix having linearly independent eigenvectors?

It's diagnolizable?

* Under what conditions does a matrix have orthonormal eigenvectors?

It's the identity matrix.

* What is the power method? What is it good for?

Through repeaded squaring of a matrix against a random vector, we can find an approximation to the largest eigenvalue, and a corresponding eigenvector.

* What is the determinant?

I answer this question in the next review note anyways.

* How does the determinant relate to volumes?

The determinant is the area of the hyperparalleliped formed by the column space of the matrix.

* Which matrices have determinants?

Square ones.

* Which matrices have nonzero determinants?

Invertible ones.

* What do determinants have to do with eigenvalues?

The characteristic polynomial, expressed by this formula:

```
det((^*I) - A)
```

is equal to zero only when ^ is an eigenvalue. If one solves for the roots of the polynomial, one can find all the eigenvalues.

* What is a Markov chain?

A markov chain is a digraph of states wherein transitions have a certain probability of occuring. The sum of the transition properties must be unitary.

* What do Markov chains have to do with eigenvectors?

If one identifies the eigenvalues of the markov chain, one can find the stationary distribution of the markov chain by repeatedly compounding the diagnolized matrix.
