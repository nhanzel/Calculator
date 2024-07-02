from equations import *

running = True

def operations():
    return "1. Impulse Momentum Equation (working equation)"

while running:
    print(operations())
    operation = input("Enter operation: ")
    if operation == "1":
        unknown = ""
        m = float(input("Enter mass: "))
        v1 = float(input("Enter initial velocity: "))
        v2 = float(input("Enter final velocity: "))
        t = float(input("Enter time: "))
        fnet = float(input("Enter net force: "))

        for value in [m, v1, v2, t, fnet]:
            if value == -6969:
                unknown = get_var_name(value)
        
        print(unknown + ": " + str(impulse_momentum(m, v1, v2, t, fnet)[0]))
    else:
        print("Invalid operation")