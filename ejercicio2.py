import pulp as p

'''
P1: Max z = x1 + x2
S.A
x1 + 2x2 >= 30
3x1 +x2 <= 30
x1, x2 >= 0
'''

problema = p.LpProblem("2fases",p.LpMaximize)

#Definir variables de decisión
x1 = p.LpVariable("x1",lowBound=0,cat = p.LpContinuous)
x2 = p.LpVariable("x2",lowBound=0,cat = p.LpContinuous)

#Definir funcion Objetivo
problema += x1 + x2, "Func. Objetivo"

#Definir restricciones
problema += x1 + 2*x2 >= 30, "R1"
problema += 3*x1 + x2 <= 30, "R2"

problema.solve()

print("Valor x1: ", x1.value())
print("Valor x2: ", x2.value())
print("Valor optimo: ",p.value(problema.objective))

