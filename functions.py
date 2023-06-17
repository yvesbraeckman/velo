import random
import time
from classes import *
import pickle
import yaml
from jinja2 import Environment, FileSystemLoader
import os


def available_bikes(stations, amount_of_stations=5):
    """
    Functie geeft een lijst terug met gevraagd aantal stations waar een fiets geleend kan worden.
    :param stations: lijst van stations
    :param amount_of_stations: aantal stations met beschikbare fietsen dat er moeten gezocht worden
    :return: lijst met random stations waar fietsen beschikbaar zijn.
    """
    available = []
    while len(available) < amount_of_stations:
        station = random.choice(stations)
        if station.sloten < station.capaciteit:
            if station not in available:
                available.append(station)
    for station in available:
        print(f"{station.capaciteit - station.sloten} fietsen beschikbaar in station {station.naam}")
    return available


def available_stations(stations, amount_of_stations=5):
    """
    Functie geeft een lijst terug met gevraagd aantal stations waar een fiets geplaatst kan worden.
    :param stations: lijst van stations
    :param amount_of_stations: aantal stations met beschikbare sloten dat er moeten gezocht worden
    :return: lijst met random stations waar sloten beschikbaar zijn.
    """
    available = []
    while len(available) < amount_of_stations:
        station = random.choice(stations)
        if station.sloten > 0:
            if station not in available:
                available.append(station)
    for station in available:
        print(f"{station.sloten} sloten beschikbaar in station {station.naam}")
    return available


def random_user(amount=1000):
    """
    :param amount: aantal te genereren namen
    :return: Lijst met random namen
    """
    users = []
    namen = ["Jan", "Piet", "Joris", "Korneel", "Marie", "Eva", "Lisa", "Tom", "Sophie", "Emma", "Mohammed", "Hassan",
             "Fatima", "Aisha", "Liam", "Noah", "Olivia", "Emma", "Sophia", "Ava", "Isabella", "Mia", "Charlotte",
             "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila",
             "Aria", "Scarlett", "Victoria", "Madison", "Luna", "Grace", "Chloe", "Penelope", "Layla", "Riley", "Zoey",
             "Nora", "Lily", "Eleanor", "Hannah", "Lillian", "Addison", "Aubrey", "Ellie", "Stella", "Natalie", "Zoe",
             "Leah", "Hazel", "Violet", "Aurora", "Savannah", "Audrey", "Brooklyn", "Bella", "Claire", "Skylar", "Lucy",
             "Paisley", "Everly", "Anna", "Caroline", "Nova", "Genesis", "Emilia", "Kennedy", "Samantha", "Maya",
             "Willow", "Kinsley", "Naomi", "Aaliyah", "Elena", "Sarah", "Ariana", "Allison", "Gabriella", "Alice",
             "Madelyn", "Cora", "Ruby", "Eva", "Serenity", "Autumn", "Adeline", "Hailey", "Gianna", "Valentina", "Isla",
             "Eliana", "Quinn", "Nevaeh", "Ivy"]
    achternamen = ["Janssen", "De Vries", "Van der Meer", "Van den Berg", "Bakker", "Visser", "Smit", "Meijer",
                   "Mulder", "De Boer", "Kuipers", "Jacobs", "Hendriks", "Vermeulen", "Van Dijk", "Bos", "Peters",
                   "Hermans", "Van Leeuwen", "Dijkstra", "Kramer", "Klein", "Verbeek", "Willems", "Van der Linden",
                   "Kok", "Prins", "Vos", "Brouwer", "Sanders", "Van der Laan", "Van den Heuvel", "Lammers",
                   "Van der Heijden", "Scholten", "Schouten", "Wolters", "Van Beek", "Van Dam", "Jonker",
                   "Van den Broek", "Hoekstra", "Bosch", "Kuijpers", "Huisman", "Postma", "Gerritsen", "Martens",
                   "Veenstra", "Van der Wal", "Groen", "Hendriksen", "Koster", "Bosman", "Van Wijk", "Van Doorn",
                   "Verhoeven", "Van der Velden", "Jansen", "Bosch", "Hermans", "Van den Heuvel", "Timmermans",
                   "Peters", "Smeets", "Van der Ven", "Timmer", "Van der Horst", "Van den Brink", "Dekker",
                   "Van der Voort", "Van der Valk", "Scheffer", "Beekman", "Van de Velde", "Blom", "Schipper",
                   "Van der Plas", "Langeveld", "Wolff", "Groeneveld", "Bakker", "Bosman", "Vos", "Van den Brink",
                   "Van Dijk", "Smeets", "Bosch", "Hermans", "Martens", "Van der Horst", "Schipper", "Van der Wal",
                   "Van der Ven", "Timmermans", "Van der Laan", "Smit"]
    for i in range(amount):
        voornaam = random.choice(namen)
        naam = random.choice(achternamen)
        user_ = Gebruiker(i+1, naam, voornaam)
        users.append(user_)
    return users


