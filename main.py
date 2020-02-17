# -*- coding: utf-8 -*-

from read_data import *
from checks import *

def main():
    # Reading the lists
    rating_list = read_rating_list()
    entry_list = read_entry_list()

    # Getting the info from the tournament
    filename = input("Nombre del archivo de input: ")
    text = read_file(filename)
    check_file(text)
    tournament = read_tournament(text)

    # in player_list are the players with rating
    (players_list, new_players) = read_players(text, tournament[4])
    # check_players_rating(player_list, rating_list)


if __name__== "__main__":
    main()