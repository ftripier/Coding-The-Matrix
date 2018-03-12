* What is an inner product for vectors over R?

the inner product for vectors over R is apparantly equivalent to the dot product. I'm not sure why we're introducing another name for the dot product.

* How is norm defined in terms of dot-product?
Since the inner product is equivalent to the dot product, the norm is defined as the square root of the dot product.

* What does it mean for two vectors to be orthogonal?
They're perpindicular! This explanation is given more intuition by showing the pythagorean theorem in the context of linear algebra, and giving some cotnext for why perpendicularity may be important.

* What is the pythagorean theorem for vectors?
The pythagorean theorem for vectors is that two vectors u and v are orthogonal if

```
norm(u + v)^2 == norm(u)^2 + norm(v)^2
```

If you think of two vectors as translations from the origin, in some order (the actual order doesn't matter by symmetry of the inner product), then one can visualize them as forming a triangle with one side u, one side v, and one side u + v. By equational reasoning through properties of the inner product:

norm(u + v)^2 = <u + v, u + v>
 = <u, u + v> + <v, u + v>
 = <u, v> + <u, u> + <v, v> + <v, u>
 = norm(u)^2 + (<u, v>)^2 + norm(v)^2

which means norm(v + v)^2 = norm(u)^2 + norm(v)^2
if u and v are orthogonal and therefore <u, v> == 0.
And indeed, the pythagorean theorem only works on right triangles.

problem 8.3.4:
u = [1, 1]
v = [2, 2]
alpha = 2
beta = 3

||alpha*u + beta*v||^2 = 
||[8, 8]||^2 = 128

alpha^2 * ||u||^2 + beta^2 * ||v||^2
4*||[1, 1]||^2 + 9*||[2, 2]||^2
8 + 72 = 80


problem 8.4.5:

if for integer i, all preceding terms alpha^(i-k)^2||v^(i-k)||^2 have been equal to ||alpha^i-k*v^i-k...||^2,
then all the preceding terms could be expressed as one scalar multiplied against one vector component by homegenity, and we've already proven the two term case with the pythagorean proof.

* what is parallel-perpindicular decomposition of a vector?
decomposing the vector b with respect to another vector v in such a way that the decomposition has one component that describes the projection of b orthogonal to v (the perpindicular one), and one alongside v (the parallel one). The book goes on to give an example of a generic 2d parallel-perpindicular vector with respect to the unitary x-axis vector to show that the projection in that case is as simple as taking the x-axis component of the original vector paired with 0 as the parallel component, and the y-component paired with 0 as the perpindicular component.

* How does one find the projection of a vector b orthogonal to another vector v?

So, you know that the point closest to v in the span of v will be b^parallel, and you know that the distance will be b^perpendicular. You know b^perpendicular is orthogonal to v, and therefore <b^perpendicular, v> == 0. You know that the vector from b to b^parallel must be orthogonal to v, because b^perpendicular + b^parallel == b, and so <b - b^parallel, v> == 0. b^parallel is equivalent to v times some scalar, because b^parallel is in the span of v, and so <b - a*v, v> == 0. By linearity and homogenity, you can derive <b, v> - a*<v, v> = 0, and solving for zero,
a = <b, v>/<v, v>. The projection of b along v is just a*v.

* How can linear algebra help in optimizing a nonlinear function?

In the example presented in the book, the optimization step is a linear transformation from the weight vector being optimized to a more optimal one along the gradient of some loss function.

More generally, one can define an n-dimensional linear space, and use it as a search space in the n+1 dimensional space formed by considering the nonlinear loss function by sampling the n+1 component of points derived by linear transformation in the original n-dimensional space.
