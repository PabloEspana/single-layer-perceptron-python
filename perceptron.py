"""Creación de perceptrón simple o neurona artificial usado la fórmula de
Frank Rosenblatt para calcular los nuevos pesos 
Este perceptrón aprenderá la tabla del AND o del OR"""

import numpy as np

class Perceptron():
	entradas = np.array([[1,1,1],[1,0,0],[0,1,0],[0,0,0]]) # tabla AND
	#entradas = np.array([[1,1,1],[1,0,1],[0,1,1],[0,0,0]]) # tabla OR
	pesos = np.random.uniform(-1, 1, 3)
	salida_entera = None
	aprendiendo = True
	iteraciones = 0
	tasa_de_aprendizaje  = 0.3

	while aprendiendo:
		print('Aprendiendo')
		aprendiendo = False
		for x in range(0, 4): # Recorrido de las 4 filas de las entradas
			salida_real = (entradas[x][0] * pesos[0]) + (entradas[x][1] * pesos[1]) + pesos[2]
			print("salida: " + str(salida_real))
			if salida_real > 0:
				salida_entera = 1
			else:
				salida_entera = 0
			print(salida_entera)
			error = entradas[x][2] - salida_entera
			if error != 0:
				pesos[0] = pesos[0] + ( tasa_de_aprendizaje  * error * entradas[x][0])
				pesos[1] = pesos[1] + ( tasa_de_aprendizaje  * error * entradas[x][1])
				pesos[2] = pesos[2] + ( tasa_de_aprendizaje  * error * 1)
				aprendiendo = True
		iteraciones = iteraciones + 1
	

	print('Iteraciones ' + str(iteraciones))
	print('Pesos correctos: ' + str(pesos))

	for x in range(0, 4): # Recorrido de las 4 filas de las entradas
		salida_real = (entradas[x][0] * pesos[0]) + (entradas[x][1] * pesos[1]) + pesos[2]
		if salida_real > 0:
			salida_entera = 1
		else:
			salida_entera = 0
		print('Entradas: ' + str(entradas[x][0]) + ' y ' + str(entradas[x][1])  
			+ ' = ' + str(entradas[x][2]) + ' Perceptrón: ' + str(salida_entera))

Perceptron()