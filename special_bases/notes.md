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

The wavelet basis is defined by construction on some vector space V of dimension n. The wavelet basis is composed of the union for bases of the following vector spaces:

V1: the basis composed of the box vector for Vn in 1 dimension. Generally, this is a vector whose domain is covered by the multiplicative unit (1 in the reals) in each component.

Wi for i in k^2 for i = 0; i < root(n); i += 1:
Wavelet spaces of dimension i. A wavelet space is the orthogonal comblement for the box space of the original v of the same dimension.

This composition illustrates orthogonal complement and direct sum as the original vector space can be decomposed into many component orthogonal spaces disjuncted by direct sum.

* What is the process for computing a vector's representation in the wavelet basis?

Given a wavelet basis, once could find the representation of a vector v in the matrix by contstructing a matrix with column space drawn from the wavelet basis, taking the ivnerse, and multiplying that against the vector.

In practice, the computational debt can be amortized significantly.

By construction, one finds the representation of a vector v drawn from vector space V in a first order wavelet decomposition of Vn/2 + Wn/2. This is done by finding of linear combination of n vectors like

v = x0*b0 + ... + xn/2*bn/2 + y0*w0 + .... yn/2*wn/2

where, since the vectors are mutually orthogonal by construction, we can simply find the coefficients by the project-along rule, i.e.

xi = (v*bi)/(bi * bi)
yi = (v*wi)/(wi * wi)

These dotproducts have computational shortcuts due to known characteristics about the box basis and wavelet basis. Specifically, xi can be calculated as the average of entries 2i and 2i + 1 of v, and yi can be calculated as the difference of entries 2i and 2i + 1 of v.

If one iterates this construction to the wavelet basis (powers of two wavelet spaces along with the one-dimensional vector space), one retrieves the coefficients in terms of the wavelet basis.

The book goes on to describe how to normalize this basis in order to make it orthonormal in order to facilitate the computational requirements of transforming to and from the basis. Wavelet coefficients of the form wi^s (where s determines the vector space dimensional partition, a power of two) are normalized by multiplying sqrt(n/4s), and the box coefficient is normalized by multipling sqrt(n).

* What is the inner product for vectors over C?

The inner product of two complex vectors v and b is defined as

conjugate(v) * b (* is the dot product).

We take the conjugate of v in order to fullfil the inner product requirement that the inner product of a complex vector with itself yield the norm, and therefore a positive real number.

* What is the Hermitian adjoint?

THe hermitian adjoint of a matrix A over the complex numbers is the transpose of A, but with each element as the complex conjugate of every element in A. This is the complex equivalent of an column orthogonal inverse in the reals. Actually, column orthogonal matrices over the complex numebrs are called _unitary_, and the definition of a unitary matrix is one such that, when multiplied by its hermitian adjoint, it yields the identity matrix.

* What does the discrete Fourier basis have to do with circulant matrices?

Circulant matrix multiplication can be significantly computationally amortized (specifically, diagnolized), when in the discrete fourier basis.

This computation is expressed by

FourierMatrix*DiagnolizedCirulant*InverseFourier



