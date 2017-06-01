"""
Copyright 2013 Steven Diamond

This file is part of CVXPY.

CVXPY is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CVXPY is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CVXPY.  If not, see <http://www.gnu.org/licenses/>.
"""

# for decimal division
from __future__ import division

import cvxopt
import numpy as np
from pylab import *
import math

from cvxpy import *

# Taken from CVX website http://cvxr.com/cvx/examples/
# Example: CVX Textbook exercise 4.3: Solve a simple QP with inequality constraints
# Ported from cvx matlab to cvxpy by Misrab Faizullah-Khan
# Original comments below


# From Boyd & Vandenberghe, "Convex Optimization"
# Joelle Skaf - 09/26/05
#
# Solves the following QP with inequality constraints:
#           minimize    1/2x'*P*x + q'*x + r
#               s.t.    -1 <= x_i <= 1      for i = 1,2,3
# Also shows that the given x_star is indeed optimal

# Generate data
n = 3
P = cvxopt.matrix([	13, 12, -2,
					12, 17, 6,
					-2, 6, 12], (n,n))
q = cvxopt.matrix([-22, -14.5, 13], (n,1))
r = 1
x_star = cvxopt.matrix([1, 1/2, -1], (n,1))

# Frame and solve the problem

x = Variable(n)
objective = Minimize(  0.5 * quad_form(x, P)  + q.T * x + r )
constraints = [ x >= -1, x <= 1]

p = Problem(objective, constraints)
# The optimal objective is returned by p.solve().
result = p.solve()
