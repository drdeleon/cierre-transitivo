import numpy as np

MA = [
	[0,0,1,1], #1
	[1,0,0,0], #2
	[0,1,0,0], #3
	[0,0,0,0], #4
]


print(MA[0][3])
print(len(MA))

for i in range(0, len(MA)):
	for j in range(0, len(MA)):
		for k in range(0, len(MA)):
			MA[i][j] = MA[i][j] or (MA[i][k] and MA[k][j])


print("Matriz resultante (Cierre transitivo)")
for row in range(0, len(MA)):
	print(MA[row])
