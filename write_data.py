from player import *
import os
import datetime
from datetime import date

def write_entry_list(entry_list):

    os.rename("entry_list", "entry_list.bak")
    with open("entry_list", "w") as file:
        for p in entry_list:
            if not p.entring:
                file.write("{0} - {1} - {2} - {3}\n".format(p.name, p.n_games,
                                                            p.score, p.av_op))

def write_rating_list(player_list, entry_list):
    id = 0

    os.rename("rating_list", "rating_list.bak")
    with open("rating_list", "w") as file:
        for p in player_list:
            if p.rankeado:
                file.write("{0} - {1} - {2} - {3}\n".format(p.id, p.name,
                                                        p.rating, p.n_games))
            if p.id > id:
                id = int(p.id)
        
        for p in entry_list:
            if p.entring:
                file.write("{0} - {1} - {2} - {3}\n".format(id, p.name,
                                                        p.rating, 0))
                id += id

def write_report(player_list, entry_list, tournament):
    with open("report", "w") as file:
        file.write("{0}\n".format(date.today()))
        file.write("Reporte del torneo {0}\njugado el {1}\n\n".format(tournament[0],
                                                        tournament[1]))
        file.write("Variaciones de rating:\n")

        for p in player_list:
            if p.rankeado:
                file.write("{0}: {1} -> {2} ({3})\n".format(p.name, p.old_rating,
                                                        p.rating, p.variation))
        
        file.write("\nNuevos jugadores:\n")
        for p in entry_list:
            if p.entring:
                file.write("{0} entró con {1}\n".format(p.name, p.rating))