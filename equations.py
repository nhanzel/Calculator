import numpy as np
import math
import re
import sympy as sp

## GLOBALS
equation_unknowns = { # m: mass, M: friction coefficient
    "FN": ["FN"],
    "Fg": ["m", "g"],
    "Fpush": ["Fpush"],
    "Fpull": ["Fpull"],
    "Ffs": ["Ms", "FN"],
    "Ffk": ["Mk", "FN"],
    "FT": ["FT"],
}

equation_code = { # formatted as python accessible strings
    "Fg": "m*g",
    "Ffs": "Ms*FN",
    "Ffk": "Mk*FN",
}

## FUNCTIONS
def impulse_momentum(m, vi, vf, t, fnet):
    if m == "?":
        m = sp.Symbol("m")
    elif vi == "?":
        vi = sp.Symbol("vi")
    elif vf == "?":
        vf = sp.Symbol("vf")
    elif t == "?":
        t = sp.Symbol("t")
    elif fnet == "?":
        fnet = sp.Symbol("fnet")
    eq = -(fnet * t) + (m * (vf - vi))
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

def free_body_diagram(x_components, y_components, unknowns):
    x_operators = []
    y_operators = []

    #format equations as strings (python syntax)
    for xc in x_components:
        eq = xc.split("=")[1].strip()
        for key in equation_code:
            if key in eq:
                eq = eq.replace(key, equation_code[key])
        x_operators.append(eq)
    for yc in y_components:
        eq = yc.split("=")[1].strip()
        for key in equation_code:
            if key in eq:
                eq = eq.replace(key, equation_code[key])
        y_operators.append(eq)

    x_equation = " + ".join(x_operators) + " - (m * ax)"
    y_equation = " + ".join(y_operators) + " - (m * ay)"
    x_equation = format_trig_for_sympy(x_equation)
    y_equation = format_trig_for_sympy(y_equation)

    #plug in known values
    for key, value in unknowns.items():
        if value != '?':
            x_equation = x_equation.replace(key, str(value))
            y_equation = y_equation.replace(key, str(value))

    #get unknowns
    variable_unknowns = [key for key, value in unknowns.items() if value == '?']
    symbol_unknowns = [sp.symbols(var) for var in variable_unknowns]
    
    #solve
    x_result = sp.sympify(x_equation)
    y_result = sp.sympify(y_equation)

    return sp.solve([x_result, y_result], symbol_unknowns, dict=True)

def mechanical_energy(m, vi, vf, hi, hf, wnc, g):
    if g == "?" or g == "": #special case to allow earth gravity to be a blank input
        g = 9.81 if g == "" else sp.Symbol("g")
    if m == "?":
        m = sp.Symbol("m")
    elif vi == "?":
        vi = sp.Symbol("vi")
    elif vf == "?":
        vf = sp.Symbol("vf")
    elif hi == "?":
        hi = sp.Symbol("hi")
    elif hf == "?":
        hf = sp.Symbol("hf")
    elif wnc == "?":
        wnc = sp.Symbol("wnc")
    eq = (.5 * m * (vf**2 - vi**2)) + (m * g * (hf - hi)) - wnc
    return sp.solve(eq)

def center_of_mass(masses):
    dimensions = len(masses[0]) - 1
    component_vector = [0.0, 0.0, 0.0]
    result_vector = []
    for mass in masses:
        weight = float(mass[0])
        for d in range(dimensions):
            component_vector[d] += weight * float(mass[d + 1])
    for component in component_vector:
        component /= sum([float(mass[0]) for mass in masses])
        result_vector.append(component)
    return result_vector

def angular_momentum(v1, v2):
    f1 = [float(v1[0]), float(v1[1]), float(v1[2])]
    f2 = [float(v2[0]), float(v2[1]), float(v2[2])]
    return np.cross(f1, f2)

## HELPERS
def get_components(axis):
    components = []
    component_counter = 1
    running = True
    print("ENTERING " + axis + " COMPONENTS (type 'done' to finish)")
    print("Ex: FN = FN*cos(32), Fg = 0, Fg = -Fg, etc.")
    while running:
        component = input(str(component_counter) + ": ")
        if component == "done":
            running = False
        else:
            component_counter += 1
            components.append(component)
    return components

def get_component_unknowns(components, axis):
    unknowns = ['m', 'a' + axis]
    for c in components:
        parts = c.split("=")
        unk = parts[1].strip()
        for key, value in equation_unknowns.items():
            if key in unk: # if we detect an equation, add any new needed variables to our unknowns
                for v in value:
                    if v not in unknowns:
                        unknowns.append(v)
    return unknowns

def get_input_param(prompt):
    raw_input = input(prompt)
    try:
        return parse_trig(raw_input)
    except ValueError:
        return "?"
    
def get_var_name(var):
    params = locals().copy()
    for name, value in params.items():
        if value == var:
            return name
    
def output_answer(answer, params):
    print("\n")
    print(next((key for key, value in params.items() if value == "?"), None) + ": " + answer) 
    print("\n")

def parse_trig(input):
        parts = input.split('*')
        if len(parts) == 2:
            multiplier, trig_part = parts
            multiplier = float(multiplier)
            for trig_func in ['sin', 'cos', 'tan']:
                if trig_func in trig_part:
                    angle = float(trig_part.split(trig_func)[1].strip('()'))
                    angle_rad = math.radians(angle)
                    # Calculate the trigonometric value and multiply by the multiplier
                    if trig_func == 'sin':
                        return multiplier * math.sin(angle_rad)
                    elif trig_func == 'cos':
                        return multiplier * math.cos(angle_rad)
                    elif trig_func == 'tan':
                        return multiplier * math.tan(angle_rad)
        # If no multiplier was found, it's a regular float
        return float(input)

def format_trig_for_sympy(equation):
    patterns = {
        r'cos\((.*?)\)': r'cos(\1*3.14159265359/180.0)',
        r'sin\((.*?)\)': r'sin(\1*3.14159265359/180.0)',
        r'tan\((.*?)\)': r'tan(\1*3.14159265359/180.0)'
    }
    
    for pattern, replacement in patterns.items():
        equation = re.sub(pattern, replacement, equation)
    
    return equation