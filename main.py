from equations import *

running = True

def operations():
    return """1. Impulse Momentum Theorem (working equation)\n
2. Work Energy Theorem (working equation)\n"""

while running:
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
    if operation == "2":
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
    else:
        print("Invalid operation")