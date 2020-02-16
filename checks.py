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

def check_players_rating(Tplayers_list, rating_list):
    '''
    Check if players from the tournament with rating are in the rating list
    And if the rating matches
    '''