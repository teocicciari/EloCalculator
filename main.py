# -*- coding: utf-8 -*-

from read_data import *
from checks import *

def main():
    rating_list = read_rating_list()
    entry_list = read_entry_list()

    filename = input("Nombre del archivo de input: ")
    text = read_file(filename)
    check_file(text)
    tournament = read_tournament(text)


if __name__== "__main__":
    main()