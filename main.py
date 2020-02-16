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
    # players_list = read_players(text)
    # check_players_rating()


if __name__== "__main__":
    main()