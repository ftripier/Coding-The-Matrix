1. Can a vector space have bases of different sizes?

Nope! In the book proof is given by way of the morphing lemma, based on the Exchange lemma. This lemma leads to a theorem that a basis are the smallest sets of generators for their vector spaces.

Basically, the idea is that if some set of vectors wasn't a basis, then it would be linearly dependent, and therefore would have redundant vectors. So it would be larger than a basis. A basis has to be the smallest, because for any set of generators you can swap out a linearly independent subset of those vectors with the basis and maintain linear independence and cardinality of both sets.


2. What is the rank of a set of vectors?
The rank of a set of vectors is the dimension of its span.

3. What is the rank of a matrix?
The row rank is the rank of its row space, and the column rank is the rank of its column space.

The rank is either one, because they're equivalent by the rank theorem.

4. What is the difference between rank and dimension?

- The dimension of a vector space is the amount of vectors in its basis
- The rank of a set of vectors is the dimension of its span.

rank applies to any sets of vectors, the dimension applies to a vector space.

5. How do rank and dimension apply to graphs?
The rank and dimension can be used to find the size of the MST.

6. What is the rank theorem?
The rank theorem is that the rank of the rows of matrix equal the rank of its columns.

This is proved by decomposing the column space of a matrix A into its basis and coordinate representation. From there it is shown that all of the rows in A are linear combinations of the rows of the coordinate representation of the column space, and therefore must be a subspace. By applying this to the transpose, you can use the inequality of both row spaces to prove equivalence of column and row rank.


7. When can two vectors spaces form a direct sum?

When they share no nonzero vectors.

8. How does the dimension of a direct sum of two vector spaces relate to their dimensions?

360 no scope: It is the max(n, k) where n and k are the dimensions of the two vector spaces. The intuition here is that it can't be smaller than the largest dimension because then there would be a vector in either vector space not represented in the direct sum, and it can't be larger because any vectors non-extant in the two vector spaces are simply linear combinations of those that do exist.

Turns out I was wrong on this: the union of a basis of U and a basis of V is a basis of U + V.

The intuition is that there cannot be a vector in the direct sum of two bases, because there would have to be some nontrivial linear combination, but there can't be, because by definition of a direct sum, they have no nontrivial vectors in common.

9. How can dimension be used in a criterion for a linear function to be invertible?

It has a lower bound on the dimension of its input. The geometric intuition here is that all points in the output have to have a one-to-one mapping to their respecitive input, and if the input is dimensionally collapsed, you loose that one-to-one relationship. Plane goes to line == you have an entire line of points that could be responsible for the output line.


7. What is the dimension principle?

If v is a subspace of b
1) then dim v <= dim b
2) if dim v == dim b, then v == b.

this proof works because since v is a subspace, b must contain v's basis and so b has v as a lower bound. If b is at the lower bound, then it can't contain any more vectors than v.
 

10. What is the Kernel-Image theorem?

The kernel image theorem states that the dimension of the domain equals the dimension of the kernel added to the dimension of the image vector space. I think the intuition here is a dimension can either be mapped to or collapsed, so there's always a trade off between null space and image space. 

11. What is the Rank-Nullity theorem?

That for any matrix, it's rank can be decomposed into the rank of its null space and the rank of its column space. It follows from the kernel-image theorem.

12. How can dimension be used to give a criterion for matrix invertability?

Basically, if you preserve the dimension of your domain, you're invertible. This kind of follows from the rank-nullity theorem, but I like thinking about it in terms of the last time I answered this question.

13. What is the annihilator of a vector space?

The annihilator of a vector space is a vector space for which every vector nullifies every vector in the original vector space. The ahnnihilator is equivalently the null space of the row-matrix representation of a vector space's generators.

14. What is the annihilator theorem?
The annihilator of an annihilator is the original space. The proof of this relies on the commutativity of the dot product to show that the original space would annihilate every vector in the annihilator.
