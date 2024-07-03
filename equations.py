import numpy as np
import sympy as sp
import inspect

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