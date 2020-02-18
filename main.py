# -*- coding: utf-8 -*-

from read_data import *
from checks import *
from calculate import *
from write_data import *
import sys

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

    errors = check_players_rating(player_list, rating_list)
    if errors == 0:
        print("Everything OK")
    else:
        sys.exit()

    # Makes the messy things
    calculate(player_list)
    calculate_init(player_list, entry_list)

    # Write all the files!
    write_entry_list(entry_list)
    write_rating_list(player_list, entry_list)
    write_report(player_list, entry_list, tournament)

if __name__== "__main__":
    main()