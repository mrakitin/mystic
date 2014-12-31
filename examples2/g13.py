# A-R Hedar and M Fukushima, "Derivative-Free Filter Simulated Annealing
# Method for Constrained Continuous Global Optimization", Journal of
# Global Optimization, 35(4), 521-549 (2006).
# 
# code for function PrG13c and PrG13f
# translated from Matlab Code written by A. Hedar (Nov. 23, 2005).
# http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/go.htm

def objective(x):
    from numpy import exp, product
    return exp(product(x))

bounds = [(-2.3,2.3)]*2 + [(-3.2,3.2)]*3
# with penalty='penalty' applied, solution is:
xs = [-1.717143, 1.595709, 1.827247, -0.7636413, -0.763645]
_xs = [-1.717143, 1.595709, 1.827247, 0.7636413, 0.763645]
x_s = [-1.717143, 1.595709, -1.827247, 0.7636413, -0.763645]
xs_ = [-1.717143, 1.595709, -1.827247, -0.7636413, 0.763645]
ys = 0.05394983

from mystic.symbolic import generate_constraint, generate_solvers, solve
from mystic.symbolic import generate_penalty, generate_conditions

equations = """
x0**2 + x1**2 + x2**2 + x3**2 + x4**2 - 10.0 = 0.0
x1*x2 - 5*x3*x4 = 0.0
x0**3 + x1**3 + 1.0 = 0.0
"""
#cf = generate_constraint(generate_solvers(solve(equations))) #XXX: solve slow
pf = generate_penalty(generate_conditions(equations))

from mystic.constraints import as_constraint

cf = as_constraint(pf)



if __name__ == '__main__':

    from mystic.solvers import lattice
    from mystic.math import almostEqual

    result = lattice(objective, 5, [3]*5, bounds=bounds, penalty=pf, ftol=1e-8, xtol=1e-8, disp=False, full_output=True)

    assert almostEqual(result[0], xs, tol=1e-2) \
        or almostEqual(result[0], _xs, tol=1e-2) \
        or almostEqual(result[0], x_s, tol=1e-2) \
        or almostEqual(result[0], xs_, tol=1e-2)
    assert almostEqual(result[1], ys, rel=1e-2)



# EOF