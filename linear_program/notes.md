* What is a linear program?

A linear program is a matrix-vector equation A*x = b where each vector entry i corresponds to the number of some object, and each row i of A corresponds to weights allocated to the objects of x, and entry i of b corresponds to some constraint on the sum of that weight.

Typically, linear programs solve for the optimization of allocation across multiple resources under certain constraints.

* How can a resource-allocation question be formulated as a linear program?

I just answered that above I think.

* What is linear programming duality?

linear programming duality is the existence of a correspondence between the linear programming minimizing cost i.e. min{ c * x : A*x >= b} and one maximizing tightness to constraint i.e. max{b * y : y^T*A=c, y>=0}

* What is the basis of the simplex algorithm?

Weak duality, specifically, iterating through verticies of the solution polyhedron by finding solutions to subsets of the rowspace of the original linear program, checking for feasibility of constraint tightness (the max dual), and if not found, moving to a vertex that tightens the loosest constraint and drops the most violated constraint from the subsystem of linear equations.

* What is the connection between linear programming and zero-sum two-person games?

zero-sum two-person games have an equilibrium wherein the maxmin equals the minmax. Consequently, they can be framed as linear programs and solved that way. The constraints are that for each strategy x, x >= 0, _1_ * x = 1 where _1_ is the all 1 vector, and for row ai of the payoff matrix A, ai * x >= lambda, where lambda is the lower bound all all possible pure strategies from the opposing player. The opposing player is represented by the dual program discussed above.