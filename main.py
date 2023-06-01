import sys
from functions import *


def main():
    if len(sys.argv) > 1:
        # simulation mode
        if sys.argv[1] == "-s" or sys.argv[1] == "-S":
            print("simulatie modus")
            sim_mode = int(input("1 voor verder gaan van vorige situatie, 2 voor opnieuw beginnen: "))
            if sim_mode == 1:
                simulation_mode(True)
            if sim_mode == 2:
                simulation_mode(False)
        else:
            print("geen geldige modus")
    else:
        operating_mode = int(input("1 voor simulatie, 2 voor fiets lenen/terugplaatsen, 3 voor HTML: "))
        if operating_mode == 1:
            print("simulatie modus")
            sim_mode = int(input("1 voor verder gaan van vorige situatie, 2 voor opnieuw beginnen: "))
            if sim_mode == 1:
                simulation_mode(True)
            if sim_mode == 2:
                simulation_mode(False)
        elif operating_mode == 2:
            sim_mode = int(input("1 voor lenen, 2 voor terugplaatsen: "))
            if sim_mode == 1:
                user_ = int(input("1 voor gebruiker, 2 voor transporteur: "))
                if user_ == 1:
                    leen_fiets(stations, "gebruiker", user_for_non_sim)
                if user_ == 2:
                    leen_fiets(stations, "transporteur", transporteur_for_non_sim)
            if sim_mode == 2:
                user_ = int(input("1 voor gebruiker, 2 voor transporteur: "))
                if user_ == 1:
                    zet_fiets_terug(stations, "gebruiker", user_for_non_sim)
                if user_ == 2:
                    zet_fiets_terug(stations, "transporteur", transporteur_for_non_sim)
        elif operating_mode == 3:
            get_html()
        else:
            print("geen geldige modus")


def leen_fiets(stations, type_of_user, user):
    print("---------------------------------------------")
    print("|          zelf station ingeven: 1          |")
    print("|     kiezen uit beschikbare stations: 2    |")
    print("|                  quit: 3                  |")
    print("---------------------------------------------")
    operating_mode = int(input("kies modus: "))
    while operating_mode not in [1, 2, 3]:
        print("geen geldige modus")
        operating_mode = int(input("kies modus"))
    if type_of_user == "gebruiker":
        match operating_mode:
            case 1:
                station = input("geef station op: ")
                for element in stations:
                    if element.naam == station:
                        aantal_fietsen = element.capaciteit - element.sloten
                        print(f"{aantal_fietsen} fietsen beschikbaar in {station}")
                        if aantal_fietsen > 0:
                            succes = user.neem_fiets(element)
                            if not succes:
                                print("je hebt al een fiets")
                                main()
                            else:
                                print("fiets geleend")
                                main()
                        else:
                            print("geen fietsen beschikbaar")
                            leen_fiets(stations, "gebruiker", user_for_non_sim)
            case 2:
                available = available_bikes(stations)
                gekozen_station = int(input("kies station 1 - 5: "))
                succes = user.neem_fiets(available[gekozen_station-1])
                if succes:
                    print("fiets geleend")
                    main()
                else:
                    print("je hebt al een fiets")
                    main()
            case 3:
                main()
    elif type_of_user == "transporteur":
        match operating_mode:
            case 1:
                station = input("geef station op: ")
                for element in stations:
                    if element.naam == station:
                        aantal_fietsen = element.capaciteit - element.sloten
                        print(f"{aantal_fietsen} fietsen beschikbaar in {station}")
                        fietsen_nemen = int(input("Hoeveel fietsen uit station nemen?: "))
                        if fietsen_nemen > aantal_fietsen:
                            print("niet genoeg fietsen beschikbaar")
                            leen_fiets(stations, "transporteur", transporteur_for_non_sim)
                        else:
                            transporteur_for_non_sim.neem_fietsen(element, fietsen_nemen)
                            main()
            case 2:
                available = available_bikes(stations)
                gekozen_station = int(input("kies station 1 - 5: "))
                transporteur_station = available[gekozen_station - 1]
                aantal_fietsen = transporteur_station.capaciteit - transporteur_station.sloten
                print(f"{aantal_fietsen} fietsen beschikbaar in {transporteur_station.naam}")
                fietsen_nemen = int(input("Hoeveel fietsen uit station nemen?: "))
                if fietsen_nemen > aantal_fietsen:
                    print("niet genoeg fietsen beschikbaar")
                    leen_fiets(stations, "transporteur", transporteur_for_non_sim)
                else:
                    transporteur_for_non_sim.neem_fietsen(transporteur_station, fietsen_nemen)
                    main()
            case 3:
                main()


