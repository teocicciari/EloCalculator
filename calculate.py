def calculate(player_list):
	'''
	returns two lists:
	variations = (name, games, old_rating, new_rating)
	new_players = (name, games, score, av.oponents)
	'''

	variations = []
	new_players = []

	for player in player_list:
		if (player[1] == 0):	# Si no tiene elo

			games4elo = 0
			score = 0
			average_oponents = 0

			rounds = player[2]
			for round in rounds:
				oponent = round[0] - 1
				ratingB = player_list[oponent][1]
				
				if (ratingB != 0):
					games4elo = games4elo + 1
					score = score + float(round[1])
					average_oponents = average_oponents + ratingB

			try:
				average_oponents = average_oponents / games4elo
				new_players.append((player[0], games4elo, score, int(average_oponents)))

			except:
				pass

		else:
			sExpected = 0
			points = 0
			games = 0

			k = player[3]
			
			ratingA = player[1]
			rounds = player[2]
			
			for round in rounds:
				games = games+1
				points = points + float(round[1])
				
				oponent = round[0] - 1
				ratingB = player_list[oponent][1]
				expected = 1.0 * 1.0 / (1 + pow(10, 1.0 * (ratingB - ratingA) / 400))
				sExpected = sExpected + expected
			
			newRating = ratingA + k * (points - sExpected)
			
			variations.append((player[4], player[0], games, player[5], ratingA, int(newRating)))
	
	return(variations, new_players)