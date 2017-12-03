4.7.3
Find a nonzero vector in the null space of the matrix
1. [1 0 1]
A: [1, 0, -1]

2. [
  [2, 0, 0],
  [0, 1, 1]
]
A: [0, 1, -1]

3. [
  [1, 0, 0],
  [0, 0, 0],
  [0, 0, 1]
]
A: [0, 1, 0]

Quiz 4.10.5:
show that f([x, y]):R2 -> x * y is not a linear function by giving inputs for which the function volates either L1 or L2
f([1, 0]) -> 0
f([0, 1]) -> 0
f([0, 1] + [1, 0]) -> 1

Quiz 4.10.6:
show that rotation by ninety degrees r90(.), is a linear function
there's a matrix for rotation by ninety degrees, and we now that
f(x): M * x is a linear function so QED man

Exercise 4.10.7:
the function g : R2 -> R3 by g([x, y]) = [x, y, 1] isn't linear by proof of construction:
2 * g([2, 2]) = [4, 4, 2]
g(2 * [2, 2]) = [4, 4, 1]

which defies L2

Exercise 4.10.8:
h: R2 -> R2 takes a point [x, y] to its reflection about the y-axis
h = [x, y] -> [
  [-1, 0]
  [0, 1]
] * [x, y]
it's linear cuz its multiplied by a matrix man
L1: a*f([x, y]) = f(a[x, y])
= a*[-x, y]
= [-x * a, a * y]
f([a*x, a*y])
= f(a([x, y]))

problem 4.10.9
example 4.9.6, the function from R2 to R2 that translates a point one unit to the right and two units up
the matrix is presumed to be [
  [2, 1]
  [2, 3]
]

so a = f([2, 5]) = [9, 19]
and b = f([1, 3]) = [5, 11]
a + b = [14, 30]
[2, 5] + [1, 3] = [3, 8]
f([3, 8]) = [11, 30]
which violates L1

4.13.2:
if f is a linear function and g is its inverse then g is also a linear function

for every scalar a and vector y in the domain of g, g(a*y) = a*g(y)

g(a * y)  = g(a * f(x))
          = g(f(a * x))
          = a * x
          = a * g(y)
