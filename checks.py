# -*- coding: utf-8 -*-

import re

def check_file(text):
    '''
    Check that the input file have the right format
    '''

    patterns = ['Organizador', 'Elo medio', 'Fecha', '', 'Clasificación Final', '', 'Rank']
    cErrors = 0

    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    print("CHECKEAR FORMATO:")
    print('...')

    for i in range(7):
        if not (re.search(patterns[i], text[i+2])):
            cErrors = cErrors+1
            print("pattern: ", patterns[i])
            print("file: ", text[i+2])

    if (cErrors != 0):
        print('Errores encontrados en el formato: ', cErrors)
        print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    else:
        print('Formato de archivo OK!')
        print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

def check_players_rating(players_list, rating_list):
    '''
    Check if players from the tournament with rating are in the rating list
    And if the rating matches

    TODO: que hacer en los casos de no matcheo
    '''

    print('..................................................')
    print("Chequendo los jugadores en la base...")
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    new_players_list = []
    for player in players_list:
        if (player[1] != 0):
            p = [_player for _player in rating_list if (_player[1] == player[0])]
            try:
                p = p[0]
                if (player[1] != p[2]):
                    print("el rating de "+player[0]+" no coincide con la base")
                else:
                    player = (player[0], player[1], player[2], p[3], int(p[0]), int(p[4]))
                    new_players_list.append(player)
                    print("jugador OK")
            except IndexError:
                print("el jugador "+player[0]+" no se encuentra en la base")
        else:
            new_players_list.append(player)

    return(new_players_list)