def zet_fiets_terug(stations, type_of_user, user):
    print("---------------------------------------------")
    print("|          zelf station ingeven: 1          |")
    print("|     kiezen uit beschikbare stations: 2    |")
    print("|                  quit: 3                  |")
    print("---------------------------------------------")
    operating_mode = int(input("kies modus: "))
    while operating_mode not in [1, 2, 3]:
        print("geen geldige modus")
        operating_mode = int(input("kies modus"))
    if type_of_user == "gebruiker":
        match operating_mode:
            case 1:
                station = input("geef station op: ")
                for element in stations:
                    if element.naam == station:
                        print(f"{element.sloten} plaatsen beschikbaar in {station}")
                        if element.sloten > 0:
                            succes = user.plaats_fiets(element)
                            if not succes:
                                print("je hebt geen fiets")
                                main()
                            else:
                                print("fiets terug geplaatst")
                                main()
                        else:
                            print("geen sloten beschikbaar")
                            zet_fiets_terug(stations, "gebruiker", user_for_non_sim)
            case 2:
                available = available_stations(stations)
                gekozen_station = int(input("kies station 1 - 5: "))
                succes = user.plaats_fiets(available[gekozen_station - 1])
                if succes:
                    print("fiets teruggeplaatst")
                    main()
                else:
                    print("je hebt geen fiets")
                    main()
            case 3:
                main()
    elif type_of_user == "transporteur":
        match operating_mode:
            case 1:
                station = input("geef station op: ")
                for element in stations:
                    if element.naam == station:
                        print(f"{element.sloten} plaatsen beschikbaar in {station}")
                        fietsen_plaatsen = int(input("Hoeveel fietsen in station zetten?: "))
                        if fietsen_plaatsen > element.sloten:
                            print("niet genoeg plaatsen beschikbaar")
                            zet_fiets_terug(stations, "transporteur", transporteur_for_non_sim)
                        else:
                            transporteur_for_non_sim.plaats_fietsen(element, fietsen_plaatsen)
                            print(f"{fietsen_plaatsen} fietsen in station {element.naam}")
                            main()
            case 2:
                available = available_stations(stations)
                gekozen_station = int(input("kies station 1 - 5: "))
                transporteur_station = available[gekozen_station - 1]
                print(f"{transporteur_station.sloten} plaatsen beschikbaar in {transporteur_station.naam}")
                fietsen_plaatsen = int(input("Hoeveel fietsen in station zetten?: "))
                if len(transporteur_for_non_sim.fietsen) >= fietsen_plaatsen:
                    if fietsen_plaatsen > transporteur_station.sloten:
                        print("niet genoeg plaatsen beschikbaar")
                        zet_fiets_terug(stations, "transporteur", transporteur_for_non_sim)
                    else:
                        transporteur_for_non_sim.plaats_fietsen(transporteur_station, fietsen_plaatsen)
                        main()
                else:
                    print(f"je hebt nog maar {len(transporteur_for_non_sim.fietsen)} beschikbaar")
                    zet_fiets_terug(stations, "transporteur", transporteur_for_non_sim)
            case 3:
                main()


user_for_non_sim = Gebruiker(1, "sys", "sys")
transporteur_for_non_sim = Transporteur(1)
stations = vul_stations(maak_stations())
main()
