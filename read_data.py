# -*- coding: utf-8 -*-
from player import Player

def read_rating_list():
    '''
    Read the rating list from file, then append the players on a list
    '''
    print('..................................................')
    print("Read rating list")
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    with open("rating_list", "r") as file:
        players = []

        for line in file.readlines():
            try:
                p = line.split(' - ')
                players.append(Player(p[0], p[1], int(p[2]), int(p[3])))
            except Exception as e:
                print(e)
        
        for player in players:
            print(player.name + ' - ' + str(player.rating)+ ' - ' + str(player.k))
	
    print('..................................................')
    print('OK!')
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
	
    return(players)

def read_entry_list():
    '''
    Read the entry list from file, this is the list with players who have played
    rating games but not enough
    '''
    print('..................................................')
    print("Read entry list")
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    with open("entry_list", "r") as file:
        players = []
        for line in file.readlines():
            try:
                player = line.split(' - ')
                player = (player[0], int(player[1]), float(player[2]), float(player[3]))
                players.append(player)
            except Exception as e:
                print(e)
        
        for player in players:
            print(player[0]+ ' - ' + str(player[3]))
    
    print('..................................................')
    print('OK!')
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    return(players)

def read_file(filename):
    with open(filename, "r") as file:
        text = file.readlines()
    
    return(text)

def read_tournament(text):
    '''
    Read the info of the tournament
    '''
    nameT = text[0].rstrip()
    organizator = text[2][31:].rstrip()
    eloMed = text[3][31:35].rstrip()
    date = text[4][31:42].rstrip()

    if (text[8][45:50] == "1.Rd."):
        type_T = "s"
    else:
        type_T = "a"

    return(nameT, date, organizator, eloMed, type_T)

def read_players(text):
    '''
    Read the players from the new tournament
    Returns the list of players
    '''