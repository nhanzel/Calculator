import numpy as np
import sympy as sp

def impulse_momentum(m, v1, v2, t, fnet):
    if m == "?":
        m = sp.Symbol("m")
    elif v1 == "?":
        v1 = sp.Symbol("v1")
    elif v2 == "?":
        v2 = sp.Symbol("v2")
    elif t == "?":
        t = sp.Symbol("t")
    elif fnet == "?":
        fnet = sp.Symbol("fnet")
    eq = -(fnet * t) + (m * (v2 - v1))
    return sp.solve(eq)

def work_energy(m, vi, vf, x, fnet):
    sign_check = False # required since we are dealing with square roots and sympy wants to use the negative
    if m == "?":
        m = sp.Symbol("m")
    elif vi == "?":
        vi = sp.Symbol("vi")
        sign_check = True
    elif vf == "?":
        vf = sp.Symbol("vf")
        sign_check = True
    elif x == "?":
        x = sp.Symbol("x")
    elif fnet == "?":
        fnet = sp.Symbol("fnet")
    eq = -(fnet * x) + (0.5 * m * (vf**2 - vi**2))
    result = sp.solve(eq)
    if sign_check:
        result[0] = abs(result[0])
    return result

# HELPER FUNCTIONS

def get_var_name(var):
    params = locals().copy()
    for name, value in params.items():
        if value == var:
            return name
        
def get_input_param(prompt):
    raw_input = input(prompt)
    try:
        return float(raw_input)
    except ValueError:
        return "?"
    
def output_answer(answer, params):
    print("\n")
    print(next((key for key, value in params.items() if value == "?"), None) + ": " + answer) 
    print("\n")