from __future__ import print_function

import sys
from ortools.constraint_solver import pywrapcp

def test():
    solver = pywrapcp.Solver("simple_example")
    # Create the variables.
    V = solver.IntVar(1, 8, "V")
    D = solver.IntVar(1, 8, "D")
    C = solver.IntVar(1, 8, "C")
    R = solver.IntVar(1, 8, "R")
    E = solver.IntVar(1, 8, "E")
    A = solver.IntVar(1, 8, "A")
    U = solver.IntVar(1, 8, "U")
    G = solver.IntVar(1, 8, "G")

    # VVD
    # Dzz
    # CDA
    #  CU
    # REG

    # Create the constraints.
    solver.Add(V != D)
    solver.Add(V != C)
    solver.Add(V != R)
    solver.Add(V != E)
    solver.Add(V != A)
    solver.Add(V != U)
    solver.Add(V != G)

    solver.Add(D != C)
    solver.Add(D != R)
    solver.Add(D != E)
    solver.Add(D != A)
    solver.Add(D != U)
    solver.Add(D != G)

    solver.Add(C != R)
    solver.Add(C != E)
    solver.Add(C != A)
    solver.Add(C != U)
    solver.Add(C != G)

    solver.Add(R != E)
    solver.Add(R != A)
    solver.Add(R != U)
    solver.Add(R != G)

    solver.Add(E != A)
    solver.Add(E != U)
    solver.Add(E != G)

    solver.Add(A != U)
    solver.Add(A != G)

    solver.Add(U != G)

    solver.Add(V + D + C + 1 == R)
    solver.Add(V + D + C + 1 < 10)
    solver.Add((V + 6 + D + C + 2) % 10 == E)
    solver.Add((D + 6 + A + U) % 10 == G)

    solver.Add((D + 6 + A + U) > 20)

    # Call the solver.
    db = solver.Phase([V, D, C, R, E, A, U, G], solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
    solver.Solve(db)
    print_solution(solver, V, D, C, R, E, A, U, G)


def print_solution(solver, *array):
    count = 0

    while solver.NextSolution():
        count += 1
        # print(array)
    # print("\nNumber of solutions found:", count)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=1) * 1000, "ms")