import pulp as p

'''
    P = Max 7x1 + 4x2 +3x3
    s.a
    x1 + 2x2 + 2x3 <= 30
    2x1 +x2 +2x3 <= 45
    x1+x2+x3 >= 0
'''
problema = p.LpProblem("simplex",p.LpMaximize)

#Definir las variables de decisión
x1 = p.LpVariable("x1", lowBound = 0, cat = p.LpContinuous)
x2 = p.LpVariable("x2", lowBound = 0, cat = p.LpContinuous)
x3 = p.LpVariable("x3", lowBound = 0, cat = p.LpContinuous)

#Definimos la función objetivo
problema += 7*x1 + 4*x2 + 3*x3, 'Funcion Objetivo'

#Definimos la restricciones
problema += x1 + 2*x2 + 2*x3 <= 30 , 'R1'
problema += 2*x1 + x2 + 2*x3 <= 45 , 'R2'

problema.solve()

print("Valor de x1: ", x1.value())
print("Valor de x2: ", x2.value())
print("Valor de x3: ", x3.value())

print("Valor optimo: ", p.value(problema.objective))
