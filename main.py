import sys
from functions import *

user_for_non_sim = Gebruiker(1, "sys", "sys")
transporteur_for_non_sim = Transporteur(1)
stations = vul_stations(maak_stations())


def my_main():
    if len(sys.argv) > 1:
        # simulation mode
        if sys.argv[1] == "-s" or sys.argv[1] == "-S":
            print("simulatie modus")
            sim_mode = int(input("1 voor verder gaan van vorige situatie, 2 voor opnieuw beginnen: "))
            if sim_mode == 2:
                speed = float(input("kies snelheid [0.0001, 100]: "))
                simulation_mode(True, stations, my_main, speed)
            if sim_mode == 1:
                # unpickle data
                with open("pickle.dat", "rb") as f:
                    data = pickle.load(f)
                speed = int(input("kies snelheid [0.0001, 100]: "))
                simulation_mode(False, data[2], my_main, speed, data[0], data[1])
        else:
            print("geen geldige modus")
    else:
        operating_mode = float(input("1 voor simulatie, 2 voor fiets lenen/terugplaatsen, 3 voor HTML,"
                                   "4 voor te quitten: "))
        if operating_mode == 1:
            print("simulatie modus")
            sim_mode = int(input("1 voor verder gaan van vorige situatie, 2 voor opnieuw beginnen: "))
            if sim_mode == 2:
                speed = float(input("kies snelheid [0.0001, 100]: "))
                simulation_mode(True, stations, my_main, speed)
            if sim_mode == 1:
                # unpickle data
                with open("pickle.dat", "rb") as f:
                    data = pickle.load(f)
                speed = float(input("kies snelheid [0.0001, 100]: "))
                simulation_mode(False, data[2], my_main, speed, data[0], data[1])
        elif operating_mode == 2:
            sim_mode = int(input("1 voor lenen, 2 voor terugplaatsen: "))
            if sim_mode == 1:
                user_ = int(input("1 voor gebruiker, 2 voor transporteur: "))
                if user_ == 1:
                    leen_fiets(stations, "gebruiker", user_for_non_sim, my_main)
                if user_ == 2:
                    leen_fiets(stations, "transporteur", transporteur_for_non_sim, my_main)
            if sim_mode == 2:
                user_ = int(input("1 voor gebruiker, 2 voor transporteur: "))
                if user_ == 1:
                    zet_fiets_terug(stations, "gebruiker", user_for_non_sim, my_main)
                if user_ == 2:
                    zet_fiets_terug(stations, "transporteur", transporteur_for_non_sim, my_main)
        elif operating_mode == 3:
            get_html()
        elif operating_mode == 4:
            pass
        else:
            print("geen geldige modus")


my_main()
