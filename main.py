from equations import *

running = True

def operations():
    return "1. Impulse Momentum Equation (working equation)"

while running:
    print(operations())
    operation = input("Enter operation: ")
    if operation == "1":
        params = {
            "m": 0.0,
            "v1": 0.0,
            "v2": 0.0,
            "t": 0.0,
            "fnet": 0.0
        }
        params['m'] = get_input_param("Enter mass (m): ")
        params['v1'] = get_input_param("Enter initial velocity (vi): ")
        params['v2'] = get_input_param("Enter final velocity (vf): ")
        params['t'] = get_input_param("Enter time (t): ")
        params['fnet'] = get_input_param("Enter net force (fnet): ")
        
        answer = str(impulse_momentum(params['m'], params['v1'], params['v2'], params['t'], params['fnet'])[0])
        output_answer(answer, params)
    else:
        print("Invalid operation")