def random_transporters(amount=10):
    transporters = []
    for i in range(amount):
        transporters.append(Transporteur(i))
    return transporters


def maak_stations():
    """
    Functie leest json data uit en maakt op basis van deze data stations aan
    :return: Lijst van stations met correcte naam, aantal sloten en id
    """
    stations = []
    with open("velo.geojson", "r") as file1:
        read_content = file1.read()
        # parse json to dictionary
        data_dict = json.loads(read_content)
        # read name and slots for each station
    for station in data_dict["features"]:
        naam = station["properties"]["Naam"]
        plaatsen = station["properties"]["Aantal_plaatsen"]
        station_id = station["properties"]["OBJECTID"]
        # maak station objecten aan met json data
        stations.append(Station(plaatsen, naam, station_id))
    return stations


def vul_stations(stations, aantal_fietsen=2000):
    """
    :param stations: lijst met stations die voorzien moeten worden van fietsen
    :param aantal_fietsen: aantal fietsen te verdelen over de lijst van stations
    :return: geeft orginele lijst van stations terug, gevuld met fietsen
    """
    i = 0
    succes = 0
    while succes < aantal_fietsen:
        gekozen_station = random.choice(stations)
        if gekozen_station.add_bike(Fiets(i+1)):
            succes += 1
            # telt aantal succesvol geplaatste fietsen
        i += 1
    return stations


def get_html_users(data="logje.json"):
    html_string = ""
    template_env = Environment(loader=FileSystemLoader(searchpath='./'))
    template = template_env.get_template("users.html")
    with open(data) as f:
        inhoud = json.load(f)
        for interactie in inhoud:
            if interactie["type"] == "gebruiker":
                if interactie["actie"] == "lenen":
                    html_string += '<tr class="red-row">'
                else:
                    html_string += '<tr class="green-row">'
                html_string += f'<td>{interactie["type"]}</td>'
                html_string += f'<td>{interactie["actie"]}</td>'
                html_string += f'<td>{interactie["station"]}</td>'
                html_string += f'<td>{interactie["naam"]}</td>'
                html_string += f'<td>{interactie["achternaam"]}</td>'
                html_string += f'<td>{interactie["id"]}</td>'
                html_string += f'<td>{interactie["fiets id"]}</td>'
                html_string += "</tr>"

    with open("log_users.html", "w") as output_file:
        output_file.write(
            template.render(
                rows=html_string
            )
        )


def get_html_transporters(data="logje.json"):
    html_string = ""
    template_env = Environment(loader=FileSystemLoader(searchpath='./'))
    template = template_env.get_template("transporters.html")
    with open(data) as f:
        inhoud = json.load(f)
        for interactie in inhoud:
            if interactie["type"] == "transporteur":
                if interactie["actie"] == "lenen":
                    html_string += '<tr class="red-row">'
                else:
                    html_string += '<tr class="green-row">'
                html_string += f'<td>{interactie["type"]}</td>'
                html_string += f'<td>{interactie["actie"]}</td>'
                html_string += f'<td>{interactie["station"]}</td>'
                html_string += f'<td>{interactie["aantal fietsen"]}</td>'
                html_string += f'<td>{interactie["id"]}</td>'
                html_string += "</tr>"

    with open("log_transporters.html", "w") as output_file:
        output_file.write(
            template.render(
                rows=html_string
            )
        )


