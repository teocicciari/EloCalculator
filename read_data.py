# -*- coding: utf-8 -*-
from player import Player
import re

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

def getPlayers_suizo(t):
    player_list = []

    num_lines = sum(1 for line in t)
    num_rounds = int((len(t[8])-66)/5)

    for line in range(9, num_lines):
        player = t[line]

        name = player[13:36].rstrip()
        elo = int(player[36:40])
        results = []

        for j in range(0, num_rounds):
            offset = j*8

            try:
                oponent = int(player[45+offset:47+offset].strip())
                result = player[51+offset].strip()
                result = re.sub('½','.5',result)
                result = float(result)

                r = (oponent, result)
                results.append(r)
            except ValueError:
                pass
            
        player = (name, elo, results)
        player_list.append(player)

    return(player_list)

def getPlayers_americano(t):

    player_list = []

    num_lines = sum(1 for line in t)
    num_rounds = num_lines - 9
    if ((num_rounds % 2) != 0): # Si el num de jugadores impar se suma uno
        num_rounds = num_rounds + 1

    for line in range(9, num_lines):
        player = t[line]

        name = player[13:36].rstrip()
        elo = int(player[36:40])
        results = []

        for oponent in range(1, num_rounds + 1):
            offset = oponent*2
        
            try:
                result = player[45+offset].strip()
                result = re.sub('½','.5',result)
                result = float(result)

                r = (oponent, result)
                results.append(r)
            except ValueError:
                pass

        player = (name, elo, results)
        player_list.append(player)

    return(player_list)

def read_players(text, tType):
    '''
    Read the players from the new tournament
    Check if the players are in the rating list
    Check if the rating match
    Returns two list: list of the players with rating,
    list with new players
    '''
    print('..................................................')
    print("Read players from the tournament")
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    new_players = []

    if (tType == 'a'):
        player_list = getPlayers_americano(text) 
    else:
        player_list = getPlayers_suizo(text)

    for player in player_list:
        if (player[1] == 0):
            new_players.append(player)
            player_list.remove(player)

    print('..................................................')
    print("Players with rating: ")
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    for p in player_list:
        print(p[0] + ' ' + str(p[1]))
    
    print('..................................................')
    print("Players without rating: ")
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    for p in new_players:
        print(p[0] + ' ' + str(p[1]))

    return(player_list, new_players)