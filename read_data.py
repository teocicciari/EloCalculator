# -*- coding: utf-8 -*-
from player import Player

def read_rating_list():
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    print("Read rating list")

    with open("rating_list", "r") as file:
        players = []

        for line in file.readlines():
            try:
                p = line.split(' - ')
                players.append(Player(p[0], p[1], int(p[2]), int(p[3])))
            except Exception as e:
                print(e)
                print(player)
	
    print('OK!')
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
	
    return(players)

def read_entry_list():
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    print("Read entry list")

    with open("entry_list", "r") as file:
        players = []
        for line in file.readlines():
            try:
                player = line.split(' - ')
                player = (player[0], int(player[1]), float(player[2]), float(player[3]))
                players.append(player)
            except Exception as e:
                print(e)
                print(player)
    
    print('OK!')
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    return(players)

def read_file(filename):
    with open(filename, "r") as file:
        text = file.readlines()
    
    return(text)

def read_tournament(text):
    nameT = text[0].rstrip()
    organizator = text[2][31:].rstrip()
    eloMed = text[3][31:35].rstrip()
    date = text[4][31:42].rstrip()

    if (text[8][45:50] == "1.Rd."):
        type_T = "s"
    else:
        type_T = "a"

    return(nameT, date, organizator, eloMed, type_T)