from playground_equations import *
import sympy as sp
import numpy as np

FN = sp.Symbol("FN")
m = sp.Symbol("m")
g = 9.81
v = 5.5556
R = 100
theta = angle(15)
FF = sp.Symbol("FF")
MU = sp.Symbol("MU")

eq1 = FN*(np.cos(theta)) + FF*(np.sin(theta)) - m*g
eq2 = FN*(np.sin(theta)) - FF*(np.cos(theta)) - m*v**2 / R
eq3 = FF - MU*FN

solution = sp.solve([eq1, eq2, eq3], (FN, FF, MU))

print(solution[0][2])