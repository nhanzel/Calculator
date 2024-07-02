import numpy as np
import sympy as sp

def impulse_momentum(m, v1, v2, t, fnet):
    for var in [m, v1, v2, t, fnet]:
        if var == -6969:
            t = sp.Symbol('t')
    eq = -(fnet * t) + (m * (v2 - v1))
    return sp.solve(eq)

# HELPER FUNCTIONS

def get_var_name(var):
    params = locals().copy()
    for name, value in params.items():
        if value == var:
            return name