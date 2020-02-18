# -*- coding: utf-8 -*-
import re
from player import *

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
                player = line.split(' - ')
                p = Rated_player(player[0], player[1], int(player[2]), int(player[3]))
                players.append(p)
            except Exception as e:
                print(e)

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
                p = Entry_player(player[0], int(player[1]), float(player[2]), float(player[3]))
                players.append(p)
            except Exception as e:
                print(e)
        
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
        rating = int(player[36:40])
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
            
        player = Player(name, rating, results)
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
        rating = int(player[36:40])
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

        player = Player(name, rating, results)
        player_list.append(player)

    return(player_list)

def read_players(text, tourn_type):
    '''
    Read the players from the new tournament
    returns a list of them
    '''
    print('..................................................')
    print("Read players from the tournament")
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    if (tourn_type == 'a'):
        player_list = getPlayers_americano(text) 
    else:
        player_list = getPlayers_suizo(text)

    return(player_list)