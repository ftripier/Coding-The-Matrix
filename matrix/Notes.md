# The Matrix

4.7.4: For any R X C matrix A and C vector v, a vector z is in the null space of A if and only if A * (v + z) = A * v

4.7.11
H = [
  [0, 0, 0, 1, 1, 1, 1],
  [0, 1, 1, 0, 0, 1, 1],
  [1, 0, 1, 0, 1, 0, 1],
]
H * e1 = H * e2

e1 = [1, 1, 0, 0, 0, 0, 0]
e2 = [0, 0, 1, 0, 0, 0, 0]

4.9.2
1. The domain of f(M^T) is C
2. The codomain of f(M^T) is R
3. [1, -10] has an all-zero vector in the image of f(M^T)

4.10.2 (linear functions)
U, V = vector spaces over field F
a function f : U -> V is a linear function (linear transformation) if

L1: For any vector u in the fomain of f and any scalar a in F
f(a * u) = a * f(u)

L2: For any two vectors u and v in the domain of f,
f(u + v) = f(u) + f(v)

prop: for any matrix M the function x -> M * x is a linear function
Lemma 4.10.3: FOr any C-vector a over F, the function f: F^C -> F defined by f(x) = a * x
is a linear function
^ the proof just uses a one row matrix

Linear functions map the zero vector of the domain to the zero vector of the codomain, which makes sense since the codomain is a vector space.

the kernel of a linear function f is {v : f(v) = 0}. we denote the kernel of f by Ker f.
The kernel of a function is a vector space:
proof:

The kernel must include the zero vector since the zero vector of the input maps to the zero vector of the output.

The kernel must have closure over addition because, say we have v1 and v2 in the kernel
f(v1) = 0 and f(v2) = 0 by definition. f(v1 + v2) = 0 by L2

THe kernel must have closure over scalar multiplication by L1, following the same logic.

Matrix-matrix multiplication
row r of AB = (row r of A) * B
columns s of AB = A * (column s of B)
entry rc of AB is the dot-product of row r of A with column c of B
