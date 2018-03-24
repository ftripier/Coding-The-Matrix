* Why does the function x -> Qx preserve dot-products when Q is a column-orthogonal matrix? Why does it preserve norms?

The dot product of Qx with another vector in the same basis Qb can be decomposed into the dot product of two matrix-vector multiplications wherein Q is preserved:

(Q*x)^T*(Q*b) = dot-product

Through some algebraic manipulation, one inevitably negates the multiplication of Q with its transpose (in a column-orthogonal matrices, the inverse is its transpose), and regains the dot-product in x's standard basis.

Preserving norms is an extension of this equational reasoning. One can imagine any vector a expressed by some linear combination of basis vectors. By the argument above, these basis vectors will retain dot-product even in Q's basis, and so will have the same norm.

* How does one find the closest vector whose representation in a given basis is k-sparse? Why would one want to do so?

For a vector b with representation x, you want a vector measure in x's basis that's k-sparse such that you minimze the distance to x.

Finding k-sparse vectors seems to be useful for compression, which is useful both for storage and limiting compute. Finding a sparse representation in another basis seems to be useful because it can prove more sparse, but once transformed, yield a vector in the original basis with less discontinuities than a k-sparse vector in the original basis.

* Why might you want a basis such that there are fast algorithms for converting between a vector and the vector's coordinate representation?

Well, it could be that either representation is advantageous in certain use cases, the conversion is performed often, and speed is particularly valuable. The book discussed compression as such a use case, with the coordinate representation specifically being a k-sparse representaion.

* What is a wavelet basis? How does it illustrate the notions of direct sum and orthogonal complement?

* What is the process for computing a vector's representation in the wavelet basis?

* What is the inner product for vectors over C?

* What is the Hermitian adjoint?

* What does the discrete Fourier basis have to do with circulant matrices?

