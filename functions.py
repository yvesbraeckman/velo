import random
import json
from classes import *


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


def random_user(amount):
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


def vul_stations(stations, aantal_fietsen=4200):
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


def simulation_mode(restart):
    return None


def get_html():
    return None
