# -*- coding: utf-8 -*-

from read_data import *
from checks import *
from calculate import *

def main():
    # Reading the lists

    rating_list = read_rating_list()
    # rating_list = (id, name, rating, k)

    entry_list = read_entry_list()
    # entry_list = (name, n_games, score, av_op)

    # Getting the info from the tournament
    filename = input("Nombre del archivo de input: ")
    text = read_file(filename)
    check_file(text)
    tournament = read_tournament(text)

    player_list = read_players(text, tournament[4])
    # player_list = [(name, rating, results)]
                                    # results = [(oponent, result)]

    player_list = check_players_rating(player_list, rating_list)

    (variations, new_players) = calculate(player_list)
	# variations = (name, games, old_rating, new_rating)
	# new_players = (name, games, score, av.oponents)

    for player in variations:
        print (player)
    print("-----------------------")
    for player in new_players:
        print (player)


if __name__== "__main__":
    main()