def leen_fiets(stations, type_of_user, user, main):
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
                            leen_fiets(stations, "gebruiker", user, main)
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
                            leen_fiets(stations, "transporteur", user, main)
                        else:
                            user.neem_fietsen(element, fietsen_nemen)
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
                    leen_fiets(stations, "transporteur", user, main)
                else:
                    user.neem_fietsen(transporteur_station, fietsen_nemen)
                    main()
            case 3:
                main()


def zet_fiets_terug(stations, type_of_user, user, main):
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
                            zet_fiets_terug(stations, "gebruiker", user, main)
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
                            zet_fiets_terug(stations, "transporteur", user, main)
                        else:
                            user.plaats_fietsen(element, fietsen_plaatsen)
                            print(f"{fietsen_plaatsen} fietsen in station {element.naam}")
                            main()
            case 2:
                available = available_stations(stations)
                gekozen_station = int(input("kies station 1 - 5: "))
                transporteur_station = available[gekozen_station - 1]
                print(f"{transporteur_station.sloten} plaatsen beschikbaar in {transporteur_station.naam}")
                fietsen_plaatsen = int(input("Hoeveel fietsen in station zetten?: "))
                if len(user.fietsen) >= fietsen_plaatsen:
                    if fietsen_plaatsen > transporteur_station.sloten:
                        print("niet genoeg plaatsen beschikbaar")
                        zet_fiets_terug(stations, "transporteur", user, main)
                    else:
                        user.plaats_fietsen(transporteur_station, fietsen_plaatsen)
                        main()
                else:
                    print(f"je hebt nog maar {len(user.fietsen)} beschikbaar")
                    zet_fiets_terug(stations, "transporteur", user, main)
            case 3:
                main()


def simulation_mode(restart, stations, main, speed=0.5, users_par=None, transporters_par=None):
    user_type = ["gebruiker", "gebruiker", "gebruiker", "gebruiker", "gebruiker", "gebruiker", "transporteur",
                 "transporteur"]
    opdracht_type = ["plaats", "leen"]
    if restart:
        users = random_user(100)
        transporters = random_transporters(10)
        try:
            while True:
                person = random.choice(user_type)
                opdracht = random.choice(opdracht_type)
                handeling_set = set()
                handeling_set.add(person)
                handeling_set.add(opdracht)
                if handeling_set == {"gebruiker", "plaats"}:
                    current_user = random.choice(users)
                    current_user.neem_fiets(random.choice(stations))
                elif handeling_set == {"gebruiker", "leen"}:
                    current_user = random.choice(users)
                    current_user.plaats_fiets(random.choice(stations))
                elif handeling_set == {"transporteur", "plaats"}:
                    current_user = random.choice(transporters)
                    current_user.plaats_fietsen(random.choice(stations), random.randint(1, 20))
                elif handeling_set == {"transporteur", "leen"}:
                    current_user = random.choice(transporters)
                    current_user.neem_fietsen(random.choice(stations), random.randint(1, 20))
                time.sleep(1/speed)
        except KeyboardInterrupt:
            data = [users, transporters, stations]
            with open("pickle.dat", 'wb') as f:
                pickle.dump(data, f)
            log.dump_data()
            main()
    else:
        users = users_par
        transporters = transporters_par
        try:
            while True:
                person = random.choice(user_type)
                opdracht = random.choice(opdracht_type)
                handeling_set = set()
                handeling_set.add(person)
                handeling_set.add(opdracht)
                if handeling_set == {"gebruiker", "plaats"}:
                    current_user = random.choice(users)
                    current_user.neem_fiets(random.choice(stations))
                elif handeling_set == {"gebruiker", "leen"}:
                    current_user = random.choice(users)
                    current_user.plaats_fiets(random.choice(stations))
                elif handeling_set == {"transporteur", "plaats"}:
                    current_user = random.choice(transporters)
                    current_user.plaats_fietsen(random.choice(stations), random.randint(1, 20))
                elif handeling_set == {"transporteur", "leen"}:
                    current_user = random.choice(transporters)
                    current_user.neem_fietsen(random.choice(stations), random.randint(1, 20))
                time.sleep(1/speed)
        except KeyboardInterrupt:
            data = [users, transporters, stations]
            with open("pickle.dat", 'wb') as f:
                pickle.dump(data, f)
            log.dump_data()
            main()
