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

    check_players_rating(player_list, rating_list)

    calculate(player_list)
    calculate_init(player_list, entry_list)

    for p in player_list:
        if p.rankeado:
            print(p.name +' - '+str(p.old_rating)+' -> '+str(p.rating))

    for p in entry_list:
        if p.entring:
            print(p.name +' entró con '+ str(p.rating))


if __name__== "__main__":
    main()