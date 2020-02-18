from read_data import Entry_player

# this conversion table can be found in the fide handbook
# https://handbook.fide.com/chapter/B022017

conversion_table = { 1.0 : 800, 0.99 : 677 , 0.98 : 589 , 0.97 : 538, 
                    0.96 : 501, 0.95 : 470 , 0.94 : 444, 0.93 : 422, 
                    0.92 : 401, 0.91 : 383, 0.90 : 366, 0.89 : 351, 
                    0.88 : 336, 0.87 : 322, 0.86 : 309, 0.85 : 296, 
                    0.84 : 284, 0.83 : 273, 0.82 : 262, 0.81 : 251, 
                    0.80 : 240, 0.79 : 230, 0.78 : 220, 0.77 : 211, 
                    0.76 : 202, 0.75 : 193, 0.74 : 184, 0.73 : 175, 
                    0.72 : 166, 0.71 : 158, 0.70 : 149, 0.69 : 141, 
                    0.68 : 133, 0.67 : 125, 0.66 : 117, 0.65 : 110,
                    0.64 : 102, 0.63 : 95, 0.62 : 87, 0.61 : 80, 0.60 : 72, 
                    0.59 : 65, 0.58 : 57, 0.57 : 50, 0.56 : 43, 0.55 : 36, 
                    0.54 : 29, 0.53 : 21, 0.52 : 14, 0.51 : 7, 0.50 : 0, 
                    0.49 : -7, 0.48 : -14 , 0.47 : -21 , 0.46 : -29 , 
                    0.45 : -36 , 0.44 : -43 , 0.43 : -50 , 0.42 : -57 , 
                    0.41 : -65 , 0.40 : -72 , 0.39 : -80 , 0.38 : -87 , 
                    0.37 : -95 , 0.36 : -102, 0.35 : -110, 0.34 : -117, 
                    0.33 : -125, 0.32 : -133, 0.31 : -141, 0.30 : -149, 
                    0.29 : -158, 0.28 : -166, 0.27 : -175, 0.26 : -184, 
                    0.25 : -193, 0.24 : -202, 0.23 : -211, 0.22 : -220, 
                    0.21 : -230, 0.20 : -240, 0.19 : -251, 0.18 : -262, 
                    0.17 : -273, 0.16 : -284, 0.15 : -296, 0.14 : -309, 
                    0.13 : -322, 0.12 : -336, 0.11 : -351, 0.10 : -366, 
                    0.09 : -383, 0.08 : -401, 0.07 : -422, 0.06 : -444, 
                    0.05 : -470, 0.04 : -501, 0.03 : -538, 0.02 : -589, 
                    0.01 : -677, 0.00 : -800 }

def calculate(player_list):
	'''
	This function gets the performance of the players
	it perform the most messy things of the program
	'''
	for player in player_list:
		if (player.rating == 0):
			n_games, score, av_op = 0, 0, 0
			rounds = player.results

			for round in rounds:
				oponent = round[0] - 1
				ratingB = player_list[oponent].rating
				
				if (ratingB != 0):
					n_games = n_games + 1
					score = score + float(round[1])
					av_op = av_op + ratingB

			try:
				av_op = av_op / n_games
				player.refresh_data_nr(n_games, score, av_op)
			except:
				pass

		else:
			sExpected, points, n_games = 0, 0, 0

			k = player.k
			ratingA = player.rating
			rounds = player.results
			
			for round in rounds:
				n_games = n_games+1
				points = points + float(round[1])
				oponent = round[0] - 1
				ratingB = player_list[oponent].rating
				expected = 1.0 * 1.0 / (1 + pow(10, 1.0 * (ratingB - ratingA) / 400))
				sExpected = sExpected + expected
			
			newRating = ratingA + k * (points - sExpected)
			player.refresh_rating(int(newRating), n_games)

def calculate_init(player_list, entry_list):
	'''
	For every player without rating it searches in the entry list:
	+ merge the info if found
	+ append the player to the entry list if is not there

	mark the players who have enough games to get rating
	'''

	for p in player_list:
		if not p.rankeado:
			ep = [_player for _player in entry_list if (_player.name == p.name)]
			# this line searchs the player in the entry list and returns it if found
			# (inside of a list)

			if (ep != []):
				ep = ep[0]
				n_games = ep.n_games + p.n_games
				av_op = ((p.av_op * p.n_games) + (ep.av_op * ep.n_games)) / (n_games)

				score = ep.score + p.score
				ep.refresh(score, n_games, av_op)

			else:
				new_ep = Entry_player(p.name, p.n_games, p.score, p.av_op)
				entry_list.append(new_ep)

	for player in entry_list:
		if (player.n_games >= 5):
			mid = (player.n_games)/2

			if (player.score == mid):
				new_rating = player.av_op

			elif (player.score > mid):
				new_rating = player.av_op + (player.score - mid)*40

			else:
				per = format(player.score/player.n_games, '.2f')
				var = conversion_table[float(per)]
				new_rating = av_op + var

			player.new_rated(new_rating)