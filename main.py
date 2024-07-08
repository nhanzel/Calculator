from equations import *
import os
import sympy

running = True
os.system('clear')

def operations():
    return """1. Impulse Momentum Theorem (working equation)\n
2. Work Energy Theorem (working equation)\n
3. Free Body Diagram (\u03A3F = ma)\n"""

while running:
    sympy.init_printing(use_unicode=True)
    print(operations())
    operation = input("Enter operation: ")

    # Impulse Momentum Theorem
    if operation == "1":
        params = {
            "m": 0.0,
            "vi": 0.0,
            "vf": 0.0,
            "t": 0.0,
            "fnet": 0.0
        }
        params['m'] = get_input_param("Enter mass (m): ")
        params['vi'] = get_input_param("Enter initial velocity (vi): ")
        params['vf'] = get_input_param("Enter final velocity (vf): ")
        params['t'] = get_input_param("Enter time (t): ")
        params['fnet'] = get_input_param("Enter net force (fnet): ")
        
        answer = str(impulse_momentum(params['m'], params['vi'], params['vf'], params['t'], params['fnet'])[0])
        output_answer(answer, params)

    # Work Energy Theorem
    elif operation == "2":
        params = {
            "m": 0.0,
            "vi": 0.0,
            "vf": 0.0,
            "x": 0.0,
            "fnet": 0.0
        }
        params['m'] = get_input_param("Enter mass (m): ")
        params['vi'] = get_input_param("Enter initial velocity (vi): ")
        params['vf'] = get_input_param("Enter final velocity (vf): ")
        params['x'] = get_input_param("Enter distance (x): ")
        params['fnet'] = get_input_param("Enter net force (fnet): ")

        answer = str(work_energy(params['m'], params['vi'], params['vf'], params['x'], params['fnet'])[0])
        output_answer(answer, params)

    # Free Body Diagram
    elif operation == "3":
        print("\n")
        x_components = get_components("X")
        y_components = get_components("Y")
        
        unknowns = {}
        x_unknowns = get_component_unknowns(x_components, 'x')
        y_unknowns = get_component_unknowns(y_components, 'y')
        for u in x_unknowns:
            unknowns[u] = 0.0
        for u in y_unknowns:
            if u not in unknowns:
                unknowns[u] = 0.0
        
        for u in unknowns:
            unknowns[u] = get_input_param("Enter " + u + ": ")

        answer = free_body_diagram(x_components, y_components, unknowns)

        print("\n")
        for a in answer:
            print(a)
        print("\n")
        
    else:
        print("\n")
        print("Invalid operation")
        print("\n")