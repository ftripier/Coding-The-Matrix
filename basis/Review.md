1. What is coordinate representation?

Specifically, a coordinate representation is a representation of a point in space. From a linear algebra perspective, a space is defined by its basis of vectors. A point in that space is some linear combination of those vectors. The coordinate representation is tantamount to a vector of the coefficients of those vectors.

2. How can you express conversion between a vector and its coordinate representation using matrices?

So, if a coordinate representation is the coefficients of the linear combination of a vector space's basis, it suffices to recover the full linear combination to multiply it against a matrix with the basis as its column space. They are equivalent by the linear combination definition of matrix vector multiplication.

3. What is linear dependence?

360 no scope answer:
Linear dependence is a relationship between a vector and a set of other vectors wherein the vector can be described as some linear combination of the set of vectors. 

Looked at the book answer:
A set of vectors is linearly dependent if they have a nontrivial linear combination that equals the zero vector.

4. What is the Grow algorithm?

360 no scope answer:
The Grow algorithm is a greedy algorithm for finding the minimum spanning tree of a weighted graph. The grow algorithm works by adding the lowest cost path step to the accumulated set of path components.

Actual answer:
The grow algorithm is a greedy algorithm for finding the minimum number of vectors in a vector space V that span V. It works by accumulating a basis by adding vectors from v that are not in the accumulated basis.

5. What is the shrink algorithm?

360 no scope answer:
The shrink algorithm is like the grow algorithm only it works by initializing the result basis to the entire vector space, and removing vectors spanned by the basis until termination.

Actual answer:
Yeah the 360 no scope was pretty good actually.

6. How do the concepts of linear dependence and spanning apply to subsets of edges of graphs?

360 no scope answer:

Graphs can be represented as matrices through the _adjacency list_ representation,where in column space, each column represents the presence of edges from the column's vertex to other vertices (the other columns of the matrix), with one representational field being 0 for no edge and 1 for an edge.

Under this representation, a vector represents a path through the complete graph of its dimension. If a set of these path vectors is linearly dependent, then that means some subset of that set can yield all paths in the set. A spanning set of paths can yield all paths in their space.

Actual answer:
Under a matrix representation of a graph with domain R X C where R is the set of edges in the graph, and C is the set of vertices in the graph, vectors represent paths in the graph.

The same observations from the "360 no scope" answer hold, but are constrained to the graph's space rather than the complete graph by virtue of the domain.

7. Why is the output of the growing algorithm a set of linearly independent vectors?

Inductively, the result of the algorithm is always linearly independent - we only add vectors that preserve linear independece by invariant. Since we only ever add vectors to the result basis that aren't in the span, they're linearly independent by definition.

8. Why is the output of the shrinking algorithm a set of linearly independent vectors?

The algorithm terminates once it has a linearly independent set of vectors.

9. What is a basis?

360NOSCOPE:

A basis for a vector space v is a set of linearly independent vectors drawn from v that spans v.

ACTUAL:

clutched itt

10. What is a unique representation?


360NOSCOPE:
A unique representation for a vector is the coordinate representation of that vector in a given basis. This representation is unique, because a basis is linearly independent.

ACTUAL:
Yeeeeeaaaaaah

11. What is a change of basis?

A change of basis is a linear transformation of a given vector to its unique representation in a different basis.

12. What is the exchange lemma?

The exchange lemma is the formalization of the idea that in a set of vectors, you can maintain the linear independence of a set of vectors by swapping a vector in from outside that subset if the removal of the old vector and the addition of the new one would maintain linear independence.

