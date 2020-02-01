#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import datetime
from datetime import date
	
def print_menu():
	
	print("\nMenu")
	print("´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
	print("Calcular elo:")
	print("1) Torneo suizo")
	print("2) Torneo americano")
	print("´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
	
	option = "0"
	while not((option == "1") | (option == "2")):
		option = input("Ingrese una opción: ")

	return(int(option))
	
def checkFile(text):

	patterns = ['Organizador', 'Elo medio', 'Fecha', '', 'Clasificación Final', '', 'Rank']
	cErrors = 0

	print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
	print("CHECKEAR FORMATO:")
	print('...')

	for i in range(7):
		if not (re.search(patterns[i], text[i+2])):
			cErrors = cErrors+1
			print("pattern: ", patterns[i])
			print("file: ", text[i+2])

	if (cErrors != 0):
		print('Errores encontrados en el formato: ', cErrors)
		print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

	else:
		print('Formato de archivo OK!')
		print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

	return(text[0])

def getData_suizo(t):
	
	num_lines = sum(1 for line in t)
	num_rounds = int((len(t[8])-66)/5)

	"""data del torneo"""
	organizador = t[2][31:].rstrip()
	eloMedio = t[3][31:35].rstrip()
	fecha = t[4][31:42].rstrip()

	player_list = []

	for line in range(9, num_lines):
		player = t[line]

		name = player[13:36].rstrip()
		elo = int(player[36:40])

		results = []
		for j in range(0, num_rounds):
			offset = j*8

			try:
				oponent = int(player[45+offset:47+offset].strip())
				result = player[51+offset].strip()
				result = re.sub('½','.5',result)
				result = float(result)

				r = (oponent, result)
				results.append(r)
			except ValueError:
				pass

		player = (name, elo, results)
		player_list.append(player)

	return(player_list)

def getData_americano(t):
	
	num_lines = sum(1 for line in t)
	num_rounds = num_lines - 9
	if ((num_rounds % 2) != 0): # Si el num de jugadores impar se suma uno
		num_rounds = num_rounds + 1

	player_list = []

	for line in range(9, num_lines):
		player = t[line]

		name = player[13:36].rstrip()
		elo = int(player[36:40])

		results = []
		for j in range(0, num_rounds):
			offset = j*2
			
			try:
				oponent = j + 1

				result = player[45+offset].strip()
				result = re.sub('½','.5',result)
				result = float(result)

				r = (oponent, result)
				results.append(r)
			except ValueError:
				pass

		player = (name, elo, results)
		player_list.append(player)

	return(player_list)

def calculate_and_write(player_list, tournamentName):
	
	outFilename = input("Nombre del archivo de output: ")
	outFilemame = outFilename + ".txt"
	
	file = open(outFilename, "w+")
	file.write("Reporte del torneo {0}".format(tournamentName))
	file.write("{0}\n\n".format(date.today()))

	print("Factor K")
	print("´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
	print("Ingrese el factor k para cada jugador:")
	print("1) k 40")
	print("2) k 20")
	print("3) k 10")
	print("´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
	
	for player in player_list:
		if (player[1] == 0):	# Si no tiene elo

			games4elo = 0
			score = 0
			average_rating_oponents = 0

			rounds = player[2]
			for round in rounds:
				rank_oponent = round[0] - 1
				ratingB = player_list[rank_oponent][1]
				
				if (ratingB != 0):
					games4elo = games4elo + 1
					score = score + float(round[1])
					average_rating_oponents = average_rating_oponents + ratingB

			try:
				average_rating_oponents = average_rating_oponents / games4elo

				# TODO: Calcular la performance!

				file.write("\n{0} no tiene elo, jugó {1} partidas\nScore: {2} - Performance: {3}\n\n"
					.format(player[0], games4elo, score, average_rating_oponents))
			except ZeroDivisonError:
				file.write("\n{0} no tiene elo, no jugó partidas contra jugadores rankeados\n\n"
					.format(player[0]))
		
		else: # Jugadores con elo
			sExpected = 0
			points = 0

			coefK = "0"
			while not((coefK == "1") | (coefK == "2") | (coefK == "3")):
				coefK = input(player[0])
				if (coefK == "1"):
					k = 40
				elif (coefK == "2"):
					k = 20
				elif (coefK == "3"):
					k = 10
				else:
					print("Error de input, vuelva a ingresar su opción")
			
			ratingA = player[1]
			rounds = player[2]
			
			for round in rounds:
				points = points + float(round[1])
				
				rank_oponent = int(round[0]) - 1
				ratingB = player_list[rank_oponent][1]
				expected = 1.0 * 1.0 / (1 + pow(10, 1.0 * (ratingB - ratingA) / 400))
				sExpected = sExpected + expected
			
			newRating = ratingA + k * (points - sExpected)
			
			if (newRating > ratingA):
				variation = newRating - ratingA
				file.write("{0} teniá {1} - subió {2} puntos (k: {3}) - Nueva puntuación: {4} \r\n"
					.format(player[0],ratingA, int(variation), k, int(newRating)))
				
			if (newRating < ratingA):
				variation = ratingA - newRating
				file.write("{0} teniá {1} - bajó {2} puntos (k: {3}) - Nueva puntuación: {4} \r\n"
					.format(player[0],ratingA, int(variation), k, int(newRating)))

def main():
	
	option = print_menu()
		
	filename = input("Nombre del archivo de input: \n")
	
	try:
		with open(filename, "r", encoding="utf-8") as file:
			text = file.readlines()
	except FileNotFoundError:
		print("Archivo no encontrado")
		input3 = input("presione ENTER para salir")
		return(0)

	tournamentName = checkFile(text)
	
	if (option == 1):
		player_list = getData_suizo(text)
	elif (option == 2):
		player_list = getData_americano(text)

	calculate_and_write(player_list, tournamentName)
	
	input3 = input("presione ENTER para salir")

if __name__== "__main__":
	main()