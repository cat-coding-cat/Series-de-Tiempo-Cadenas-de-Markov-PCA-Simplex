import numpy as np

#  metodo simplex para Maximizar/Minimizar
#  es decir OPTIMIZACIóN
#  considerando restricciones específicas.

# tenemos dos variables x1 x2
# y queremos maximizar la suma

# x1 + x2 = y (sea m'aximo)

# considerando las siguientes condiciones:

#  x1 >= 0
#  x2 >= 0
#  2x2 - x1 <= 4
#  x2 + 2x1 <= 10

#  simplex

#  1. Introducimos una veriable x3
#     x3 >= 0
#     para convertir -x₁ + 2x₂ + x₃ = 4



#  2. Hacemos lo mismo x₄ ≥ 0
#     2x₁ + x₂ + x₄ = 10


#  nos queda

#  x₁ + x₂ con las condiciones:

#  -x₁ + 2x₂ + x₃ = 4
#  2x₁ +x₂ + x₄ = 10
#  x₁ ≥ 0, x₂ ≥ 0, x₃ ≥ 0, x₄ ≥ 0





#  El sistema Ax = b tiene un conjunto de soluciones
#  x1, x2, x3, x4

a = [
    [-1, 2, 1, 0],
    [2, 1, 0, 1],
    [0, 0, 1, 0], # condicion 1x3
    [0, 0, 0, 1]  # condición 1x4
]

#   queremos x3 = 0 y x4 = 0
b = [4, 10, 0, 0]

x1, x2, x3, x4 = np.linalg.solve(a, b)

print('x1 =', x1)
print('x2 =', x2)
print('x3 =', x3)
print('x4 =', x4)

print(x1+x2)
print(-x1 + 2*x2 + x3)






