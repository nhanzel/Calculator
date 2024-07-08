## DONE

#### impulse momentum theorem working equation

#### work energy theorem working equation

## TODO

#### momentum conservation theorem

#### free body diagram

- figure out how to get a system of equations working with sympy
- get the input for all of the x and y components and store those equations (as strings?)
- programatically determine which variables are included with each equation entered in the component step
- get the variables that are needed (including trig representations of data)
- denote which variables I don't have

- set up my equations with my variables and unknowns
- solve the system of equations

TESTING

- Test for negative multipliers for trig functions
- Test for

{'m': 20.0, 'ax': '?', 'g': -9.81, 'FN': '?', 'ay': 0.0, 'Mk': 0.4}
['Fg = -Fg', 'FN = FN', 'Ffk = 0', 'Fpush = 5*cos(32)']
['Fg = 0', 'FN = 0', 'Ffk = -Ffk', 'Fpush = 5*sin(#2)']

20.0 * ax = -20.0*9.82 + FN + 0 + 40.0*cos(32)
20.0 * 0.0 = 0 + 0 + -0.4*FN + 40.0*sin(32)
